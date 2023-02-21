import scrapy

from ..items import Qd07MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = "maoyan"
    allowed_domains = ["maoyan.com"]
    start_urls = ["https://m.maoyan.com/asgard/board/4"]

    def parse(self, response):
        # print(response.text)
        divs = response.css('.board-card.clearfix')  # 提取到所有的div标签

        for div in divs:
            title = div.css('.title::text').get()
            actors = div.css('.actors::text').get()
            date = div.css('.date::text').get()
            number = div.css('.number::text').get()
            print(Qd07MaoyanItem(title=title, actors=actors, date=date, number=number))
            yield Qd07MaoyanItem(title=title, actors=actors, date=date, number=number)
