import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from w3lib.html import remove_tags

# scrapy crawl theholyspider -o output.json

class TheholyspiderSpider(CrawlSpider):
    name = "theholyspider"
    allowed_domains = ["sacred-texts.com"]
    start_urls = ["https://www.sacred-texts.com/lgbt/index.htm"]
    deny_patterns = [r'cdshop', r'contact\.htm', r'search\.htm', r'faq\.htm', r'about\.htm', r'rtos\.htm', r'cnote\.htm']
    
    rules = (
        # Follow all links except those that contain the deny_patterns
        Rule(LinkExtractor(deny=deny_patterns), callback="parse_item", follow=True),
    )
    
    custom_settings = {
        'DEPTH_LIMIT': 10,  # Set maximum depth to 10
    }
    
    
    def parse_item(self, response):
        # Extract all text from the page
        body_text = response.xpath('//body//text()').getall()
        
        # Join all text into a single string
        all_text = ''.join(body_text)
        
        # Remove HTML tags from the filtered text
        clean_text = remove_tags(all_text)

        # Remove unwanted patterns from the text
        pattern = r'(This is a quiet place in cyberspace|devoted to religious tolerance and scholarship|Non-public domain contents of this site|not otherwise copyrighted are © copyright)'
        filtered_text = re.sub(pattern, '', clean_text)
        filtered_text = '\n'.join(line for line in filtered_text.split('\n') if 'CD-ROM' not in line)
        
        unique_text = ' '.join(list(set(filtered_text.split())))

        # Yield the extracted data in a dictionary format
        yield {
            'text': unique_text.strip(),
            'url': response.url,
        }
