import random

def generate_random_matrix(rows, cols):
    if rows <= 0 or cols <= 0:
        raise ValueError("Number of rows and columns must be positive integers.")

    matrix = []

    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)

    return matrix

# Example usage:
if __name__ == "__main__":
    row = int(input("Enter the count of rows.\n"))
    col = int(input("Enter the count of columns.\n"))
    random_matrix = generate_random_matrix(row, col)
    for row in random_matrix:
        print(row)