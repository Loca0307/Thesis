import numpy as np

def generate_hilbert_matrix(size):
    """Generates a Hilbert matrix of given size."""
    hilbert_matrix = np.array([[1 / (i + j + 1) for j in range(size)] for i in range(size)])
    return hilbert_matrix

if __name__ == "__main__":
    size = 12
    hilbert_matrix = generate_hilbert_matrix(size)
    print(hilbert_matrix)