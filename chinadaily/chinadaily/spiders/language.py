import re

import scrapy
from ..items import ChinadailyItem


class LanguageSpider(scrapy.Spider):
    name = "language"
    allowed_domains = ["chinadaily.com.cn"]

    # start_urls = [f"http://language.chinadaily.com.cn/thelatest/page_{i}.html" for i in range(1, 11)]

    # start_urls = ["http://language.chinadaily.com.cn/thelatest/page_1.html"]

    '''
    ！！！！start_requests -->> 这个函数不是自定义的函数，scrapy框架会在底层对应找 之前写成 start_request就爬不到数据还不知道什么情况
    -->>   start_requests 是scrapy框架里面的函数，只不过需要自己手动创建写逻辑，框架会处理这个函数
    '''

    def start_requests(self):
        yield scrapy.Request(url="http://language.chinadaily.com.cn/thelatest/page_1.html", callback=self.parse)

    #     '''
    #     callback --> 把这一次url的请求交给谁来处理  这里交给parse函数来处理
    #     回掉和递归有点像，现在还不能发现两者的区别
    #     !!! scrapy有很多callback
    #     '''

    def parse(self, response):
        divs = response.css('.content_left>.gy_box')
        '''
        parse函数已经根据前面的url请求得到了response
        '''

        # 一页15个数据，十页150
        for div in divs:
            title = div.css('.gy_box_txt>p:nth-child(1)>a::text').get().replace('"', "'")
            '''
            ！！！写入csv文件时候很多符号不能写进去，看文件发现有一些地方莫名奇妙有换行导致field写错，
            意识到是introduction爬取到的一些数据结尾有空白，用strip()去除就没问题了，其它有问题的地方再replace一下
            '''

            '''
            框架不能用异常捕获，可能还是会把错误暴露出来 --->>>  也可以发现，当start_urls构建了多个urls，某一个出错了不会影响其它的请求
                                                        只会给出那个错误请求的错误信息
            这里加了try except 还是给出了 introduction 的错误，然后结束了程序运行，得用if else改一下  
            ！！！知道 introduction 是有问题的 下面给出了introduction的报错说明框架使用异常捕获可能还是会报错（也可能不报错，第一次第二次爬取没有报错），！所以不要使用异常捕获                                     
            UnboundLocalError: local variable 'introduction' referenced before assignment 
                                           
            能使用一些例如异常重试之类的方法
            '''
            # try:
            introduction = div.css('.gy_box_txt>p:nth-child(2)>a::text').get()
            # 判断一下introduction是不是空值，不是进行字符串操作，是就给introduction 赋一个none字符串
            if introduction:
                introduction = div.css('.gy_box_txt>p:nth-child(2)>a::text').get().strip().replace(' "', "'").replace(
                    ',', '，').replace('"', "'")
            else:
                introduction = 'None'

            # except Exception:
            #     pass
            '''
            这里写a标签定位不到，不知道为什么 --> 能定位到，和xpath记混淆了，xpath二次提取要用.表示从当前节点开始, css不存在这个问题
            '''
            img = div.css('a>img::attr(src)').get()

            '''
            scrapy crawl language -o data.csv 在没有写pipeline.py保存逻辑的时候用来做测试（测试解析的字段是否完整），生成的csv文件会有field，
            正式的保存文件例如language.csv不会有field
            '''
            '''方法一'''
            # yield {'title': title,
            #        'introduction': introduction,
            #        'img': img}
            '''方法二'''
            yield ChinadailyItem(title=title, introduction=introduction, img=img)

        '''
        ！！！！！我服了，标签之前定位有两个，数据爬不完整，一定要注意找到唯一的标签啊！！！！！！
        '''
        '''
        这里因为next_page（href）得到没有https://所以要提取出来
        '''
        next_page = response.css('.content_left>#div_currpage>a:nth-last-child(2)::attr(href)').get().split('/')[-1]
        page_num = int(re.findall('.*_(.*?)\..*', next_page)[0])
        '''
        ！可以字符串数字比大小 （ 前面验证码叫传字符串数字，但传int数字也可以，--> python好像对于数字不区分是str还是int
        ---->>>>>>> !! 艹，不能比较字符串数字大小 '2' < '11' 得到的是False
        '''

        if page_num:
            url = 'http://language.chinadaily.com.cn/thelatest/' + next_page

            yield scrapy.Request(url=url, callback=self.parse)


'''
！！！！！！！！！！！！！！！！！！！！！！！！！！！！
crawl 所有数据（这里是一页一页爬取，因为不知道多少页，找翻页逻辑一页一页翻的）
爬多了几次就会变慢，可能被限制请求了（也可能是网速问题，网速自己感觉得到，也可以测速，打开请求的网页速度正常 网速一般就没有问题），我记得刚开始几分钟就爬完了

INFO: Ignoring response <502 http://language.chinadaily.com.cn/thelatest/page_357.html>: HTTP status code is not handled or not allowed
2023-02-17 16:55:04 [scrapy.spidermiddlewares.httperror] INFO: Ignoring response <502 http://language.chinadaily.com.cn/thelatest/page_22.html>: HTTP status code is not handled or not allowed
最终爬到一定页面就不让爬取数据了，这样应该是被识别出来不是人正常请求给反爬了，应该要加上headers cookies才能爬到了，学了scrapy 高级添加上再试一下

--->>> 这里是爬取速度太快被🚫请求了 在scrapy default_setting当中设置了 DOWNLOAD_DELAY=1（等待一秒再进行下一次请求，之前默认是=0）
'''
