        print("\nERROR DURING SIGNAL GENERATION:")
        print("-" * 60)
        
        import traceback
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        print("\nTraceback:")
        traceback.print_exc()
        
        print("\nDIAGNOSTIC INFORMATION:")
        try:
            print(f"TensorFlow imported: {'tf' in globals()}")
            if 'tf' in globals():
                print(f"TensorFlow version: {tf.__version__}")
            
            # Check input parameters
            print(f"\nInput parameters:")
            print(f"  Mode: {args.mode}")
            print(f"  Num samples: {args.num_samples}")
            print(f"  Add noise: {args.add_noise}")
            print(f"  Oversampling: {args.oversampling}")
            
            # Check if frequency range is properly defined
            print(f"\nFrequency configuration:")
            if hasattr(generator, 'center_freq'):
                print(f"  Center frequency: {generator.center_freq} MHz")
            
            # Check for file system issues
            print(f"\nOutput directory:")
            print(f"  Path: {args.output_dir}")
            print(f"  Exists: {os.path.exists(args.output_dir)}")
            print(f"  Writable: {os.access(args.output_dir, os.W_OK) if os.path.exists(args.output_dir) else 'N/A'}")
            
            # import psutil   
            # process = psutil.Process(os.getpid())
            # print(f"\nMemory usage: {process.memory_info().rss / (1024 * 1024):.2f} MB")
            
        except Exception as diag_error:
            print(f"Error during diagnostics: {diag_error}")
        
        print("-" * 60)