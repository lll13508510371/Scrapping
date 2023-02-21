import scrapy

"""
作用:
    1.收集所有需要采集的地址
    2.解析数据

"""


class QuotesSpider(scrapy.Spider):  # scrapy.Spider 爬虫基类
    # 爬虫文件的名字,通过scrapy genspider 时创建, 后期启动爬虫项目的时候需要指定爬虫的名字
    name = "quotes"

    # 在运行爬虫的时候, 对采集的地址进行域名的限制, 只要这个属于这个域名的地址都会采集
    # 如果列表为空, 代表没有限制域名
    allowed_domains = []

    # 数据采集的起始网址, 爬虫从哪个网址进行采集, 对于有规律的url地址, 一般采用列表推导式取收集所有需要采集的地址
    # 在列表中的网址, 都会被请求到, 默认请求到的数据都会交给下面的函数<parse>处理
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        # start_urls  起始网址返回的数据, 默认会给 parse 函数进行处理
        # 默认会携带 response 参数
        # response 具有所有响应体和请求体的方法和属性 + 以及具有 parsel<css, xpath re>模块中所有数据解析的方法 parsel也是从scrapy当中拿出去的
        # print(response.text)

        """数据二次提取"""
        divs = response.css('.quote')

        for div in divs:
            text = div.css('.text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('.tags>a::text').getall()

            # scrapy框架里面所有爬虫文件返回的数据  全部用 yield 返回
            # 一条一条返回数据
            # yield返回的是字典, 那么scrapy框架会自动处理
            yield {
                'text': text,
                'author': author,
                'tags': tags,
            }

# 如果反扒了呢?
# 数据怎么保存呢?
