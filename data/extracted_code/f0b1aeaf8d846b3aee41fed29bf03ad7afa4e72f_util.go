
		resp = append(r.Data.Children, nextFiles...)
	}

	return resp, err
}

func (d *Doubao) getUserInfo() (UserInfo, error) {
	var r UserInfoResp

	_, err := d.request("/passport/account/info/v2/", http.MethodGet, nil, &r)
	if err != nil {
		return UserInfo{}, err
	}

	return r.Data, err
}

// 签名请求
func (d *Doubao) signRequest(req *resty.Request, method, tokenType, uploadUrl string) error {
	parsedUrl, err := url.Parse(uploadUrl)
	if err != nil {
		return fmt.Errorf("invalid URL format: %w", err)
	}

	var accessKeyId, secretAccessKey, sessionToken string
	var serviceName string

	if tokenType == VideoDataType {
		accessKeyId = d.UploadToken.Samantha.StsToken.AccessKeyID
		secretAccessKey = d.UploadToken.Samantha.StsToken.SecretAccessKey
		sessionToken = d.UploadToken.Samantha.StsToken.SessionToken
		serviceName = "vod"
	} else {
		accessKeyId = d.UploadToken.Alice[tokenType].Auth.AccessKeyID
		secretAccessKey = d.UploadToken.Alice[tokenType].Auth.SecretAccessKey
		sessionToken = d.UploadToken.Alice[tokenType].Auth.SessionToken
		serviceName = "imagex"
	}

	// 当前时间，格式为 ISO8601
	now := time.Now().UTC()
	amzDate := now.Format("20060102T150405Z")
	dateStamp := now.Format("20060102")

	req.SetHeader("X-Amz-Date", amzDate)

	if sessionToken != "" {
		req.SetHeader("X-Amz-Security-Token", sessionToken)
	}

	// 计算请求体的SHA256哈希
	var bodyHash string
	if req.Body != nil {
		bodyBytes, ok := req.Body.([]byte)
		if !ok {
			return fmt.Errorf("request body must be []byte")
		}

		bodyHash = hashSHA256(string(bodyBytes))
		req.SetHeader("X-Amz-Content-Sha256", bodyHash)
	} else {
		bodyHash = hashSHA256("")
	}

	// 创建规范请求
	canonicalURI := parsedUrl.Path
	if canonicalURI == "" {
		canonicalURI = "/"
	}

	// 查询参数按照字母顺序排序
	canonicalQueryString := getCanonicalQueryString(req.QueryParam)
	// 规范请求头
	canonicalHeaders, signedHeaders := getCanonicalHeadersFromMap(req.Header)
	canonicalRequest := method + "\n" +
		canonicalURI + "\n" +
		canonicalQueryString + "\n" +
		canonicalHeaders + "\n" +
		signedHeaders + "\n" +
		bodyHash

	algorithm := "AWS4-HMAC-SHA256"
	credentialScope := fmt.Sprintf("%s/%s/%s/aws4_request", dateStamp, Region, serviceName)

	stringToSign := algorithm + "\n" +
		amzDate + "\n" +
		credentialScope + "\n" +
		hashSHA256(canonicalRequest)
	// 计算签名密钥
	signingKey := getSigningKey(secretAccessKey, dateStamp, Region, serviceName)
	// 计算签名
	signature := hmacSHA256Hex(signingKey, stringToSign)
	// 构建授权头
	authorizationHeader := fmt.Sprintf(
		"%s Credential=%s/%s, SignedHeaders=%s, Signature=%s",
		algorithm,
		accessKeyId,
		credentialScope,
		signedHeaders,
		signature,
	)

	req.SetHeader("Authorization", authorizationHeader)

	return nil
}

