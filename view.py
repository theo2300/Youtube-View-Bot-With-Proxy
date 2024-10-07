import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

def load_proxies(path):  # Load proxies from file
    with open(path, 'r') as file:
        return [proxy.strip() for proxy in file.readlines() if proxy.strip()]

def create_driver(proxy):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Optional: Remove if you want to see the browser window
    chrome_options.add_argument(f'--proxy-server=http://{proxy}')
    
    # Initialize webdriver - make sure ChromeDriver is installed and in PATH
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def load_session(url, proxy):  # Open YouTube URL with proxy
    try:
        driver = create_driver(proxy)
        driver.get(url)
        time.sleep(5)  # Let the page load for 5 seconds
        driver.quit()
    except Exception as e:
        print(f"Error with proxy {proxy}: {e}")

if __name__ == "__main__":
    # Input from user
    youtube_url = input("Enter YouTube URL: ")
    refresh_rate = float(input("Enter refresh rate (seconds): "))
    view_count = int(input("Enter number of views: "))
    
    # Load proxies
    proxies = load_proxies('proxy.txt')
    
    # Ensure we have enough proxies
    if len(proxies) == 0:
        print("No proxies found in 'proxy.txt'. Please add some proxies.")
        exit(1)
    
    print("Working...")
    
    counter = 0
    while counter < view_count:
        proxy = random.choice(proxies)  # Pick a random proxy
        print(f"Using proxy: {proxy}")
        load_session(youtube_url, proxy)
        counter += 1
        time.sleep(refresh_rate)
    
    print(f"Completed {view_count} views.")
