from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from socrata.items import SocrataItem


class OpendataSpider(CrawlSpider):
    '''
    Spider to crawl OpenData
    '''
    name = "opendata_crawl"
    allowed_domains = ["opendata.socrata.com"]
    start_urls = ['http://opendata.socrata.com/']
    rules = [Rule(LinkExtractor(allow='browse\?&page=\d+'),
                  callback='parse_item', follow=True)]

    def parse_item(self, response):
        titles = Selector(response).xpath('//div[@class="browse2-result"]')
        for title in titles:
            item = SocrataItem()
            item["text"] = title.xpath('.//h2[@class="browse2-result-name"]/a/span/text()').extract()[0]
            item["url"] = title.xpath('.//h2[@class="browse2-result-name"]/a/@href').extract()[0]
            item["views"] = title.xpath('.//div[@class="browse2-result-view-count-value"]/text()').extract()[0].strip()
            yield item