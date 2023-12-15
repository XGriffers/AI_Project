import scrapy
from scrapy.spuders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'BlogSpider'
    #allowed_domains = ['domain.com']
    start_urls = ['http://bit.ly/3GOY3RG']

    rules = (
        Rule(LinkExtractor(allow=('/page/')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # Scrape data from page
        title = response.xpath('//h1/text()').extract()[0]
        content = response.xpath('//p/text()').extract()[0]

        yield {'title': title, 'content': content}

        pass