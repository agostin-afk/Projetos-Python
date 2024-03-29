import scrapy
# estrutura base
"""class QuotsSpider(scrapy.Spider):
    name = ''
    start_url = []

    def parse(self, response):
        pass"""

class QuotsSpider(scrapy.Spider):
    name = 'QuotsSpider'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        qoute = response.xpath('*//div[@class="qoute"]')
        for q in qoute:
            yield{
                'title' : q.xpath('.//span[@class = "text"]/text()').get(),
                'author' : q.xpath('.//small[@class = "author"]/text()').get(),
                'tags' : q.xpath('.//div[@class = "tags"]/a[@class = "tag"]/text()').getall()   
            }