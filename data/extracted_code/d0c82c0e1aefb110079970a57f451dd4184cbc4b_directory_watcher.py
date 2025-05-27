    if not new_files:
        logger.info("No new files found.")
        return None

    # Process the first new file
    for new_file in new_files:
        if new_file.is_file():
            # Check for duplicate filenames and rename the file by appending a timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            # If a file with the same name exists, append a timestamp to avoid conflicts
            new_filename = f"{new_file.stem}_{timestamp}{new_file.suffix}"
            new_file_path = directory_to_watch / new_filename
            
            # Loop to ensure no conflicts even after renaming
            while new_file_path.exists():
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                new_filename = f"{new_file.stem}_{timestamp}{new_file.suffix}"
                new_file_path = directory_to_watch / new_filename
            
            new_file.rename(new_file_path)
            new_file = new_file_path
    
            new_filepath = new_file.with_name(new_filename)
            new_file.rename(new_filepath)
            logger.info(f"Renamed file: {new_file.name} -> {new_filename}")