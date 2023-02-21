import scrapy
from ..items import FulibaItem


class FulibaSpider(scrapy.Spider):
    name = "fuliba"
    allowed_domains = ["fuliba2023.net"]
    start_urls = ["http://fuliba2023.net/"]

    def parse(self, response):
        # print(response.text)
        '''
        确实得关闭机器人协议，这里可以得到一部分内容，但另外一部分内容显示会有问题（乱码，重叠之类的反正看着很怪），关闭了就显示正常了
        '''
        articles = response.css('.excerpt')

        for article in articles:
            title = article.css('header a::attr(title)').get()  # 文章标题
            put_time = article.css('.meta>time::text').get()  # 发布时间
            comments = article.css('.meta>span::text').get().replace('阅读', '').lstrip('(').rstrip(')')  # 评论数 --> 应该是阅读数吧 -> yep
            starts = article.css('.meta>.post-like>span::text').get()  # 点赞数
            info = article.css('p::text').get()  # 简介

            '''
            这里应该是创建一个FulibaItem类对象item（就像创建字符串类对象那种，str是一个class,看类型的时候就是str class，这里看item类型应该也是 FulibaItem class） 
            -> items.py 里面有写define the fields for your item here
            '''
            yield FulibaItem(title=title, put_time=put_time, comments=comments, starts=starts, info=info)

        next_page = response.css('.next-page>a::attr(href)').get()
        # print('下一页标签是：', next_page)

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

        '''
        -o 是管道没有打开之前用来测试的，如果管道打开，正式和测试文件都会生成
        '''



