import requests
import scrapy


response = requests.get('https://timesofindia.indiatimes.com/entertainment/latest-new-movies/hindi-movies?curpg=100')

if response.status_code == 200:
    selector = scrapy.Selector(text=response.text)
    movie_selectors = selector.xpath('//*[@id="perpetualListingInitial"]//div[@class="mr_lft_box"]').extract_first()
    print(movie_selectors)

print('------------------------------------------')

response = requests.get('https://timesofindia.indiatimes.com/entertainment/latest-new-movies/hindi-movies?curpg=2')

if response.status_code == 200:
    selector = scrapy.Selector(text=response.text)
    movie_selectors = selector.xpath('//*[@id="perpetualListingInitial"]//div[@class="mr_lft_box"]').extract_first()
    print(movie_selectors)


