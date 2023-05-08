# settings.py

# Important names for the spider
BOT_NAME = 'the_holy_spider'

SPIDER_MODULES = ['holySpider.holy_spider_scraper']
NEWSPIDER_MODULE = 'holySpider.holy_spider_scraper'

# Set the user agent to identify as a web browser
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

# Add a 5-second delay between requests
DOWNLOAD_DELAY = 5
