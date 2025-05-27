	uptrace.ConfigureOpentelemetry(
		uptrace.WithServiceName("mcp-dbmem"),
		uptrace.WithServiceVersion(viper.GetString(config.Keys.SoftwareVersion)),
	)
