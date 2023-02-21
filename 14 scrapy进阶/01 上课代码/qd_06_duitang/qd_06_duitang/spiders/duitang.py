import scrapy

from ..items import Qd06DuitangItem


class DuitangSpider(scrapy.Spider):
    name = "duitang"
    allowed_domains = ["duitang.com"]
    start_urls = ["https://www.duitang.com/napi/blogv2/list/by_search/?kw=%E8%9C%A1%E7%AC%94%E5%B0%8F%E6%98%9F&after_id=48&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&_=1676289161640"]

    def parse(self, response):
        # print(response.json())

        data_list = response.json()['data']['object_list']

        for data in data_list:
            img_url = data['photo']['path']
            yield Qd06DuitangItem(img_url=img_url)
