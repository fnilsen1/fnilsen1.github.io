
# # alder = input("Hva er alderen din: ")

# # def minimumalder(age):

# #     print(f"dette er minimum alderen du kan ha sex med: {int(age)/2+7}")


# # minimumalder(alder)
# # alder = int(input("hva er din alder: "))
# if(alder > 18 or alder < 16):
#     print("du er under 16")

# if(alder < 18):
#     print("du er over 18")

# else:
#     print("du er 18")

import time
import webbrowser
target_time = "16:00"  # Replace with your desired time in HH:MM format

# Wait until the target time is reached
while True:
    current_time = time.strftime("%H:%M", time.localtime())
    if current_time >= target_time:
        break

url = "https://www.worldcubeassociation.org/competitions/BergenOpen2023/register"  # Replace with the URL of the website you want to open

webbrowser.open(url)

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# option = Options()
# option.add_argument("--window-size=1920, 1080")
# driver = webdriver.Chrome(options=option)
# driver.get("https://www.worldcubeassociation.org/competitions/PleaseBeLoudinTashkent2023/register")

# # folder = driver.find_element("xpath", '//input[@name="commit"]')
# # folder.click()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Set up the WebDriver
# driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed

# # Open the link
# url = 'https://www.worldcubeassociation.org/competitions/PleaseBeLoudinTashkent2023/register'
# driver.get(url)

# # Wait for the element to be clickable
# element_xpath = '//input[@name="commit"]'
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))

# # Click on the element
# element.click()
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# # Set up the WebDriver
# driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed

# # Open the link
# url = 'https://www.worldcubeassociation.org/competitions/PleaseBeLoudinTashkent2023/register'
# driver.get(url)

# # Find the element by XPath
# element_xpath = '//input[@name="commit"]'
# element = driver.find_element(By.XPATH, element_xpath)

# # Click on the element
# element.click()
# driver.quit()






