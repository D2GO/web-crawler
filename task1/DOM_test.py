import requests
import scrapy


response = requests.get('https://timesofindia.indiatimes.com/entertainment/latest-new-movies/hindi-movies?curpg=1')

if response.status_code == 200:
    selector = scrapy.Selector(text=response.text)
    print(selector.xpath('//*[@id="perpetualListingInitial"]/div[3]/div[2]/div/div[1]/span[1]/text()').extract())
    print(selector.xpath('//*[@id="perpetualListingInitial"]/div[3]/div[2]/div/div[1]/span[3]/text()').extract())
    print(selector.xpath('//*[@id="perpetualListingInitial"]/div[3]/div[2]/div/div[2]/span[1]/text()').extract())
    print(selector.xpath('//*[@id="perpetualListingInitial"]/div[3]/div[2]/div/div[2]/span[3]/text()').extract())
    print(selector.xpath('//*[@id="perpetualListingInitial"]/div[3]/div[2]/div/div[2]').extract())
    movie = selector.xpath('//div[@class="mr_lft_box"]')
    i = movie[10]
    res = i.xpath('div[@class="FIL_right"]/div').extract()
    print(res)

    res = i.xpath('div[@class="FIL_right"]/div/h4/text()').extract()
    print(res)


