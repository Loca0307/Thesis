        lines = file.readlines()
        if len(lines) < 2:
            logging.error(f"File {downloaded_filename} does not contain enough data.")
            exit(1)
        second_line = lines[1]