import os
import sys
import chardet

# Define a function to read and decode binary data
def read_binary_file(filename):
    # Open the file in binary mode
    with open(filename, 'rb') as f:
        # Read the binary data from the file
        binary_data = f.read()
        # Determine the file encoding
        encoding = chardet.detect(binary_data)['encoding']
        # Decode the binary data to text
        text_data = binary_data.decode(encoding)
    return text_data

# Define the main function to parse command line arguments
def main():
    # Get the filename from the command line arguments
    filename = sys.argv[1]
    # Check if the file exists
    if not os.path.isfile(filename):
        print("File not found")
        return
    # Check if the file is a binary file
    if os.path.isfile(filename) and os.access(filename, os.X_OK):
        print("This is an executable file")
        return
    else:
        # Read and decode the file data
        text_data = read_binary_file(filename)
        # Print the decoded data to the console
        print(text_data)

if __name__ == '__main__':
    main()
