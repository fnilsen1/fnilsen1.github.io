import subprocess
import json

# Load the scrambles dictionary from a JSON file
with open("zblls.json", "r") as f:
    scrambles_dict = json.load(f)

# Dictionary to store solutions
solutions_dict = {}

# Track total number of scrambles
total_scrambles = sum(len(scrambles) for scrambles in scrambles_dict.values())
processed_count = 0

# Iterate through the groups and scrambles
for group, scrambles in scrambles_dict.items():
    solutions_dict[group] = {}  # Create sub-dictionary for group
    
    for index, scramble in scrambles.items():
        try:
            # Run the command and capture output
            result = subprocess.run(
                ["nissy", "solve", "-n", "50", "-m", "12", "-p", scramble],
                capture_output=True,
                text=True,
                check=True
            )
            # Store the output as a list of solutions
            solutions_dict[group][index] = result.stdout.strip().split("\n")
        except subprocess.CalledProcessError as e:
            print(f"Error solving for {group} index {index}: {e}")

        # Update progress
        processed_count += 1
        print(f"Processed {processed_count}/{total_scrambles} scrambles...")

# Save the solutions to a new JSON file
output_file = "zbll_solutions.json"
with open(output_file, "w") as f:
    json.dump(solutions_dict, f, indent=4)

print(f"Solutions saved to {output_file}")
