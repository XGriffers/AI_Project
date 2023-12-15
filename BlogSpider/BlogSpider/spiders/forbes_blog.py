import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class forbesBlogSpider(CrawlSpider):
    name = "forbesSpider"
    start_urls = ['https://www.forbes.com/advisor/business/start-a-blog/']
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        filename = 'forbes.html'
        with open(filename, 'wb') as f:
            title = response.xpath('//title/text()').get()
            content = response.xpath('//*/p/text()').getall()
            f.write(title.encode())
            for paragraph in content:
                f.write(paragraph.encode())

        def parse_item(self, response):
            item = BlogspiderItem()
            item['title'] = response.xpath('//title/text()').get()
            item['content'] = response.xpath('//*/p/text()').get()
            yield item
