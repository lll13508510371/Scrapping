# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ChinadailyPipeline:
    def process_item(self, item, spider):
        with open('language_2.csv', mode='a', encoding='utf-8', newline='') as f:
            f.write(item['title'] + ',' + item['introduction'] + ',' + item['img'])
            f.write('\n')
        return item
