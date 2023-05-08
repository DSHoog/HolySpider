# settings.py

# Important names for the spider
BOT_NAME = 'holy_spider'

SPIDER_MODULES = ['holy_sider.spiders']
NEWSPIDER_MODULE = 'holy_sider.spiders'

# ScraOps API Key
SCRAPEOPS_API_KEY = 'cbe2aba4-0561-45bd-9f9f-a223e227ca02'

EXTENSIONS = {
        'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
        }

# Set the user agent to identify as a web browser
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

# Add a 5-second delay between requests
DOWNLOAD_DELAY = 5
