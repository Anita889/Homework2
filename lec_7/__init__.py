def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of '{file_name}':\n{content}")
            return content
    except FileNotFoundError:
        print(f"File '{file_name}' doesn't exist. Please enter a valid filename.")
        return None

def write_to_file(file_name, content):
    while True:
        write_option = input("Do you want to write to this file? (yes/no): ").lower()
        if write_option == "yes":
            try:
                with open(file_name, 'w') as file:
                    file.write(content)
                    print(f"Content has been written to '{file_name}' successfully.")
                    break
            except Exception as e:
                print(f"Error writing to file: {e}")
                file_name = input("Please provide a valid filename to write: ")
        elif write_option == "no":
            new_file_name = input("Enter the new file name to write: ")
            new_content = input("Enter the content to write: ")
            try:
                with open(new_file_name, 'w') as file:
                    file.write(new_content)
                    print(f"Content has been written to '{new_file_name}' successfully.")
                    break
            except FileNotFoundError:
                print(f"File '{new_file_name}' cannot be created. Please enter a valid filename.")
            except Exception as e:
                print(f"Error writing to file: {e}")
                continue


if __name__ == "__main__":

    file_name = input("Enter the name of the text file you want to open: ")

    while True:
        try:
            file_content = read_file(file_name)
            if file_content is not None:
                write_to_file(file_name, file_content)
            break
        except ValueError:
            print("Please enter a valid filename.")
            file_name = input("Enter the name of the text file you want to open: ")