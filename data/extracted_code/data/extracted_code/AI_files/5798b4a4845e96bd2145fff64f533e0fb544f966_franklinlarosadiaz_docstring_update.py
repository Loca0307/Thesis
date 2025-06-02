    """
    Converts a given DNA sequence to its RNA equivalent by replacing 
    'T' (thymine) with 'U' (uracil).

    Args:
        dna_sequence (str): A string representing a DNA sequence.
    
    Returns:
        str: A string representing the RNA sequence with 'T' replaced by 'U'.
    """
    return dna_sequence.replace('T', 'U')  # Replace 'T' with 'U'