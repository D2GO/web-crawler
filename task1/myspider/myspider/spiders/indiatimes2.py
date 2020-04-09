# -*- coding: utf-8 -*-
import scrapy
import re


class Indiatimes2Spider(scrapy.Spider):
    name = 'indiatimes2'
    allowed_domains = ['timesofindia.indiatimes.com']
    urls = ['https://timesofindia.indiatimes.com/entertainment/top-rated-movies/best-movies-of-all-time']
    label1 = ['tamil', 'telugu', 'malayalam', 'kannada', 'marathi', 'bengali', 'hindi', 'english', 'punjabi', 'bhojpuri', 'gujarati']
    label2 = [['hindi/bollywood','bollywood'], ['english/hollywood','hollywood'], ['tamil/kollywood','tamil'], ['telugu/tollywood','telugu'], ['malayalam/mollywood','malayalam'],['kannada','kannada'], ['marathi','marathi'],['bengali','bengali']]
    years1 = [str(i) for i in range(2006,2021)]
    years2 = [str(i) for i in range(2017,2021)]
    for i in label1:
        for j in years1:
            urls.append('https://timesofindia.indiatimes.com/entertainment/top-rated-movies/'+i+'/best-movies/'+j+'/2742916')
    for i in label2:
        for j in years2:
            urls.append('https://timesofindia.indiatimes.com/entertainment/'+i[0]+'/tollywood/top-20-best-'+i[1]+'-movies-of-'+j)
    start_urls = urls

    def parse(self, response):
        item_key, url_id = get_item_key(response.url)
        item = {item_key:[]}
        if url_id == 0:
            divs = response.xpath('//div[@class="mr_lft_box"]')
            for i in divs:
                item_i = {}
                rank = i.xpath('@data-index').extract_first()
                item_i['rank'] = rank
                name = i.xpath('div[@class="FIL_right"]/h3/a/text()').extract_first()
                item_i['name'] = name
                film_time = i.xpath('div[@class="FIL_right"]/h4/text()').extract()
                item_i['time'] = film_time[0]
                duration = i.xpath('div[@class="FIL_right"]/h4/text()').extract()
                item_i['duration'] = film_time[-1]
                label = i.xpath('div[@class="FIL_right"]/small/text()').extract()
                item_i['label'] = label
                '''
                ratings = i.xpath()
                item_i['ratings'] = ratings
                '''
                synopsls = i.xpath('div[@class="FIL_right"]/div/p').extract() #不好拿
                item_i['synopsls'] = label
            item[item_key].append(remove_null(item_i))
        elif url_id == 1:
            divs = response.xpath('//div[@class="mr_lft_box"]')
            for i in divs:
                item_i = {}
                rank = i.xpath('@data-index').extract_first()
                item_i['rank'] = rank
                name = i.xpath('div[@class="FIL_right"]/h3/a/text()').extract_first()
                item_i['name'] = name
                actors = i.xpath('div[@class="FIL_right"]/div/p/a/text()').extract_first()
                item_i['actors'] = actors
                film_time = i.xpath('div[@class="FIL_right"]/h4/text()').extract()
                item_i['time'] = film_time[0]
                duration = i.xpath('div[@class="FIL_right"]/h4/text()').extract()
                item_i['duration'] = film_time[-1]
                label = i.xpath('div[@class="FIL_right"]/small/text()').extract()
                item_i['label'] = label
                '''
                ratings = i.xpath()
                item_i['ratings'] = ratings
                '''
                synopsls = i.xpath('div[@class="FIL_right"]/div/p').extract() #不好拿
                item_i['synopsls'] = label
            item[item_key].append(remove_null(item_i))
        elif url_id == 2:
            divs = response.xpath('//div[@class="topten_movie_block clearfix"]')
            for i in divs:
                item_i = {}
                rank = i.xpath('//div[@class="number_block"/text()]')
                item_i['actor'] = rank
                name = i.xpath('a/div[@class="topten_movies_content"/h2/text()]')
                item_i['name'] = name
                ratings = i.xpath('a/div[@class="topten_movies_content"/div/span[2]/span/text()]')
                item_i['ratings'] = ratings
                content = i.xpath('a/div[@class="topten_movies_content"/h3/text()]')
                item_i['actor'] = content[0]
                item_i['synopsls'] = content[1]
            item[item_key].append(remove_null(item_i))
        yield item

    def get_item_key(url):
        if 'best-movies-of-all-time' in url:
            return 'best_movies_of_all_time', 0
        elif 'best-movies' in url:
            key_word = re.search(r'/([^/]*)/best-movies/.{4}', url).group()[1:].replace('/':'_','-':'_')
            return key_word, 1
        else:
            key_word = url.split('/')[-1].replace('-','_')
            return key_word, 2

    def remove_null(l):
        fl = filter(lambda x : x!=None, l)
        return list(fl)