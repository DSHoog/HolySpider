'''
 __      / _ \      __ 
/_/\/\ \_\(_)/_/ /\/\_\
\_\  /  _//"\\_  \  /_/
/_/  \   /   \   /  \ \
\_\/\ \         / /\/_/
   \_\/         \/_/   
    The Holy Spider
by: huh? with some help from the Scrapy docs and Copilot and GPT-3.5 (Thanks!)
ASCII Art by: https://www.asciiart.eu/animals/spiders and https://www.asciiart.eu/religion/crosses--and-crucifixes (Thanks again!)
Version: 0.0.2 (That works!)
Change log:
    - Using CrawlSpider and Rules to crawl the website instead of the other method (See last version)
    - Added in-depth comments on every line: The optimized code now has detailed comments for each line, 
      providing more context and explanation for each part of the code.
    - No changes in functionality: The actual functionality of the code has not been altered. 
      The primary difference between the two versions is the addition of the in-depth comments.

This is the main spider file for the Holy Spider project. It contains the code for scraping the text from the
Sacred Texts website and exporting it to a CSV file.

Just change the url in the start_urls list to change the website that the spider crawls.
'''

# Import the required libraries
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.exporters import CsvItemExporter
from scrapy.linkextractors import LinkExtractor

# Define the TheHolySpider class, which inherits from the CrawlSpider class
class TheHolySpider(CrawlSpider):
    # Set the name of the spider
    name = 'the_holy_spider'
    
    # Set the allowed domains for the spider to crawl
    allowed_domains = ['sacred-texts.com']
    
    # Set the URL to start scraping from
    start_urls = ['https://www.sacred-texts.com/']
    
    # Set the custom settings for the spider, including the feed format and filename
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'holytexts.csv'
    }
    
    # Define the rules for the spider, including a single Rule object
    # to follow links and parse items from the website
    rules = (
        Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),
    )

    # Constructor function for initializing the spider
    def __init__(self, *args, **kwargs):
        # Call the parent constructor
        super(TheHolySpider, self).__init__(*args, **kwargs)
        
        # Create an empty list to hold the scraped items
        self.items = []
        
        # Create a CsvItemExporter instance for exporting data to a CSV file
        self.exporter = CsvItemExporter(open('holytexts.csv', 'wb'))
        
        # Start exporting data to the CSV file
        self.exporter.start_exporting()

    # Function for parsing the HTML response and extracting the text
    def parse_item(self, response):
        # Create a dictionary to hold the URL and cleaned text
        item = {
            'url': response.url,  # Save the URL of the page
            'text': self.clean_text(response.xpath('//text()').getall()),  # Clean and extract the text
        }
        
        # Return the item to the spider
        return item
    
    # Function for finalizing the spider after it has finished scraping
    def closed(self, reason):
        # Get all the scraped items
        items = self.items
        
        # Export each item to the CSV file
        for item in items:
            self.exporter.export_item(item)
        
        # Finish exporting data to the CSV file
        self.exporter.finish_exporting()

    # Function for cleaning the extracted text (now a static method)
    @staticmethod
    def clean_text(text):
        # Check if the text is not empty
        if text is not None:
            # Define a regular expression pattern to match unwanted characters
            pattern = r'<.*?>|[\r\n\t]|(window\..*;)|(\n\n+)'
            
            # Remove unwanted characters from the text using the regular expression pattern
            cleaned_text = re.sub(pattern, '', ''.join(text), flags=re.DOTALL)
            
            # Return the cleaned text as a string with leading/trailing whitespace removed
            return cleaned_text.strip()
        else:
            # Return None if there is no text to clean
            return None