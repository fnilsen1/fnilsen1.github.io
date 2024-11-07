import requests
import sys
from bs4 import BeautifulSoup

# URL for ordet "sjokolade"
url = f"https://naob.no/ordbok/{sys.argv[1]}"

# Send en GET-forespørsel til siden
response = requests.get(url)
if response.status_code == 200:
    # Parse HTML-innholdet
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Finn seksjonen med klassen 'betydning'
    betydning_sections = soup.find_all('div', class_='betydning')

    if betydning_sections:
        print("Betydning")
        for section in betydning_sections:
            # Finn den nested div-en som inneholder teksten
            inline_eske = section.find('div', class_='inline-eske')
            if inline_eske:
                print(inline_eske.get_text(strip=True))
    else:
        print("Fant ikke 'betydning og bruk'-seksjonen.")
else:
    print(f"Feil ved henting av siden, statuskode: {response.status_code}")
