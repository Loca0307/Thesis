func deriveBunDBMyOptions(cfg ClientConfig) (string, error) {
	// these are all optional, the bun adapter figures out defaults
	port := cfg.Port
	address := cfg.Address
	username := cfg.User
	password := cfg.Password

	// validate database
	database := cfg.Database
	if database == "" {
		return "", errors.New("no database set")
	}

	tlsConfig, err := makeTLSConfig(cfg)
	if err != nil {
		zap.L().Error("Error creating TLS config", zap.Error(err))
		return "", fmt.Errorf("could not create tls config: %w", err)
	}

	mysqlOptions := ""
	if username != "" {
		mysqlOptions += username
		if password != "" {
			mysqlOptions += ":" + password
		}
		mysqlOptions += "@"
	}
	if address != "" {
		mysqlOptions += "tcp(" + address
		if port > 0 {
			mysqlOptions += ":" + strconv.Itoa(int(port))
		}
		mysqlOptions += ")"
	}
	mysqlOptions += "/" + database

	// options
	if tlsConfig != nil {
		if err := mysql.RegisterTLSConfig("bun", tlsConfig); err != nil {
			return "", fmt.Errorf("could not register tls config: %w", err)
		}

		mysqlOptions += "?tls=bun"
	}

	return mysqlOptions, nil
}

func deriveBunDBPGOptions(cfg ClientConfig) (*pgx.ConnConfig, error) {