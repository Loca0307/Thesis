func handleStats(jsonStats string) models.InfluxDbFields {
	jsonLine := strings.Split(strings.TrimSpace(jsonStats), "\n")

	fields := models.InfluxDbFields{}

	for _, line := range jsonLine {
		var DockerStat models.DockerStat

		if err := json.Unmarshal([]byte(line), &DockerStat); err != nil {
			log.Printf("Error parsing JSON text '%s': %s\n", line, err)
			continue
		}

		parsedCPUPercentage, cpuParsingErr := parsePercentage(DockerStat.CPUPercentage)
		parsedMemPercentage, memParsingErr := parsePercentage(DockerStat.MemoryPercentage)
		parsedPidCount, pidParsingErr := strconv.Atoi(DockerStat.PIDs)

		if cpuParsingErr != nil {
			log.Printf("Error parsing CPU percentage: %s\n", cpuParsingErr)
			continue
		}

		if memParsingErr != nil {
			log.Printf("Error parsing Memory percentage: %s\n", memParsingErr)
			continue
		}

		if pidParsingErr != nil {
			log.Printf("Error parsing PID count: %s\n", pidParsingErr)
			continue
		}

		if _, exists := fields["cpu_usage_percentage"]; !exists {
			fields["cpu_usage_percentage"] = make([]models.InfluxDbTaggedValue, 0)
		}
		fields["cpu_usage_percentage"] = append(fields["cpu_usage_percentage"], models.InfluxDbTaggedValue{
			Value: parsedCPUPercentage,
			Tags: map[string]string{
				"container_name": DockerStat.Name,