# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Qd01QuotesPipeline:
    def process_item(self, item, spider):
        # pipelines 会拿到每一条items数据
        # d = dict(item)
        with open('quotes.csv', mode='a', encoding='utf-8') as f:
            f.write(item['text'] + ',' + item['author'] + ',' + '-'.join(item['tags']))
            f.write('\n')

        return item


"""
管道文件/数据管道
    
    所有的数据最终都会流经数据管道
    一般通过数据管道取进行数据存储
    
管道文件写完后需要在设置文件中配置生效
"""
