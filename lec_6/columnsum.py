from randommatrix import  generate_random_matrix
def get_column_sum(matrix, column_index):
    if not matrix:
        return 0  # Return 0 if the matrix is empty.

    if column_index < 0 or column_index >= len(matrix[0]):
        raise ValueError("Invalid column index")


    return sum(matrix[:][column_index])



if __name__ == "__main__":
    # Example usage:
    row = int(input("Enter the count of rows.\n"))
    col = int(input("Enter the count of columns.\n"))
    random_matrix = generate_random_matrix(row, col)
    for row in random_matrix:
        print(row)

    idx = int(input("Enter column index for calculating sum.\n"))

    result = get_column_sum(random_matrix, idx)
    print(f"Sum of column {idx}: {result}")