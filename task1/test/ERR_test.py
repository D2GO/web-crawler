import requests
import scrapy


response = requests.get('https://timesofindia.indiatimes.com/entertainment/latest-new-movies/hindi-movies')

if response.status_code == 200:
    selector = scrapy.Selector(text=response.text)
    '''
    l = [str(i) for i in range(100)]
    def test(n):
        print(selector.xpath('//*[@id="perpetualListingInitial"]/div['+n+']/div[2]/div/div[1]/span[1]/text()').extract())
        print(selector.xpath('//*[@id="perpetualListingInitial"]/div['+n+']/div[2]/div/div[1]/span[3]/text()').extract())
        print(selector.xpath('//*[@id="perpetualListingInitial"]/div['+n+']/div[2]/div/div[2]/span[1]/text()').extract())
        print(selector.xpath('//*[@id="perpetualListingInitial"]/div['+n+']/div[2]/div/div[2]/span[3]/text()').extract())
        print(selector.xpath('//*[@id="perpetualListingInitial"]/div['+n+']/div[2]/div/div[2]').extract())

    for i in l:
        test(i)
    '''
    res = selector.xpath('//span[@class="star_count"]').extract()
    print(res)




