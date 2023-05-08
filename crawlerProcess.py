'''
 __      / _ \      __ 
/_/\/\ \_\(_)/_/ /\/\_\
\_\  /  _//"\\_  \  /_/
/_/  \   /   \   /  \ \
\_\/\ \         / /\/_/
   \_\/         \/_/   
    The Holy Spider
    
by: huh? with some help from the Scrapy docs and Copilot and GPT-3.5 (Thanks!)
ASCII Art by: https://www.asciiart.eu/animals/spiders and https://www.asciiart.eu/religion/crosses-and-crucifixes (Thanks again!)
Version: 0.0.2 (That works!)
Change log:
    - Using datetime and timedelta to set the duration of the crawl cause last one didn't work to stop it.
    
This is the crawler process which runs the spider and exports the data to a CSV file.
Just change the time.sleep() value to change the duration of the crawl. 
'''
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from theHolySpider import TheHolySpider

# Create a CrawlerProcess object
process = CrawlerProcess(settings=get_project_settings())
process.crawl(TheHolySpider)
process.start()
