import scrapy

from ..items import Qd02ZzsItem


class ZzsSpider(scrapy.Spider):
    name = "zzs"
    allowed_domains = ["zhangzishi.com"]
    start_urls = [f"https://www.zhangzishi.com/page/{page}" for page in range(1, 36)]

    def parse(self, response):
        # print(response.text)
        # response.css('')

        articles = response.css('.content>article')
        for art in articles:
            title = art.css('h2>a::text').get()
            info = art.css('.note::text').get()
            reads = art.css('.post-views::text').get()
            commons = art.css('.post-like>span::text').get()

            yield Qd02ZzsItem(title=title, info=info, reads=reads, commons=commons)


