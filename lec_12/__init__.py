import random
import time


# Function to generate a file with 100 lines, each containing 20 random numbers
def generate_file(filename):
    with open(filename, 'w') as file:
        for _ in range(100):
            numbers = ' '.join(str(random.randint(1, 100)) for _ in range(20))
            file.write(numbers + '\n')


# Decorator to measure function execution time
def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
        return result

    return wrapper


# Function to convert a line into an integer array
def line_to_int_array(line):
    return list(map(int, line.split()))


# Function to filter numbers greater than 40
def filter_numbers(numbers):
    return list(filter(lambda x: x > 40, numbers))


# Function to process the file using map and filter functions
@measure_execution_time
def process_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Using map function to convert lines into integer arrays
    integer_arrays = list(map(line_to_int_array, lines))

    # Using filter function to filter numbers greater than 40
    filtered_arrays = list(map(filter_numbers, integer_arrays))

    # Writing the filtered data back to the file
    with open(filename, 'w') as file:
        for array in filtered_arrays:
            file.write(' '.join(map(str, array)) + '\n')


# Generator function to yield lines from a file
def read_file_as_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line_to_int_array(line)


# Example usage
filename = 'random_numbers.txt'

# Generate a file with random numbers (each line contains exactly 20 numbers)
generate_file(filename)

# Process the file using map and filter functions
process_file(filename)

# Read the file as a generator using yield
generator = read_file_as_generator(filename)

# Print the first few lines of the generator
for _ in range(5):
    print(next(generator))
