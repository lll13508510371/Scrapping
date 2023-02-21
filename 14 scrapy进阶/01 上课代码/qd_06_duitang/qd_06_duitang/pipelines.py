# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter

# 二进制数据下载需要继承自 ImagesPipeline
from scrapy.pipelines.images import ImagesPipeline


class DownloadPicture(ImagesPipeline):
    # get_media_requests 请求 二进制数据 的方法
    def get_media_requests(self, item, info):
        img_url = item['img_url']
        # 构建二进制数据请求, 需要用过yield返回请求
        yield scrapy.Request(url=img_url)
        '''
        这里可以看出框架的好处，可以根据相应的方法直接得到想要的结果，不需要请求图片url再得到二进制数据，
        直接通过 专门用于请求二进制数据的get_media_requests函数 yield scrapy.Request(url=img_url) 就可以得到二进制数据
        '''

    '''
    网页上的图片名是根据某种加密算法确定的，确保每一张图片名都不一样
    '''
