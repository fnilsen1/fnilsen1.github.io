from collections import Counter

# Open and read the file
with open('Python Projects\moveDistribution\move.txt', 'r') as file:
    content = file.read()

# Split the content by spaces
moves = content.split()

# Count each unique move
move_count = Counter(moves)

# Print the results
for move, count in move_count.items():
    print(f"{move}: {count}")