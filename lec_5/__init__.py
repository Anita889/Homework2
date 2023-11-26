def sum_of_elements(numbers, exclude_negative=False):
    if exclude_negative:
        filtered_numbers = [num for num in numbers if num >= 0]
    else:
        filtered_numbers = numbers
    return sum(filtered_numbers)



if __name__ == "__main__":
    while True:
        # Input from the user
        user_input = input("Enter a list of numbers separated by spaces: ")
        if user_input.lower() == "exit":
            break

        numbers = [int(num) for num in user_input.split()]

        exclude_option = input("Do you want to exclude negative numbers? (yes or no): ").strip().lower()

        if exclude_option == 'yes':
            result = sum_of_elements(numbers, exclude_negative=True)
            print(f"The sum of positive numbers is: {result}")
        elif exclude_option == 'no':
            result = sum_of_elements(numbers, exclude_negative=False)
            print(f"The sum of all numbers is: {result}")
        else:
            print("Invalid input. Please enter 'yes' or 'no' to exclude or include negative numbers.")