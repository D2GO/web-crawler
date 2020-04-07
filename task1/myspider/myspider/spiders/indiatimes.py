# -*- coding: utf-8 -*-
import scrapy

class IndiatimesSpider(scrapy.Spider):
    name = 'indiatimes'
    allowed_domains = ['timesofindia.indiatimes.com']
    start_urls = ['https://timesofindia.indiatimes.com/entertainment/latest-new-movies/hindi-movies']

    def parse(self, response):
        divs = response.xpath('//*[@id="perpetualListingInitial"]//div[@class="mr_lft_box"]')
        res = []
        for i in divs:
            div = {}            
            name = i.xpath('div[@class="FIL_right"]/a/h3/text()').extract_first()
            div[name] = {}
            actors = i.xpath('div[@class="FIL_right"]/div/p/a/text()').extract()
            div[name]['actors'] = actors
            res.append(div)
        print(res)




