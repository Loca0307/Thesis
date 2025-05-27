    
    args = parser.parse_args()
    
    # If query is not provided via command line, read from stdin
    if args.query is None:
        # Check if there's data available on stdin (e.g., from a pipe)
        if not sys.stdin.isatty():
            args.query = sys.stdin.read().strip()
            # Validate that the input is not empty after stripping whitespace
            if not args.query:
                sys.stderr.write("Error: Empty input provided via stdin. Please provide a non-empty query.\n")
                sys.exit(1)
        else:
            # Exit with error if no query is provided
            sys.stderr.write("Error: No query provided. Please provide a query via --query parameter or pipe input to stdin.\n")
            sys.exit(1)
    
    return args