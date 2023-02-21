import scrapy
from ..items import ScrapyProjectItem


class MaoyanSpider(scrapy.Spider):
    name = "maoyan"
    allowed_domains = ["maoyan.com"]
    start_urls = ["https://m.maoyan.com/board/4"]

    '''
    pipeline中如果用with保存内容用w写入，在终端中用 -o data.csv测试不会内容覆盖，会进行附加操作 -> 'a'
    '''

    def parse(self, response):
        '''
        1. 终端中查看是否能请求到数据，这里没有请求到，首先想机器人协议，在setting当中关了还请求不到，添加请求头，还是请求不到，加cookies(scrapy当中要单独加）,
        不行，最终proxy。可以都写上，给优先级，我的理解是，按优先级，如果请求到数据就不会使用优先级低的 -->>  headers > cookies > proxy 自己设置的优先级
        '''
        # print(response.text)
        # print(response.request.headers)
        divs = response.css('.board-card.clearfix')  # 提取到所有的div标签

        for div in divs:
            name = div.css('.title::text').get()
            star = div.css('.actors::text').get()
            releasetime = div.css('.date::text').get()
            score = div.css('.number::text').get()
            # print(name)
            yield ScrapyProjectItem(name=name, star=star, releasetime=releasetime, score=score)
            # 也可以直接构建成字典{'name': name,'star': star, 'releasetime': releasetime, 'score': score}
            '''
            2. 在 items.py 数据结构当中 写入需要的数据字段  --->>> yield的数据经过items文件的数据结构处理变为相应的item对象（scrapy定义的字典对象）
            '''
            '''
            3. 在pipeline当中写保存逻辑，然后在setting当中打开管道让yield的数据流进管道进行保存 
            --->>> 应该是yield的数据先经过items文件的数据结构处理变为相应的item对象（scrapy定义的字典对象）然后再进入管道，在pipeline文件当中直接使用item对象来进行相应的操作
            '''
            '''
            😄 发现到最后打开了五个文件，爬虫文件和四个配置文件来进行协调，不再是单独使用一个文件进行编写了 😄
            '''
