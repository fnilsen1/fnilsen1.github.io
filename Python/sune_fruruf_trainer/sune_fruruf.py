import random
def read_file_to_list(file_path):
        with open(file_path, 'r') as file:
            content_list = file.readlines()
        return content_list

auf = [" U", " U'", " U2", ""]
file_path = 'sunefruruf (1).txt'
file_content_list = read_file_to_list(file_path)
while True:
    random_number = random.randint(0, len(file_content_list)-1)
    random_number_again = random.randint(0,3)
    print()
    combined = file_content_list[random_number].strip()+auf[random_number_again]
    print(combined)
    user_input = input()