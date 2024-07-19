#basic_web_scraper
import requests
from bs4 import Beatifulsoup

def basic_web_scraper(url):
    #send a Get request was successful (status code 200)
    response = requests.get(url)

     # check if the request was successful (status code 200)
    if response.status_code == 200:
        #parse the HTML content
        soup = Beatifulsoup(response.content,'html.parser')

        #example: Extract all the links from the page
        links = soup.find_all('a')

        #print all the links
        for link in links:
            print(link.get("href"))
        else:
            print(f"Failed to retrieve content,status code {response.status_code}")


if __name__ == "__main__":
    #URL of the webpage to scrape 
    url = input("Enter thev url:")
basic_web_scraper(url)
