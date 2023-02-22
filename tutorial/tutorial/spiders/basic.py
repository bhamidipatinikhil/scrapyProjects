import scrapy
from tutorial.items import PropertiesItem


class BasicSpider(scrapy.Spider):
    name = "basic"
    start_urls = ["https://www.goodreads.com/genres/new_releases/fantasy"]
    def parse(self, response):
        item = PropertiesItem()
        item['title'] = response.xpath('//div[contains(@class, "coverWrapper")]//img/@alt')[0].extract()
        item['coverImagePath'] = response.xpath('//div[contains(@class, "coverWrapper")]//img/@src')[0].extract()
        return item