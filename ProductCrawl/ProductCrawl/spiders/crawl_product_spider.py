import scrapy


class QuotesSpider(scrapy.Spider):
    name = "crawlproduct"
    start_urls = [
        'https://duckduckgo.com/',
    ]

    def parse(self, response):
        pass
