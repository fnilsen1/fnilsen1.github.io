import requests
import sys
from bs4 import BeautifulSoup

def get_meaning(word):
    # Construct URL for the specified word
    url = f"https://naob.no/ordbok/{word}"
    
    # Send a GET request to the page
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all sections with the class 'betydning'
        betydning_sections = soup.find_all('div', class_='betydning')

        if betydning_sections:
            print(f"Betydninger for '{word}':")
            for i, section in enumerate(betydning_sections, start=1):
                # Extract and print the main meaning description
                description = section.find('div', class_='betydningsskiller inline-eske')
                if description:
                    print(f"\nBetydning {i}: {description.get_text(strip=True)}")
                
                # Extract and print all inline-eske content within the section
                details = [div.get_text(strip=True) for div in section.find_all('div', class_='inline-eske')]
                for detail in details:
                    print(f"  - {detail}")
        else:
            print(f"Fant ikke 'betydning og bruk'-seksjonen for '{word}'.")
    else:
        print(f"Feil ved henting av siden, statuskode: {response.status_code}")

# Ensure the user provides an input argument
if len(sys.argv) > 1:
    word = sys.argv[1]
    get_meaning(word)
else:
    print("Vennligst oppgi et ord som argument når du kjører skriptet.")
