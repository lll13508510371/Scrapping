import scrapy

from ..items import Qd04KfcItem


class KfcSpider(scrapy.Spider):
    name = "KFC"
    allowed_domains = ["kfc.com.cn"]

    # 在start_urls列表里面默认发送的请求只能发送get请求
    # start_urls = ["http://kfc.com.cn/"]

    # 重写请求
    def start_requests(self):
        # scrapy.FormRequest 可以帮助我们发送post请求
        yield scrapy.FormRequest(
            url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',
            # formdata 提交post请求的表单数据, 请求参数 查询参数要写在url当中
            formdata={
                'cname': '',
                'pid': '',
                'keyword': '北京',
                'pageIndex': '1',
                'pageSize': '10',
            },
            callback=self.parse,
            meta={'page': 2}  # 1.meta一定要指定成字典对象, 键值对自定义的
        )

    """
    meta 用于两两函数间的数据传递
    meta 再函数键传递数据是一次性的, 如果有多级页面, 那么就会有多个函数, meta需要在函数中一级一级传递
    meta是一个字典, 键值对自定义的, 后可以根据键获取到值
    """

    def parse(self, response):
        # print(response.json())

        print('传下来的meta值为:', response.meta.get('page'))

        data_list = response.json()['Table1']

        for dat in data_list:
            storeName = dat['storeName']
            provinceName = dat['provinceName']
            addressDetail = dat['addressDetail']
            pro = dat['pro']
            print(Qd04KfcItem(storeName=storeName, provinceName=provinceName,
                              addressDetail=addressDetail, pro=pro))
            yield Qd04KfcItem(storeName=storeName, provinceName=provinceName,
                              addressDetail=addressDetail, pro=pro)

        page = response.meta.get('page')

        if page <= 10:
            yield scrapy.FormRequest(
                url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',
                # formdata 提交post请求的表单数据, 请求参数
                formdata={
                    'cname': '',
                    'pid': '',
                    'keyword': '北京',
                    'pageIndex': str(page),
                    'pageSize': '10',
                },
                callback=self.parse,
                meta={'page': page + 1}  #
            )