func (d *Doubao) requestApi(url, method, tokenType string, callback base.ReqCallback, resp interface{}) ([]byte, error) {
	req := base.RestyClient.R()
	req.SetHeaders(map[string]string{
		"user-agent": UserAgent,
	})

	if method == http.MethodPost {
		req.SetHeader("Content-Type", "text/plain;charset=UTF-8")
	}

	if callback != nil {
		callback(req)
	}

	if resp != nil {
		req.SetResult(resp)
	}

	// 使用自定义AWS SigV4签名
	err := d.signRequest(req, method, tokenType, url)
	if err != nil {
		return nil, err
	}

	res, err := req.Execute(method, url)
	if err != nil {
		return nil, err
	}

	return res.Body(), nil
}

func (d *Doubao) initUploadToken() (*UploadToken, error) {
	uploadToken := &UploadToken{
		Alice:    make(map[string]UploadAuthToken),
		Samantha: MediaUploadAuthToken{},
	}

	fileAuthToken, err := d.getUploadAuthToken(FileDataType)
	if err != nil {
		return nil, err
	}

	imgAuthToken, err := d.getUploadAuthToken(ImgDataType)
	if err != nil {
		return nil, err
	}

	mediaAuthToken, err := d.getSamantaUploadAuthToken()
	if err != nil {
		return nil, err
	}

	uploadToken.Alice[FileDataType] = fileAuthToken
	uploadToken.Alice[ImgDataType] = imgAuthToken
	uploadToken.Samantha = mediaAuthToken

	return uploadToken, nil
}

func (d *Doubao) getUploadAuthToken(dataType string) (ut UploadAuthToken, err error) {
	var r UploadAuthTokenResp
	_, err = d.request("/alice/upload/auth_token", http.MethodPost, func(req *resty.Request) {
		req.SetBody(base.Json{
			"scene":     "bot_chat",
			"data_type": dataType,
		})
	}, &r)

	return r.Data, err
}

func (d *Doubao) getSamantaUploadAuthToken() (mt MediaUploadAuthToken, err error) {
	var r MediaUploadAuthTokenResp
	_, err = d.request("/samantha/media/get_upload_token", http.MethodPost, func(req *resty.Request) {
		req.SetBody(base.Json{})
	}, &r)

	return r.Data, err
}

// getUploadConfig 获取上传配置信息
func (d *Doubao) getUploadConfig(upConfig *UploadConfig, dataType string, file model.FileStreamer) error {
	tokenType := dataType
	// 配置参数函数
	configureParams := func() (string, map[string]string) {
		var uploadUrl string
		var params map[string]string
		// 根据数据类型设置不同的上传参数
		switch dataType {
		case VideoDataType:
			// 音频/视频类型 - 使用uploadToken.Samantha的配置
			uploadUrl = d.UploadToken.Samantha.UploadInfo.VideoHost
			params = map[string]string{
				"Action":       "ApplyUploadInner",
				"Version":      "2020-11-19",
				"SpaceName":    d.UploadToken.Samantha.UploadInfo.SpaceName,
				"FileType":     "video",
				"IsInner":      "1",
				"NeedFallback": "true",
				"FileSize":     strconv.FormatInt(file.GetSize(), 10),
				"s":            randomString(),
			}
		case ImgDataType, FileDataType:
			// 图片或其他文件类型 - 使用uploadToken.Alice对应配置
			uploadUrl = "https://" + d.UploadToken.Alice[dataType].UploadHost
			params = map[string]string{
				"Action":        "ApplyImageUpload",
				"Version":       "2018-08-01",
				"ServiceId":     d.UploadToken.Alice[dataType].ServiceID,
				"NeedFallback":  "true",
				"FileSize":      strconv.FormatInt(file.GetSize(), 10),
				"FileExtension": filepath.Ext(file.GetName()),
				"s":             randomString(),
			}
		}
		return uploadUrl, params
	}

	// 获取初始参数
	uploadUrl, params := configureParams()

	tokenRefreshed := false
	var configResp UploadConfigResp

	err := d._retryOperation("get upload_config", func() error {
		configResp = UploadConfigResp{}

		_, err := d.requestApi(uploadUrl, http.MethodGet, tokenType, func(req *resty.Request) {
			req.SetQueryParams(params)
		}, &configResp)
		if err != nil {
			return err
		}

		if configResp.ResponseMetadata.Error.Code == "" {
			*upConfig = configResp.Result
			return nil
		}

		// 100028 凭证过期
		if configResp.ResponseMetadata.Error.CodeN == 100028 && !tokenRefreshed {
			log.Debugln("[doubao] Upload token expired, re-fetching...")
			newToken, err := d.initUploadToken()
			if err != nil {
				return fmt.Errorf("failed to refresh token: %w", err)
			}

			d.UploadToken = newToken
			tokenRefreshed = true
			uploadUrl, params = configureParams()

			return retry.Error{errors.New("token refreshed, retry needed")}
		}

		return fmt.Errorf("get upload_config failed: %s", configResp.ResponseMetadata.Error.Message)
	})

	return err
}

