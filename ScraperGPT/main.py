from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from simp_html import remove_scripts_and_css
import time
import os
import re


def get_valid_filename(s):
    # Remove invalid characters from a string to create a valid filename
    return re.sub(r'[\/:*?"<>|]', '', s)
# URL you want to retrieve HTML from
url = "https://www.leboncoin.fr/recherche?text=ordinateur%208go"

chrome_options = Options()

#chrome_options.add_argument(f'user-agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"')

chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--window-size=1920x1080")

# Setting up the Chrome WebDriver using WebDriver Manager
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

# Opening the URL
driver.get(url)

title = driver.title.strip()
filename = get_valid_filename(title) + ".html"

# Retrieving the HTML content without scripts and CSS
html_content = remove_scripts_and_css(driver.page_source)


# Saving the retrieved HTML content to a file with the title as the filename
file_path = os.path.join("html_files", filename)  # Assuming a folder named "html_files"
os.makedirs(os.path.dirname(file_path), exist_ok=True)
with open(file_path, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"HTML content saved to {file_path}")

# Getting the page source (HTML) of the loaded page

#print(html_content)


# Closing the WebDriver
while True : 
    time.sleep(0.5)
# Printing the retrieved HTML content
driver.quit()

