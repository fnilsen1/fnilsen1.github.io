import numpy as np
import time

# Parametere
array_size = 14       # Størrelsen på arrayen
num_iterations = 1000000  # Antall iterasjoner

# Initialiser en array med nuller
array = np.zeros(array_size, dtype=int)

# Start timing
start_time = time.time()

# Loop for å legge til 1 til hvert element
for _ in range(num_iterations):
    array += 1

# Slutt timing
end_time = time.time()

# Utskrift av tid brukt
print(f"Tiden brukt: {end_time - start_time:.6f} sekunder")

# Utskrift av arrayens verdier
print("Arrayens verdier:")
print(array)
