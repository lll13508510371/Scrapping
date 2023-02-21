import scrapy

from ..items import Qd08FulibaItem


class FulibaSpider(scrapy.Spider):
    name = "fuliba"
    allowed_domains = ["fuliba2023.net"]
    start_urls = [f"https://fuliba2023.net/page/{page}" for page in range(1, 151)]

    def parse(self, response):
        # print(response.text)
        arts = response.css('.content>article')

        for art in arts:
            title = art.css('h2>a::text').get()
            info = art.css('.note::text').get()
            put_time = art.css('.meta>time::text').get()
            reads = art.css('.pv::text').get()
            stars = art.css('.post-like>span::text').get()
            print(Qd08FulibaItem(title=title, info=info, put_time=put_time,
                                 reads=reads, stars=stars))
            yield Qd08FulibaItem(title=title, info=info, put_time=put_time,
                                 reads=reads, stars=stars)


