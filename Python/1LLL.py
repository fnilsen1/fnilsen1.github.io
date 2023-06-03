def find_largest_space(filename):
    with open(filename, 'r') as file:
        content = file.read()

    largest_space = 0
    largest_quote_indices = None

    start_index = 0
    while True:
        start_quote_index = content.find('"', start_index)
        if start_quote_index == -1:
            break

        end_quote_index = content.find('"', start_quote_index + 1)
        if end_quote_index == -1:
            break

        space_length = end_quote_index - start_quote_index - 1
        if space_length > largest_space:
            largest_space = space_length
            largest_quote_indices = (start_quote_index, end_quote_index)

        start_index = end_quote_index + 1

    if largest_quote_indices is None:
        return "No consecutive quotation marks found."

    start, end = largest_quote_indices
    largest_space_text = content[start+1:end]

    return largest_space_text


# Usage example
filename = r'Python\algs.txt'  # Replace with your file name
largest_space_text = find_largest_space(filename)
print("Largest space between consecutive quotation marks:")
print(largest_space_text)