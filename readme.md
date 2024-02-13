# Simple script to scrape Yelp urls
This script will run when a url is presented in this format

```python
#A url needs to be given upon creation of scraper_bot
bot = scraper_bot(f"https://www.yelp.com/search?find_desc=&find_loc={city}%2C+{state_abbreviation}+{Zip-code}")
bot.scrape_urls()


unfiltered = scrapy.url_list
data = [url for url in unfiltered if not url.startswith("https://www.yelp.com/adredir")]    #Removes sponsored pages from urls
```

Data will hold a list of URLS which can then be processed for further scraping

```python
# Write the URLs to the CSV file
with open(csv_file_path, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    for url in data:
        writer.writerow([url])
```













