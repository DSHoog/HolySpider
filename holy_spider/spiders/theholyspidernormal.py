import scrapy

# scrapy crawl test -o output.json

class MySpider(scrapy.Spider):
    name = "normalspider"
    allowed_domains = ["sacred-texts.com"]
    start_urls = ["https://www.sacred-texts.com/lgbt/index.htm#intro"]

    def parse(self, response):
        raw_text = response.text
        # Extract the page title using an XPath selector
        center_elements = response.selector.xpath('//center')
        text_content = ' '.join(center_elements.xpath('.//text()').getall())

        # Remove unwanted patterns from the text
        pattern = r'(This is a quiet place in cyberspace|devoted to religious tolerance and scholarship|Non-public domain contents of this site|not otherwise copyrighted are © copyright|\sTopics\s+Home\s+Catalog\s+African\s+Age\s+of\s+Reason\s+Alchemy\s+Americana\s+Ancient\s+Near\s+East\s+Astrology\s+Asia\s+Atlantis\s+Australia\s+Basque\s+Baha\'i\s+Bible\s+Book\s+of\s+Shadows\s+Buddhism\s+Celtic\s+Christianity\s+Classics\s+Comparative\s+Confucianism\s+DNA\s+Earth\s+Mysteries\s+Egyptian\s+England\s+Esoteric\/Occult\s+Evil\s+Fortean\s+Freemasonry\s+Gothic\s+Gnosticism\s+Grimoires\s+Hinduism\s+I\s+Ching\s+Islam\s+Icelandic\s+Jainism\s+Journals\s+Judaism\s+Legends\/Sagas\s+Legendary\s+Creatures\s+LGBT\s+Miscellaneous\s+Mormonism\s+Mysticism\s+Native\s+American\s+Necronomicon\s+New\s+Thought\s+Neopaganism\/Wicca\s+Nostradamus\s+Oahspe\s+Pacific\s+Paleolithic\s+Parapsychology\s+Philosophy\s+Piri\s+Re\'is\s+Map\s+Prophecy\s+Roma\s+Sacred\s+Books\s+of\s+the\s+East\s+Sacred\s+Sexuality\s+Shakespeare\s+Shamanism\s+Shinto\s+Symbolism\s+Sikhism\s+Sub\s+Rosa\s+Swedenborg\s+Tantra\s+Taoism\s+Tarot\s+Thelema\s+Theosophy\s+Time\s+Tolkien\s+UFOs\s+Utopia\s+Women\s+Wisdom\s+of\s+the\s+East\s+Zoroastrianism)'
        filtered_text = re.sub(pattern, '', text_content)

        # Remove all newlines
        filtered_text = filtered_text.replace('\n', ' ')

        # Yield the extracted data in a dictionary format
        yield {
            'text': filtered_text.strip(),
            'url': response.url,
        }


