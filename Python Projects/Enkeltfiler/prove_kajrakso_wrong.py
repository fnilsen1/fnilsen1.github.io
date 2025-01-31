start_key = 1
end_key = 11880

# Create the dictionary
number_dict = {key: key - 1 for key in range(start_key, end_key + 1)}

# Define the output file name
output_file = "number_dictionary.txt"

# Save the dictionary to a text file
with open(output_file, "w") as file:
    for key, value in number_dict.items():
        file.write(f"{key}: {value}\n")

print(f"Dictionary saved to {output_file}")
