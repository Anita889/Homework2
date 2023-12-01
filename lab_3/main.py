def matrix_product(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    if cols1 != rows2:
        raise ValueError(
            "Invalid matrices for multiplication: Number of columns in the first matrix must be equal to the number "
            "of rows in the second matrix.")

    result_matrix = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix


def write_matrix_to_file(matrix, file_path):
    with open(file_path, 'w') as file:
        for row in matrix:
            file.write('\t'.join(map(str, row)))
            file.write('\n')


def main():
    # Example matrices
    matrix1 = [
        [23, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    # Calculate the product of matrices
    result_matrix = matrix_product(matrix1, matrix2)

    # Output the result to a file
    output_file_path = "product_result.txt"
    write_matrix_to_file(result_matrix, output_file_path)

    print("Matrix product result has been written to '{}'.".format(output_file_path))


if __name__ == "__main__":
    main()
