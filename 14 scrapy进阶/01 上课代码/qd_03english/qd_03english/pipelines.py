# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import json

from itemadapter import ItemAdapter


# class Qd03EnglishPipeline:
#     def process_item(self, item, spider):
#         with open('english.csv', mode='a', encoding='utf-8') as f:
#             f.write(item['title'] + ',' + item['info'] + ',' + item['img_url'])
#             f.write('\n')
#         return item

class CSVPipeline:
    # def __init__(self):
    #     ## 可选实现，做参数初始化等
    #     ## doing something
    #     pass

    def open_spider(self, spider):  # spider 指的是爬虫对象
        """初始化方法, 文件的打开, 链接数据库"""
        self.f = open('english.csv', mode='a', encoding='utf-8', newline='')
        self.csv_write = csv.DictWriter(self.f, fieldnames=['title', 'info', 'img_url'])
        self.csv_write.writeheader()  # 写入表头, 只需要写一次

    def process_item(self, item, spider):
        """
        process_item  专门用于处理item数据的
        :param item: 爬虫文件解析返回的数据结构
        :param spider: 爬虫对象
        :return: item 传过来的数据必须原路返回, 给其他的管道类使用
        """
        d = dict(item)
        self.csv_write.writerow(d)

        # item 必须原路返回, 因为其他的管道类可能会使用
        return item

    def close_spider(self, spider):
        """整个项目停止之前, 默认会调用的这个函数, 一般关闭文件或者关闭数据库链接"""
        self.f.close()  # 关闭打开的文件对象


class JsonPipeline:  # [{}, {}, {},......]
    def open_spider(self, spider):
        self.f = open('english.json', mode='w', encoding='utf-8')
        # 收集每一条 item 数据
        self.d_list = []

    def process_item(self, item, spider):
        # print('self.d_list:', self.d_list)
        d = dict(item)  # 是类字典对象, 但是不是原生字典, 可以强制转化 --> 可以理解成scrapy定义的字典，不是python原生字典
        self.d_list.append(d)
        return item

    def close_spider(self, spider):
        # json数据的序列化操作, 写入到文件
        json_str = json.dumps(self.d_list, ensure_ascii=False)
        # print('json_str:::', json_str)
        self.f.write(json_str)
        self.f.close()


# class JsonPipeline_2: