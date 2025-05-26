
    if production:
        logHandler.addFilter(GoogleCloudLogFilter(project="openteams-score"))
        formatter = JsonFormatter()
        logHandler.setFormatter(formatter)
