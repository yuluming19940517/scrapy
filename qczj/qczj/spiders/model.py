import scrapy


class ModelSpider(scrapy.Spider):
    name = 'model'
    allowed_domains = ['autohome.com']
    start_urls = ['http://autohome.com/']

    def parse(self, response):
        pass
