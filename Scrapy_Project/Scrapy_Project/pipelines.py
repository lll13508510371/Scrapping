# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


# class ScrapyProjectPipeline:
#     def process_item(self, item, spider):
#         return item

'''
这里类名可以自己定，只不过之后要在setting中添加
'''
class CSVPipeline:
    # def __init__(self):
    #     ## 可选实现，做参数初始化等
    #     ## doing something
    #     pass

    def open_spider(self, spider):  # spider 指的是爬虫对象
        """初始化方法, 文件的打开, 链接数据库"""
        self.f = open('maoyan.csv', mode='w', encoding='utf-8')
        self.csv_writer = csv.DictWriter(self.f, fieldnames=['name', 'star', 'releasetime', 'score'])
        self.csv_writer.writeheader()

    # 这个方法必须实现
    def process_item(self, item, spider):
        """
        process_item  专门用于处理item数据的
        :param item: 爬虫文件解析返回的数据结构
        :param spider: 爬虫对象
        :return: item 传过来的数据必须原路返回, 给其他的管道类使用
        """
        d = dict(item)
        self.csv_writer.writerow(d)

        return item

    def close_spider(self, spider):
        """整个项目停止之前, 默认会调用的这个函数, 一般关闭文件或者关闭数据库链接"""
        self.f.close()
