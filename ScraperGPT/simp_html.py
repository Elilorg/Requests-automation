
from bs4 import BeautifulSoup
import re

def remove_scripts_and_css1(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Remove all script tags
    for script in soup.find_all("script"):
        script.extract()
    
    # Remove all style tags (CSS)
    for style in soup.find_all("style"):
        style.extract()
    
    return str(soup)

def remove_scripts_and_css(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Remove all script tags and script links
    for script in soup.find_all(["script", "link"], {"src": re.compile(".js$")}):
        script.extract()
    
    for script in soup.find_all("script"):
        script.extract()
        
    # Remove all style tags (CSS)
    for style in soup.find_all("style"):
        style.extract()
    
    # Remove all meta tags
    for meta in soup.find_all("meta"):
        meta.extract()
    
    return soup.prettify()