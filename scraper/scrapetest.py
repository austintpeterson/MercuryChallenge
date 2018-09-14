import cfscrape

scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
# Or: scraper = cfscrape.CloudflareScraper()  # CloudflareScraper inherits from requests.Session
stuff = scraper.get("http://github.com/Anorov/cloudflare-scrape").content  # => "<!DOCTYPE html><html><head>..."
print(stuff)
