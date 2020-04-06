import requests
import scrapy


def main():
    movies = []

    response = requests.get('https://timesofindia.indiatimes.com/entertainment/latest-new-movies/hindi-movies.com')

    if response.status_code == 200:
        selector = scrapy.Selector(text=response.text)

        movie_selectors = selector.xpath('//div[@class="mr_lft_box"]')

        for mov_sel in movie_selectors:
            movies.append({
                'name': mov_sel.xpath('div[@class="FIL_right"]/a/h3/text()').extract_first(),
                'url': mov_sel.xpath('div[@class="FIL_left"]/a/@href').extract_first()
            })

    print(len(movies))
    print(movies)


if __name__ == '__main__':
    main()

