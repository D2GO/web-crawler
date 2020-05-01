# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy
import re

from myspider.items import MovieItem


class IndiatimesSpider(scrapy.Spider):
    name = 'indiatimes'
    allowed_domains = ['indiatimes.com']

    start_urls = [
        'https://timesofindia.indiatimes.com/etgenrelist.cms?genereview=latest&genere=&curpg=1'
    ]

    def parse(self, response):
        divs = response.xpath('//div[@class="mr_lft_box"]')

        if len(divs) >= 50:
            curpg = re.search(r'curpg=(\d+)', response.url).group(1)
            nextpg = int(curpg) + 1
            next_url = response.url.replace('curpg={}'.format(curpg), 'curpg={}'.format(nextpg))

            yield scrapy.Request(next_url, callback=self.parse)

        for div in divs:
            detail_url = urljoin(response.url, div.xpath('div[@class="FIL_left"]/a/@href').extract_first())
            yield scrapy.Request(detail_url, callback=self.parse_detail)

    def parse_detail(self, response):

        movie_item = MovieItem(url=response.url)

        movie_item['id'] = response.xpath(
            '//div[@data-plugin="moviereview"]/@movieshowid').extract_first()

        movie_item['name'] = response.xpath(
            '//div[contains(@class,"md_topband")]/h1/text()').extract_first()

        md_infos = response.xpath('//div[@class="md_info"]')
        infos = [info.xpath('string()').extract_first().strip() for info in md_infos]

        movie_item['release_date'] = infos[0]
        movie_item['language'] = infos[1]
        if len(infos) >= 4:
            movie_item['duration'] = infos[2]
            movie_item['genres'] = infos[3]
        else:
            is_duration = bool(re.search(r'\d+ hr[s]* \d+ min[s]*', infos[2]))
            movie_item['duration' if is_duration else 'genres'] = infos[2]

        movie_item['user_rating'] = response.xpath(
            '//div[@data-plugin="avgrating"]//span[@class="rate_count"]/text()').extract_first()

        movie_item['critic_rating'] = response.xpath(
            '//div[@data-plugin="criticrating"]//span[@class="cricrating"]/text()').extract_first()

        movie_item['description'] = response.xpath(
            '//input[@data-plugin="metadescription"]/@value').extract_first()

        movie_item['cover'] = response.xpath(
            '//div[@class="movie_poster"]//img/@src').extract_first()

        yield movie_item
