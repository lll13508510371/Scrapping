import json
import pprint
import time
import requests

requests.packages.urllib3.disable_warnings()


def get_page_num():
    url = 'https://coniun.io/api/collections/discover?'

    headers = {
        'access-control-allow-credentials': 'true',
        'access-control-allow-origin': 'https://coniun.io',
        'cf-cache-status': 'DYNAMIC',
        'cf-ray': '78abaef16f411097-HKG',

        'content-type': 'application/json; charset=utf-8',
        'date': 'Tue, 17 Jan 2023 02:32:58 GMT',
        'nel': '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}',
        'report-to': '{"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=AutIKykXu7jrqXh0zkS97piPHKuIrwLz%2BkywFGAov1EWKPnStD%2FzwTWEdC3qHnu2Z2iCu%2BrrnPuWi%2BnjKFp0KiMKwkmFc9pOi5rF9YfllafgqPE0UXYtdqz%2FXQ%3D%3D"}],"group":"cf-nel","max_age":604800}',
        'server': 'cloudflare',
        'set-cookie': 'coniun-session=s%3AeyJtZXNzYWdlIjoiY2xjeXJ5MTgyMDU4cjBobmFkZWxjMzFweiIsInB1cnBvc2UiOiJjb25pdW4tc2Vzc2lvbiJ9.2-5mSZkNJ16Y3LNh1kuRu9mQyxZsAvk1O0p9OBTMaFw; Max-Age=31557600; Path=/; HttpOnly',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-length': '177',
        'content-type': 'application/json',
        'cookie': 'auth.strategy=coniun; _gcl_au=1.1.210517201.1673871621; wooTracker=SBvsDugda0Ot; coniun-session=s%3AeyJtZXNzYWdlIjoiY2xjeXJ5MTgyMDU4cjBobmFkZWxjMzFweiIsInB1cnBvc2UiOiJjb25pdW4tc2Vzc2lvbiJ9.2-5mSZkNJ16Y3LNh1kuRu9mQyxZsAvk1O0p9OBTMaFw; _ga=GA1.2.891013776.1673871622; _gid=GA1.2.1096414723.1673871622; _fbp=fb.1.1673871622652.759319985; __cf_bm=dZ4V3MiDt59fubI4mG4.Qi0NI3SKh1.uaF9FETN48VQ-1673922312-0-ARJI/5eTSF58fi+0crptkHPXgv21FkbvpZ/rME+43z2z09h84p0g+RrEexG7A/oVDJvEPjWDt7P97VY3t/WD0r74AZ6efhPpU8WG0S99uY7cfm1lB7KhQ8PXU/MKAxmiA3QXGrYyL0o0lS8ls2E55LY=',
        'origin': 'https://coniun.io',
        'pragma': 'no-cache',
        'referer': 'https://coniun.io/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    query_params = {
        'page': '1'
    }

    json_params = {"orderBy": "oneDaySales", "orderDirection": "desc", "totalSupply": [0], "oneDayVolume": [0],
                   "sevenDayVolume": [0], "totalVolume": [0], "floorPrice": [0], "totalSales": [0], "oneDaySales": [0]}
    # json=  会把json_params转换成字符串（dumps)
    response = requests.post(url=url, headers=headers, params=query_params, json=json_params, verify=False)

    data = response.json()

    total_item = data['data']['meta']['total']

    per_page = data['data']['meta']['per_page']

    if total_item % per_page != 0:
        page_num = total_item // per_page + 1
    else:
        page_num = total_item / per_page

    return page_num


def get_query_param(page_num):
    query_params = {
        'page': str(page_num)
    }
    return query_params


def save_data(arr):
    with open('Coniun.json', mode='a', encoding='utf-8') as f:
        json_data = json.dumps(arr, ensure_ascii=False)
        f.write(json_data)


