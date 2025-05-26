#CS 472 
#NSHE ID: 5004634201     Franklin La Rosa Diaz
#Refactored code from ChatGPT
def get_valid_filename():
    """Prompt the user for a valid filename and return it."""
    while True:
        fname = input("Enter the file name: \n")
        try:
            with open(fname, 'r'):
                print("File accepted. Loading...\n")
                return fname
        except IOError:
            print("File not accessible. Try again.\n")

def transcribe_dna_to_rna(dna_sequence):
    """Convert DNA sequence to RNA by replacing 'T' with 'U'."""
    return dna_sequence.replace('T', 'U')

def read_file_and_transcribe(fname):
    """Read a DNA sequence file, transcribe it to RNA, and return the result."""
    with open(fname, 'r') as iFile:
        return [transcribe_dna_to_rna(line.strip()) for line in iFile]

# Actual Program Execution
filename = get_valid_filename()
rna_sequences = read_file_and_transcribe(filename)

# Output the result
for rna_seq in rna_sequences:
    print(rna_seq)