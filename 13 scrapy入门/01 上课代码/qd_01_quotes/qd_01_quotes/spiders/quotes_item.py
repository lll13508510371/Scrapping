import scrapy

# ..  表示取上级目录
from ..items import Qd01QuotesItem


# from qd_01_quotes.qd_01_quotes.items import Qd01QuotesItem


class QuotesNextSpider(scrapy.Spider):
    name = "quotes_item"
    allowed_domains = []
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        divs = response.css('.quote')

        for div in divs:
            text = div.css('.text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('.tags>a::text').getall()

            # 将数据通过 items 数据结构一条条返回
            # 以 items 数据结构 返回的数据默认在执行的时候会打印在终端显示
            yield Qd01QuotesItem(text=text, author=author, tags=tags)

            # yield {
            #     'text': text,
            #     'author': author,
            #     'tags': tags,
            # }
