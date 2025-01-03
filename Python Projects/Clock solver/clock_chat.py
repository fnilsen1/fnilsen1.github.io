import numpy as np

def find_combination(lists, modulo=12):
    num_lists = len(lists)
    array_length = len(lists[0][0])  # Lengden på hver array (14)
    target = [0] * array_length  # Målet vi prøver å oppnå
    
    # Backtracking-funksjon
    def backtrack(idx, current_sum, used_elements):
        current_sum = [x % modulo for x in current_sum]  # Ta modulo 12
        
        # Hvis vi har valgt 6 elementer og summen er riktig
        if len(used_elements) == 6:
            if current_sum == target:
                return used_elements
            return None

        # Hvis vi har gått gjennom alle lister
        if idx >= num_lists:
            return None

        # Utforsk alle elementene i den nåværende listen
        for element in lists[idx]:
            new_sum = [(cs + e) % modulo for cs, e in zip(current_sum, element)]
            result = backtrack(idx + 1, new_sum, used_elements + [element])
            if result:  # Hvis en løsning ble funnet
                return result

        return None

    # Start backtracking fra første liste
    return backtrack(0, [0] * array_length, [])

# Eksempeldata
np.random.seed(0)  # For reproduserbarhet
lists = [np.random.randint(0, 12, (144, 14)).tolist() for _ in range(14)]

# Kjører funksjonen
solution = find_combination(lists)

# Skrive ut løsningen
if solution:
    print("Løsning funnet:")
    for element in solution:
        print(element)
else:
    print("Ingen løsning funnet.")
