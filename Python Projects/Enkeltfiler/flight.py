
from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.chrome.options import Options  
from selenium.common.exceptions import TimeoutException  
from selenium.webdriver.common.keys import Keys  

# Choose the two dates 
# in this format 
x = "2020-03-10"
y = "2020-03-16"

a = int(x[8:10]) 
b = int(y[8:10]) 

if a > b: 
	m = a - b 
	t = b 

else: 
	m = b - a 
	t = a 
print(t) 

low_price = "" 
url_final = 'https://paytm.com/flights'
data = {} 

for i in range(t, t + m+1): 
	url = 'https://paytm.com/flights/flightSearch/BBI-\ Bhubaneshwar/DEL-Delhi/1/0/0/E/2020-03-'+str(i) 
	
	# Locations can be changed on 
	# the above statement 
	print(url) 
	
	date = "2019-12-" + str(i) 
	
	# enables the script to run properly without 
	# opening the chrome browser. 
	chrome_options = Options() 
	chrome_options.add_argument("--disable-gpu") 
	

	chrome_options.add_argument("--headless") 
	
	driver = webdriver.Chrome(executable_path = '/path/to/chromedriver', 
							options=chrome_options) 
	
	driver.implicitly_wait(20) 
	driver.get(url) 
	
	g = driver.find_element_by_xpath("//div[@class='_2gMo']") 
	price = g.text 
	
	x = price[0] 
	y = price[2:5] 
	z = str(x)+str(y) 
	p = int(z) 
	print(p) 
	
	prices=[] 
	if p <= 2000: 
		data[date] = p 
		
for i in data: 
	low_price += str(i) + ": Rs." + str(data[i]) + "\n"
	
print(low_price) 
