#include <iostream>
#include <vector>
#include <chrono>  // For timing

int main() {
    const int arraySize = 10;     // Størrelsen på arrayet (velg en mindre verdi for tydelig utskrift)
    const int numIterations = 1000000; // Antall iterasjoner

    std::vector<int> array(arraySize, 0);  // Initialiser en array med `arraySize` elementer satt til 0

    // Start timing
    auto start = std::chrono::high_resolution_clock::now();

    for (int iteration = 0; iteration < numIterations; ++iteration) {
        for (int i = 0; i < arraySize; ++i) {
            array[i] += 1;  // Legg til 1 til hvert element
        }
    }

    // Slutt timing
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

    // Output resultat
    std::cout << "Tiden brukt: " << duration.count() << " millisekunder\n";

    // Skriv ut arrayen
    std::cout << "Arrayens verdier:\n";
    for (int i = 0; i < arraySize; ++i) {
        std::cout << array[i] << " ";  // Skriv ut hvert element
    }
    std::cout << std::endl;

    return 0;
}
