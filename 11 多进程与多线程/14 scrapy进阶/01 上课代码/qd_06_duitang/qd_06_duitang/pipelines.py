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
    # get_media_requests 请求二进制数据的方法
    def get_media_requests(self, item, info):
        img_url = item['img_url']
        # 构建二进制数据请求, 需要用过yield返回请求
        yield scrapy.Request(url=img_url)
