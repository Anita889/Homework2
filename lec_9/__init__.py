import random

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.values = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.values])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition.")

        result = [[self.values[i][j] + other.values[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for subtraction.")

        result = [[self.values[i][j] - other.values[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for multiplication.")

        result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*other.values)] for row in self.values]
        return Matrix(self.rows, other.cols, result)

if __name__ == "__main__":
    matrix1 = Matrix(2, 2)
    matrix2 = Matrix(2, 2)

    print("Matrix 1:")
    print(matrix1)
    print()

    print("Matrix 2:")
    print(matrix2)
    print()

    # Addition
    add_result = matrix1 + matrix2
    print("Addition Result:")
    print(add_result)
    print()

    # Subtraction
    sub_result = matrix1 - matrix2
    print("Subtraction Result:")
    print(sub_result)
    print()

    # Multiplication
    mul_result = matrix1 * matrix2
    print("Multiplication Result:")
    print(mul_result)