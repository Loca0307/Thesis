    def print(self):
        """
        Prints the value stored in vRAM at the specified index.
        """
        if len(self.line_words) == 2:
            _index = self.line_words[1]
            print(search_ram(_index))

    def store(self):
        """
        Stores a value in vRAM at the specified index.
        """
        if len(self.line_words) == 3:
            _index = self.line_words[1]
            _value = self.line_words[2]
            write_ram(_index, dec(_value))

    def read(self):
        """
        Reads and prints the value stored in vRAM at the specified index.
        """
        if len(self.line_words) == 2:
            _index = self.line_words[1]
            print(search_ram(_index))

    def input(self):
        """
        Stores input from the user into vRAM at the specified index.
        """
        if len(self.line_words) == 2:
            _index = self.line_words[1]
            _value = input("Enter value: ")
            write_ram(_index, dec(_value))

    def conditional(self):
        """
        Executes the next command if the condition is true.
        """
        if len(self.line_words) >= 4:
            _arg1 = self.line_words[1]
            _operator = self.line_words[2]
            _arg2 = self.line_words[3]
            if _operator == '==':
                if dec(_arg1) == dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])
            elif _operator == '!=':
                if dec(_arg1) != dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])
            elif _operator == '>':
                if dec(_arg1) > dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])
            elif _operator == '<':
                if dec(_arg1) < dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])
            elif _operator == '>=':
                if dec(_arg1) >= dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])
            elif _operator == '<=':
                if dec(_arg1) <= dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])

    def gt(self):
        """
        Checks if the first number is greater than the second.
        """
        if len(self.line_words) == 3:
            _arg1 = self.line_words[1]
            _arg2 = self.line_words[2]
            return dec(_arg1) > dec(_arg2)

    def lt(self):
        """
        Checks if the first number is less than the second.
        """
        if len(self.line_words) == 3:
            _arg1 = self.line_words[1]
            _arg2 = self.line_words[2]
            return dec(_arg1) < dec(_arg2)

    def eq(self):
        """
        Checks if the first number is equal to the second.
        """
        if len(self.line_words) == 3:
            _arg1 = self.line_words[1]
            _arg2 = self.line_words[2]
            return dec(_arg1) == dec(_arg2)

    def goto(self):
        """
        Jumps to the specified line number.
        """
        if len(self.line_words) == 2:
            _line_number = int(self.line_words[1])
            global program_counter
            program_counter = _line_number - 1

def main():
    """
    The main function to run the program.
    """
    file_name = sys.argv[1]
    file_lines = process_file(file_name)
    global ram
    ram = initialize_ram(RAM_SIZE)
    global commands
    commands = ['add','sub', 'print', 'store', 'read', 'input', 'if', 'gt', 'lt', 'eq', 'goto', 'exit']

    # main loop
    global program_counter
    program_counter = 0
    while program_counter < len(file_lines):
        try:
            program_counter += 1
            file_line = file_lines.pop(0)
            line_words = file_line.split(' ')
            if not line_words[0].isdigit():
                raise ValueError
        except IndexError:
            sys.exit("Error: Reached end of file unexpectedly")
        except ValueError:
            sys.exit(f"Error at line {program_counter}: lines must start with a number")
        
        # Evaluate the code
        for line_word in line_words:
            if len(line_words) == 0 or line_word == ';':
                continue
        _CommandTranslater(line_words[0], line_words)

if __name__ == "__main__":
    main()