func (d driver) checkVersion(dsn string) error {
	parsedURL, err := url.Parse(dsn)
	if err != nil {
		return err
	}
	parsedURL.Path = "/status"
	statusURL := parsedURL.String()

	req, err := http.NewRequest(http.MethodGet, statusURL, http.NoBody)
	if err != nil {
		return err
	}

	client := &http.Client{Timeout: 10 * time.Second}
	resp, err := client.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("druid version check failed with status code: %d", resp.StatusCode)
	}

	var statusResponse struct {
		Version string `json:"version"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&statusResponse); err != nil {
		return fmt.Errorf("failed to decode Druid status response: %w", err)
	}

	if statusResponse.Version != "" {
		majorVersion := strings.Split(statusResponse.Version, ".")[0]
		if ver, err := strconv.Atoi(majorVersion); err == nil {
			if ver < 28 {
				return fmt.Errorf("druid version %s is not supported, please use 28.0.0 or higher", statusResponse.Version)
			}
		} else {
			return fmt.Errorf("failed to parse Druid version: %w", err)
		}
	} else {
		return fmt.Errorf("druid version information not found in the response")
	}

	return nil
}
