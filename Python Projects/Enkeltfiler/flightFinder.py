

from google_flight_analysis.scrape import *
result = Scrape('JFK', 'IST', '2023-08-20')
ScrapeObjects(result)
print(result.data) 