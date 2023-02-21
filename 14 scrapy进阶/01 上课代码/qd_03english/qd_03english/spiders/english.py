import scrapy

from ..items import Qd03EnglishItem


class EnglishSpider(scrapy.Spider):
    name = "english"
    allowed_domains = ["chinadaily.com.cn"]
    start_urls = [f"https://language.chinadaily.com.cn/thelatest/page_{page}.html" for page in range(1, 11)]

    # def start_requests(self):
        # yield scrapy.Request()

    def parse(self, response):
        # print(response.text)

        divs = response.css('.gy_box')

        for div in divs:
            title = div.css('.gy_box_txt2>a::text').get()
            info = div.css('.gy_box_txt3>a::text').get()
            if info:
                info = info.strip()
            else:
                info = 'None'

            img_url = div.css('.gy_box_img>img::attr(src)').get()
            # print(Qd03EnglishItem(title=title, info=info, img_url=img_url))
            yield Qd03EnglishItem(title=title, info=info, img_url=img_url)

