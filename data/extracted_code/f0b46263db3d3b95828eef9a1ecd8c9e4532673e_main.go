	ctx := context.Background()

	// Configure logger
	logger := slog.New(
		tint.NewHandler(os.Stderr, &tint.Options{
			Level:      slog.LevelDebug,
			TimeFormat: time.Kitchen,
		}),
	)

	// Set up Ollama provider
	opts := &ollama.ProviderOpts{
		Logger:  logger,
		BaseURL: "http://localhost",
		Port:    11434,
	}
	provider := ollama.NewProvider(opts)

	// Use the correct model
	model := &types.Model{
		ID: "llama3.2-vision:11b",
	}
	provider.UseModel(ctx, model)

	// Create agent configuration
	agentConf := &agent.NewAgentConfig{
		Provider:     provider,
		Logger:       logger,
		SystemPrompt: "You are a visual analysis assistant specialized in detailed image descriptions. If there is a person in the image describe what they are doing in step by step format.",
	}

	// Initialize agent
	visionAgent := agent.NewAgent(agentConf)

	// Parse command line arguments
	videoPath := "path/to/your/video.mp4"
	outputDir = "output_frames"  // default value

	for i := 1; i < len(os.Args); i++ {
		switch os.Args[i] {
		case "--video":
			if i+1 < len(os.Args) {
				videoPath = os.Args[i+1]
				i++
			}
		case "--output":
			if i+1 < len(os.Args) {
				outputDir = os.Args[i+1]
				i++
			}
		}
	}

	// Ensure video path is provided
	if videoPath == "path/to/your/video.mp4" {
		fmt.Println("Usage: go run main.go --video path/to/video.mp4 [--output output_directory]")
		os.Exit(1)
	}

	// After parsing the video path, set the videoName
	videoName = strings.TrimSuffix(filepath.Base(videoPath), filepath.Ext(videoPath))

	// Process video
	fmt.Printf("Starting video analysis...\n")
	err := processVideo(ctx, visionAgent, videoPath, outputDir)
	if err != nil {
		log.Printf("Error processing video: %v", err)
		os.Exit(1)
	}

	fmt.Println("Video processing completed successfully!")