// uploadNode 上传 文件信息
func (d *Doubao) uploadNode(uploadConfig *UploadConfig, dir model.Obj, file model.FileStreamer, dataType string) (UploadNodeResp, error) {
	reqUuid := uuid.New().String()
	var key string
	var nodeType int

	mimetype := file.GetMimetype()
	switch dataType {
	case VideoDataType:
		key = uploadConfig.InnerUploadAddress.UploadNodes[0].Vid
		if strings.HasPrefix(mimetype, "audio/") {
			nodeType = AudioType // 音频类型
		} else {
			nodeType = VideoType // 视频类型
		}
	case ImgDataType:
		key = uploadConfig.InnerUploadAddress.UploadNodes[0].StoreInfos[0].StoreURI
		nodeType = ImageType // 图片类型
	default: // FileDataType
		key = uploadConfig.InnerUploadAddress.UploadNodes[0].StoreInfos[0].StoreURI
		nodeType = FileType // 文件类型
	}

	var r UploadNodeResp
	_, err := d.request("/samantha/aispace/upload_node", http.MethodPost, func(req *resty.Request) {
		req.SetBody(base.Json{
			"node_list": []base.Json{
				{
					"local_id":     reqUuid,
					"parent_id":    dir.GetID(),
					"name":         file.GetName(),
					"key":          key,
					"node_content": base.Json{},
					"node_type":    nodeType,
					"size":         file.GetSize(),
				},
			},
			"request_id": reqUuid,
		})
	}, &r)

	return r, err
}

// Upload 普通上传实现
func (d *Doubao) Upload(config *UploadConfig, dstDir model.Obj, file model.FileStreamer, up driver.UpdateProgress, dataType string) (model.Obj, error) {
	data, err := io.ReadAll(file)
	if err != nil {
		return nil, err
	}

	// 计算CRC32
	crc32Hash := crc32.NewIEEE()
	crc32Hash.Write(data)
	crc32Value := hex.EncodeToString(crc32Hash.Sum(nil))

	// 构建请求路径
	uploadNode := config.InnerUploadAddress.UploadNodes[0]
	storeInfo := uploadNode.StoreInfos[0]
	uploadUrl := fmt.Sprintf("https://%s/upload/v1/%s", uploadNode.UploadHost, storeInfo.StoreURI)

	uploadResp := UploadResp{}

	if _, err = d.uploadRequest(uploadUrl, http.MethodPost, storeInfo, func(req *resty.Request) {
		req.SetHeaders(map[string]string{
			"Content-Type":        "application/octet-stream",
			"Content-Crc32":       crc32Value,
			"Content-Length":      fmt.Sprintf("%d", len(data)),
			"Content-Disposition": fmt.Sprintf("attachment; filename=%s", url.QueryEscape(storeInfo.StoreURI)),
		})

		req.SetBody(data)
	}, &uploadResp); err != nil {
		return nil, err
	}

	if uploadResp.Code != 2000 {
		return nil, fmt.Errorf("upload failed: %s", uploadResp.Message)
	}

	uploadNodeResp, err := d.uploadNode(config, dstDir, file, dataType)
	if err != nil {
		return nil, err
	}

	return &model.Object{
		ID:       uploadNodeResp.Data.NodeList[0].ID,
		Name:     uploadNodeResp.Data.NodeList[0].Name,
		Size:     file.GetSize(),
		IsFolder: false,
	}, nil
}

