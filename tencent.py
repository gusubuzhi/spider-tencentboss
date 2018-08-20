# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from TencenSpider.items import TencenspiderItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        for node in node_list:
            item = TencenspiderItem()
            item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0]

            item['positionLink'] = node.xpath("./td[1]/a/@href").extract()[0]

            if len(node.xpath("./td[2]/text()")):
                item['positionType'] = node.xpath("./td[2]/text()").extract()[0]
            else:
                item['positionType'] = ''

            item['peopleNumber'] = node.xpath("./td[3]/text()").extract()[0]

            item['workLocation'] = node.xpath("./td[4]/text()").extract()[0]

            item['publishTime'] = node.xpath("./td[5]/text()").extract()[0]

            yield item













        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
