import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random

def load_proxies(PATH):  # Load proxies from a file
    with open(PATH, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def create_driver(proxy):  # Create a WebDriver instance with proxy settings
    chrome_options = Options()
    chrome_options.add_argument(f'--proxy-server={proxy}')
    
    service = Service('path/to/chromedriver')  # Update the path to your chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver

inpt = input("Enter YouTube URL: ")
inpt2 = float(input("Enter refresh rate (seconds): "))
inp4 = int(input("Enter number of views: "))

print("Working...")
print('<<<<<<<<<<<<<<<<<<<<<<<<<THE VIEW BOT>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('--------------------------------------------------------------')
print('||||||||||||||||||||||||||BY @yashu1wwww ||||||||||||||||||||||||||||')
print('--------------------------------------------------------------')
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

proxies = load_proxies('path/to/proxies.txt')  # Update this path to your proxies file
counter = 0

while counter < inp4:
    proxy = random.choice(proxies)  # Choose a random proxy
    driver = create_driver(proxy)  # Create a new WebDriver instance with the selected proxy
    
    try:
        driver.get(inpt)  # Open the YouTube URL
        time.sleep(inpt2)  # Wait for the specified refresh rate
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()  # Close the WebDriver
        counter += 1  # Increment the view counter
