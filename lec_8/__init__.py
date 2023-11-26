import random
class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.matrix = [[random.randint(-50, 50) for _ in range(m)] for _ in range(n)]

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def calculate_mean(self):
        total = sum(sum(row) for row in self.matrix)
        mean = total / (self.rows * self.cols)
        return mean

    def calculate_row_sum(self, row_index):
        if row_index < 0 or row_index >= self.rows:
            return "Invalid row index"
        return sum(self.matrix[row_index])

    def calculate_col_average(self, col_index):
        if col_index < 0 or col_index >= self.cols:
            return "Invalid column index"
        col_sum = sum(row[col_index] for row in self.matrix)
        col_average = col_sum / self.rows
        return col_average

    def print_submatrix(self, col1, col2, row1, row2):
        if row1 < 0 or row2 >= self.rows or col1 < 0 or col2 >= self.cols:
            print("Submatrix indices are out of bounds")
            return

        for i in range(row1, row2 + 1):
            print(self.matrix[i][col1:col2+1])


if __name__ == "__main__":
    # Example usage:
    n = 4
    m = 4
    my_matrix = Matrix(n, m)

    # Printing the matrix
    my_matrix.print_matrix()

    # Calculating the mean of the matrix
    mean = my_matrix.calculate_mean()
    print("Mean of the matrix:", mean)

    # Calculating the sum of a given row
    row_sum = my_matrix.calculate_row_sum(2)
    print("Sum of row 2:", row_sum)

    # Calculating the average of a given column
    col_avg = my_matrix.calculate_col_average(1)
    print("Average of column 1:", col_avg)

    # Printing a submatrix
    my_matrix.print_submatrix(1, 3, 0, 2)