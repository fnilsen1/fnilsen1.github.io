import fileinput
import sys

def remove_lines_with_string(file_path, specific_string):
    # Use fileinput to modify the file in-place
    with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
        for line in file:
            if not line.startswith(specific_string):
                sys.stdout.write(line)

    print("Lines starting with '{}' have been removed from the file.".format(specific_string))


# Example usage
file_path = r'JS\KPtxt\xKP_RULFD.txt'  # Replace with the actual path to your text file
specific_string = 'U'  # Replace with the specific string you want to remove

# remove_lines_with_string(file_path, specific_string)

def remove_lines_with_string(filename, string):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Remove lines containing the specified string
    updated_lines = [line for line in lines if string not in line.strip()]

    with open(filename, 'w') as file:
        file.writelines(updated_lines)

# Usage example
filename = r'JS\KPtxt\xKP_RULFD.txt'
string_to_remove = 'F2'

# remove_lines_with_string(filename, string_to_remove)
def remove_lines_with_condition(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Filter out lines that meet the condition
    filtered_lines = [line for line in lines if not meets_condition(line)]

    # Write the filtered lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)

def meets_condition(line):
    # Implement your condition here
    # Return True if the line meets the condition, False otherwise
    # Example: Remove lines that contain the word "example"
    if(line.strip("'")[-1] == "U"):
        return True
    else:
        return False

# Usage example
file_path = r'JS\KPtxt\KPx_RUFD.txt'  # Replace with your file path

remove_lines_with_condition(file_path)