// UploadByMultipart 分片上传
func (d *Doubao) UploadByMultipart(ctx context.Context, config *UploadConfig, fileSize int64, dstDir model.Obj, file model.FileStreamer, up driver.UpdateProgress, dataType string) (model.Obj, error) {
	// 构建请求路径
	uploadNode := config.InnerUploadAddress.UploadNodes[0]
	storeInfo := uploadNode.StoreInfos[0]
	uploadUrl := fmt.Sprintf("https://%s/upload/v1/%s", uploadNode.UploadHost, storeInfo.StoreURI)
	// 初始化分片上传
	var uploadID string
	err := d._retryOperation("Initialize multipart upload", func() error {
		var err error
		uploadID, err = d.initMultipartUpload(config, uploadUrl, storeInfo)
		return err
	})
	if err != nil {
		return nil, fmt.Errorf("failed to initialize multipart upload: %w", err)
	}
	// 准备分片参数
	chunkSize := DefaultChunkSize
	if config.InnerUploadAddress.AdvanceOption.SliceSize > 0 {
		chunkSize = int64(config.InnerUploadAddress.AdvanceOption.SliceSize)
	}
	totalParts := (fileSize + chunkSize - 1) / chunkSize
	// 创建分片信息组
	parts := make([]UploadPart, totalParts)
	// 缓存文件
	tempFile, err := file.CacheFullInTempFile()
	if err != nil {
		return nil, fmt.Errorf("failed to cache file: %w", err)
	}
	defer tempFile.Close()
	up(10.0) // 更新进度
	// 设置并行上传
	threadG, uploadCtx := errgroup.NewGroupWithContext(ctx, d.uploadThread,
		retry.Attempts(1),
		retry.Delay(time.Second),
		retry.DelayType(retry.BackOffDelay))

	var partsMutex sync.Mutex
	// 并行上传所有分片
	for partIndex := int64(0); partIndex < totalParts; partIndex++ {
		if utils.IsCanceled(uploadCtx) {
			break
		}
		partIndex := partIndex
		partNumber := partIndex + 1 // 分片编号从1开始

		threadG.Go(func(ctx context.Context) error {
			// 计算此分片的大小和偏移
			offset := partIndex * chunkSize
			size := chunkSize
			if partIndex == totalParts-1 {
				size = fileSize - offset
			}

			limitedReader := driver.NewLimitedUploadStream(ctx, io.NewSectionReader(tempFile, offset, size))
			// 读取数据到内存
			data, err := io.ReadAll(limitedReader)
			if err != nil {
				return fmt.Errorf("failed to read part %d: %w", partNumber, err)
			}
			// 计算CRC32
			crc32Value := calculateCRC32(data)
			// 使用_retryOperation上传分片
			var uploadPart UploadPart
			if err = d._retryOperation(fmt.Sprintf("Upload part %d", partNumber), func() error {
				var err error
				uploadPart, err = d.uploadPart(config, uploadUrl, uploadID, partNumber, data, crc32Value)
				return err
			}); err != nil {
				return fmt.Errorf("part %d upload failed: %w", partNumber, err)
			}
			// 记录成功上传的分片
			partsMutex.Lock()
			parts[partIndex] = UploadPart{
				PartNumber: strconv.FormatInt(partNumber, 10),
				Etag:       uploadPart.Etag,
				Crc32:      crc32Value,
			}
			partsMutex.Unlock()
			// 更新进度
			progress := 10.0 + 90.0*float64(threadG.Success()+1)/float64(totalParts)
			up(math.Min(progress, 95.0))

			return nil
		})
	}

	if err = threadG.Wait(); err != nil {
		return nil, err