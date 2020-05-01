from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from myspider.spiders.indiatimes import IndiatimesSpider


def main():
    settings = get_project_settings()

    process = CrawlerProcess(settings)
    process.crawl(IndiatimesSpider)
    process.start()
    process.join()


if __name__ == '__main__':
    main()
