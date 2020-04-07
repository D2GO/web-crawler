# -*- coding: utf-8 -*-
import scrapy as sp
import requests as rs


class IndiatimesSpider(sp.Spider):
    name = 'indiatimes'
    allowed_domains = ['timesofindia.indiatimes.com']
    language = ['hindi','english','tamil','malayalam','kannada','bengali','punjabi','marathi','bhojpuri','gujarati']
    start_urls = ['https://timesofindia.indiatimes.com/entertainment/latest-new-movies/'+i+'-movies' for i in language]
    page = 2


    def parse(self, response):
        divs = response.xpath('//div[@class="mr_lft_box"]')
        for i in divs:
            item = {}            
            name = i.xpath('div[@class="FIL_right"]/a/h3/text()').extract_first()
            item[name] = {}
            actors = i.xpath('div[@class="FIL_right"]/div/p/a/text()').extract()
            item[name]['actors'] = actors
            ''' 分数拿不到 好像是js生成的
            ratings = i.xpath()
            item[name]['ratings'] = ratings
            '''
            tips = i.xpath('div[@class="FIL_right"]/div/div/small/text()').extract()
            item[name]['language'] = tips[0]
            item[name]['label'] = tips[1]
            film_time = i.xpath('div[@class="FIL_right"]/div/h4/text()').extract()
            item[name]['time'] = film_time[0].strip()
            yield item
        next_url = self.start_urls[0] + '?curpg=' + str(self.page)
        if self.page_judge(next_url):
        	self.page += 1
        	yield sp.Request(
        		next_url,
        		callback=self.parse
        	)


    def page_judge(self, url):
    	response = rs.get(url)
    	selector = sp.Selector(text=response.text)
    	jud = selector.xpath('//*[@id="perpetualListingInitial"]//div[@class="mr_lft_box"]').extract_first()
    	return True if jud != None else False


