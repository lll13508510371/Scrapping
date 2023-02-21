# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 在项目中定义数据结构字段
# 如果后续在scrapy项目数据传递是一个类字典对象, 可以通过此文件设置字典的键, 用于数据传递
class Qd01QuotesItem(scrapy.Item):  # scrapy.Item  scrapy中数据结构的基类
    # define the fields for your item here like:
    # name = scrapy.Field()
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
