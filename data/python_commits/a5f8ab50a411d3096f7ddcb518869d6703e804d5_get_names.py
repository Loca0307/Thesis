read_file_path = 'petpets/raw_names.txt'
write_file_path = 'petpets/names.txt'

# Read all petpet names from the file
with open(read_file_path, 'r') as file:
    raw_names = file.read().splitlines()

def check_if_valid(line):
    res = []
    words = line.split(" ")
    for word in words:
        word = word.strip("'")
        word = word.strip('"')
        if len(word) == 5:
            res.append(word)
    return res

# Will overwrite file every time this script is run (w for overwrite)
count = 0
with open(write_file_path, 'w') as file:
    for name in raw_names:
        valid_names = check_if_valid(name)
        for valid_name in valid_names:
            count += 1
            file.write(f"{valid_name}\n")

print(f"Saved {count} names to {write_file_path}")