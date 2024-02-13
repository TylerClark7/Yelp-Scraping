from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv


class scraper_bot:
    def __init__(self, url) -> None:

        self.url_list = []
        self.driver = webdriver.Chrome()
        self.numb_of_pages = 0
        self.current_page = 0
        self.star_url = url
        self.created_url = self.star_url + f"&start={self.current_page}"

    # Function to go to page
    def get_url(self):
        self.driver.get(self.created_url)
        self.driver.implicitly_wait(5)

    # function to scrape data from page
    def scrape_urls(self):

        self.get_url()
        self.get_numb_of_pages()
        print(type(self.numb_of_pages))

        for i in range(self.numb_of_pages):

            print(self.created_url)
            self.get_url()
            urls = self.driver.find_elements(By.CSS_SELECTOR, "h3 a")
            links = []
            links += [elem.get_attribute("href") for elem in urls]
            self.url_list += links

            self.current_page += 10
            self.created_url = self.star_url + f"&start={self.current_page}"

    # Get number of pages
    def get_numb_of_pages(self):
        try:
            # Attempt to find Number of pages
            parts = self.driver.find_element(By.CLASS_NAME, "css-1aq64zd")
            self.numb_of_pages = int(parts.text.split("of")[1].strip())

            return self.numb_of_pages
        except NoSuchElementException:
            # If the element is not found, return 1
            return 1

    # function to close driver, return data


scrapy = scraper_bot(
    "URL"   #Ex. https://www.yelp.com/search?find_desc=&find_loc=Citytown%2C+MN+55555
)

scrapy.scrape_urls()


unfiltered = scrapy.url_list
data = [url for url in unfiltered if not url.startswith("https://www.yelp.com/adredir")]    #Removes sponsored pages from urls
print(data)

csv_file_path = "urls.csv"

# Write the URLs to the CSV file
with open(csv_file_path, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    for url in data:
        writer.writerow([url])