def get_data():
    pages = get_page_num()

    array = []

    for page in range(1, pages + 1):
        print(f'第{page}页数据')
        url = 'https://coniun.io/api/collections/discover?'

        headers = {
            'access-control-allow-credentials': 'true',
            'access-control-allow-origin': 'https://coniun.io',
            'cf-cache-status': 'DYNAMIC',
            'cf-ray': '78abaef16f411097-HKG',

            'content-type': 'application/json; charset=utf-8',
            'date': 'Tue, 17 Jan 2023 02:32:58 GMT',
            'nel': '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}',
            'report-to': '{"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=AutIKykXu7jrqXh0zkS97piPHKuIrwLz%2BkywFGAov1EWKPnStD%2FzwTWEdC3qHnu2Z2iCu%2BrrnPuWi%2BnjKFp0KiMKwkmFc9pOi5rF9YfllafgqPE0UXYtdqz%2FXQ%3D%3D"}],"group":"cf-nel","max_age":604800}',
            'server': 'cloudflare',
            'set-cookie': 'coniun-session=s%3AeyJtZXNzYWdlIjoiY2xjeXJ5MTgyMDU4cjBobmFkZWxjMzFweiIsInB1cnBvc2UiOiJjb25pdW4tc2Vzc2lvbiJ9.2-5mSZkNJ16Y3LNh1kuRu9mQyxZsAvk1O0p9OBTMaFw; Max-Age=31557600; Path=/; HttpOnly',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'content-length': '177',
            'content-type': 'application/json',
            'cookie': 'auth.strategy=coniun; _gcl_au=1.1.210517201.1673871621; wooTracker=SBvsDugda0Ot; coniun-session=s%3AeyJtZXNzYWdlIjoiY2xjeXJ5MTgyMDU4cjBobmFkZWxjMzFweiIsInB1cnBvc2UiOiJjb25pdW4tc2Vzc2lvbiJ9.2-5mSZkNJ16Y3LNh1kuRu9mQyxZsAvk1O0p9OBTMaFw; _ga=GA1.2.891013776.1673871622; _gid=GA1.2.1096414723.1673871622; _fbp=fb.1.1673871622652.759319985; __cf_bm=dZ4V3MiDt59fubI4mG4.Qi0NI3SKh1.uaF9FETN48VQ-1673922312-0-ARJI/5eTSF58fi+0crptkHPXgv21FkbvpZ/rME+43z2z09h84p0g+RrEexG7A/oVDJvEPjWDt7P97VY3t/WD0r74AZ6efhPpU8WG0S99uY7cfm1lB7KhQ8PXU/MKAxmiA3QXGrYyL0o0lS8ls2E55LY=',
            'origin': 'https://coniun.io',
            'pragma': 'no-cache',
            'referer': 'https://coniun.io/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }

        json_params = {"orderBy": "oneDaySales", "orderDirection": "desc", "totalSupply": [0], "oneDayVolume": [0],
                       "sevenDayVolume": [0], "totalVolume": [0], "floorPrice": [0], "totalSales": [0],
                       "oneDaySales": [0]}

        try:
            time.sleep(1)

            response = requests.post(url=url, headers=headers, params=get_query_param(page), json=json_params,
                                     verify=False)

            # print(response.url)
            data = response.json()
            # pprint.pprint(data)

            collections = data['data']['data']
            # pprint.pprint(collections)

            for collection in collections:
                # average_price = float(format(collection['average_price'], '.3f'))
                average_price = collection['average_price']
                # print(average_price)
                name = collection['collection']['name']
                thirty_day_average_price = collection['thirty_day_average_price']
                thirty_day_change = collection['thirty_day_change']
                thirty_day_sales = collection['thirty_day_sales']
                thirty_day_volume = collection['thirty_day_volume']
                total_sales = collection['total_sales']
                total_supply = collection['total_supply']
                total_volume = collection['total_volume']
                # print(average_price, name, thirty_day_average_price, thirty_day_change, thirty_day_sales, thirty_day_volume,
                #       total_sales, total_supply, total_volume, sep=' | ')

                collection_dic = {
                    'name': name,
                    'thirty_day_average_price': thirty_day_average_price,
                    'average_price': average_price,
                    'thirty_day_change': thirty_day_change,
                    'thirty_day_sales': thirty_day_sales,
                    'thirty_day_volume': thirty_day_volume,
                    'total_sales': total_sales,
                    'total_supply': total_supply,
                    'total_volume': total_volume
                }
                array.append(collection_dic)

        except Exception:
            pass

    save_data(array)


if __name__ == '__main__':
    # 在if __name__ == '__main__'当中运行python脚本
    # print(get_page_num())
    get_data()
