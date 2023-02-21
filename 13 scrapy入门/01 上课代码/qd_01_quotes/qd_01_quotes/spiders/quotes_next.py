import scrapy

from ..items import Qd01QuotesItem


class QuotesNextSpider(scrapy.Spider):
    name = "quotes_next"
    allowed_domains = []

    # start_urls = [f"https://quotes.toscrape.com/page/{page}/" for page in range(1, 11)]
    # start_urls = ['https://quotes.toscrape.com/page/1/']

    # start_requests 重写start_urls， 只能从一个地址出发
    # -->>  这不就是start_urls = ['https://quotes.toscrape.com/page/1/']

    # start_requests 是scrapy框架里面的函数，只不过需要自己手动def创建写逻辑，框架会处理这个函数
    def start_requests(self):
        yield scrapy.Request(url='https://quotes.toscrape.com/page/1/', callback=self.parse)
    '''
    对于请求不知道有多少页的网站，就设置一个url,之后找到翻页url，通过回调函数来进行数据抓取（通过if来确定是否还有下一页）
    '''
    def parse(self, response):
        divs = response.css('.quote')

        for div in divs:
            text = div.css('.text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('.tags>a::text').getall()

            yield Qd01QuotesItem(text=text, author=author, tags=tags)

        """处理翻页"""
        next_page = response.css('.next>a::attr(href)').get()

        '''next_page没有会返回None'''
        if next_page:
            next_url = 'http://quotes.toscrape.com' + next_page

            # yield scrapy.Request() 构建一个请求
            # callback  处理这一次请求的函数, 回调函数
            yield scrapy.Request(url=next_url, callback=self.parse)
            # yield scrapy.Request(url=next_url, callback=self.parse_1)
    def parse_1(self, response):
        pass
