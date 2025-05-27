def process_instructions(instruction_string):
    # Initialize the state of mul (enabled at the start)
    mul_enabled = True
    total_sum = 0
    
    # Regular expression to match the relevant components: mul(a,b) and do()/don't()
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    # Split the input string by instructions
    parts = re.split(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", instruction_string)
    
    for part in parts:
        if re.match(mul_pattern, part):
            # If mul is enabled, process the multiplication
            match = re.match(mul_pattern, part)
            if match and mul_enabled:
                a, b = int(match.group(1)), int(match.group(2))
                total_sum += a * b
        elif re.match(do_pattern, part):
            # Enable mul
            mul_enabled = True
        elif re.match(dont_pattern, part):
            # Disable mul
            mul_enabled = False
    
    return total_sum