import requests
import scrapy


def test1(url, xp):
    response = requests.get(url)
    if response.status_code == 200:
        selector = scrapy.Selector(text=response.text)
        divs = selector.xpath(xp)
        print('name:', divs)
        print(divs.extract())
        return divs


def test1s(divs, xp):
        r = divs.xpath(xp)
        print('name:', r)
        print(r.extract())
        return r


'''
<div>
    <a>
        <p>...</p>
        <p>...</p>
        <p>...</p>
    </a>
    <a>...</a>
    <a>...</a>
</div>
# for a in div
# print(a[0], a[0][:])
'''
# 上一步得到的大块，子成员解析xpath，解析第几个子成员
# 打印制定第几个子解析的内容，再打印其的解析结果，返回解析结果对应的元素块
def test2(divs, xp, n):
        for j,i in enumerate(divs):
            if j == n:
                print('name:', i)
                print(i.extract())
                print('----------------------------------')
                div = i.xpath(xp)
                print('name:', div)
                print(div.extract())
                return div


def test3(url, xp1, xp2):
    response = requests.get(url,verify=False)
    if response.status_code == 200:
        selector = scrapy.Selector(text=response.text)
        divs = selector.xpath(xp1)
        print(divs.extract())
        for i in divs:
            div = i.xpath(xp2)
            print(div.extract())


url = 'https://timesofindia.indiatimes.com/entertainment/latest-new-movies/hindi-movies'
'''
xp = '//*[@id="perpetualListingInitial"]/div[1]/div[2]/a/h3'
test1(url, xp)
'''

xp1 = '//*[@id="perpetualListingInitial"]' 
d = test1(url, xp1)

print('----------------------------------')

xp1s = '//h3'
dd = test1s(d, xp1s)
