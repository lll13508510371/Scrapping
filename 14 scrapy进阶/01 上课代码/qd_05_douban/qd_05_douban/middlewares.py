# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import requests
from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
"""
两个中间中间件都能够处理请求和响应, 但是使用场景不同
    DownloaderMiddleware: 下载中间件
        主要的作用: 处理请求的headers cookies  proxy
    
    SpiderMiddleware: 爬虫中间件
        主要作用: 过滤错误请求的, 默认会过滤错误状态码 500 400
"""


class Qd05DoubanSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class Qd05DoubanDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class HeadersDownloaderMiddleware:
    """headers中间件"""
    def process_request(self, request, spider):
        # request.headers 拿到请求体中的请求头, 是一个字典对象
        request.headers.update(
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'Host': 'movie.douban.com',
                'Referer': 'https://www.baidu.com/link?url=wf1FW88qared7_mXkzsRXYtXcZSdTYlU7QHfydXY5u5BaFkbv17in4o5jVry9tIYk-SvijHdj08pSm6nHCYukq&wd=&eqid=e2d97ff4000034940000000663ef7e79'
            }
        )
        return None

class CookiesDownloaderMiddleware:
    """Cookies中间件"""
    def process_request(self, request, spider):
        # request.cookies 拿到请求体中的cookies, 是一个字典对象
        # cookies 片段信息有时候在请求不到数据的时候可以单独构建片段信息的键值对
        cookie = {'Cookie': 'bid=JOjnHzNKNdU; __gads=ID=390a3a70609550e8-22df6781f5d10053:T=1649854444:RT=1649854444:S=ALNI_MZfvUIHFs1pOYgYSuPbsvh7fVT9Yw; ll="118267"; _vwo_uuid_v2=D9BE563CAF8DB68077925251DB19E9857|7ec7c5b6350ccfad2f138472e47a6641; _ga=GA1.2.1895635950.1649854444; gr_user_id=9841cb26-ad30-4da9-9fad-006c711b218f; __yadk_uid=u5mrwOVUZy3PATAVm4vE63U7vqrPrxRl; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1676639868%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dwf1FW88qared7_mXkzsRXYtXcZSdTYlU7QHfydXY5u5BaFkbv17in4o5jVry9tIYk-SvijHdj08pSm6nHCYukq%26wd%3D%26eqid%3De2d97ff4000034940000000663ef7e79%22%5D; _pk_id.100001.4cf6=5a00c88162b3f1ff.1649854444.32.1676639868.1675084934.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1895635950.1649854444.1675859620.1676639868.36; __utmb=30149280.0.10.1676639868; __utmc=30149280; __utmz=30149280.1676639868.36.27.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.913704788.1649854444.1675084934.1676639868.32; __utmb=223695111.0.10.1676639868; __utmc=223695111; __utmz=223695111.1676639868.32.23.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __gpi=UID=0000059a569b8b1b:T=1653051309:RT=1676639869:S=ALNI_MboLjGTnG9YzoGaau8maDJk8dhE7A'}
        request.cookies.update(cookie)
        return None


def get_proxy():
    url = 'http://zltiqu.pyhttp.taolop.com/getip?count=1&neek=13873&type=2&yys=0&port=2&sb=&mr=2&sep=0&ts=1'
    response = requests.get(url=url)
    json_data = response.json()
    # print(json_data)

    ip_port = json_data['data'][0]['ip'] + ":" + str(json_data['data'][0]['port'])
    # print(ip_port)

    # 在scrapy框架中, 代理形式: http://0.0.0.0:5000 -》 0.0.0.0是代理服务器，5000是代理服务器端口
    # proxies = {
    #     "http": "http://" + ip_port,
    #     "https": "http://"  + ip_port,
    # }
    return ip_port

class ProxyDownloaderMiddleware:
    """Proxy中间件"""
    def process_request(self, request, spider):
        # request.meta['proxy'] 赋值操作, 就是使用代理请求数据
        request.meta['proxy'] = 'https://' + get_proxy()
        return None

# 有时候代理质量不高
# 当代理质量不高的时候我们要配置, 重试

# print(get_proxy())

# 反扒相关的业务逻辑, 都是在中间件文件写代码
