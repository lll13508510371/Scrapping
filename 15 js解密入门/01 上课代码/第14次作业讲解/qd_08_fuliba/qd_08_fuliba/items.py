# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Qd08FulibaItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    info = scrapy.Field()
    put_time = scrapy.Field()
    reads = scrapy.Field()
    stars = scrapy.Field()
