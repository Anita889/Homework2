from random_matrix import  generate_random_matrix
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
    from random_matrix import generate_random_matrix

def get_row_average(matrix, row_index):
    # Check if the row_index is within the valid range of rows in the matrix
    if row_index < 0 or row_index >= len(matrix):
        return None  # Invalid row index

    # Get the row specified by row_index
    row = matrix[row_index]

    # Calculate the sum of the elements in the row
    row_sum = sum(row)

    # Calculate the average by dividing the sum by the number of elements in the row
    if len(row) > 0:
        row_average = row_sum / len(row)
        return row_average
    else:
        return None  # Avoid division by zero for an empty row


if __name__ == "__main__":
    # Example usage:
    row = int(input("Enter the count of rows.\n"))
    col = int(input("Enter the count of columns.\n"))
    random_matrix = generate_random_matrix(row, col)
    for row in random_matrix:
        print(row)

    idx = int(input("Enter row index for calculating average of row.\n"))

    average = get_row_average(random_matrix, idx)

    if average is not None:
        print(f"Average of row {idx}: {average}")
    else:
        print(f"Invalid row index: {idx}")


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