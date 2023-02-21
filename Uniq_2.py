import csv
import json
import requests


def get_page_num():
    url = 'https://api.uniq.cx/api/collections/?page=0'  # 这里传参数会好一点，这样也没问题

    headers = {
        'Referer': 'https://uniq.cx/',
        'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)

    data = response.json()

    item_num = data['numCollections']

    # print(item_num)

    if item_num % 50 != 0:
        page_num = item_num // 50 + 1
    else:
        page_num = item_num / 50

    return page_num


def save_data(array):
    with open('Uniq.csv', mode='a', encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['name', 'thirty_day_average_price', 'thirty_day_change',
                                                   'thirty_day_difference',
                                                   'thirty_day_sales', 'thirty_day_volume'])
        csv_writer.writeheader()

        for i in array:
            csv_writer.writerow(i)



def get_data():
    pages = get_page_num()

    array = []

    for i in range(pages):
        url = f'https://api.uniq.cx/api/collections/?page={i}'

        headers = {
            'Referer': 'https://uniq.cx/',
            'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
        try:
            response = requests.get(url=url, headers=headers)

            print(f'第{i + 1}页数据')

            data = response.json()

            collection = data['collections']
            # print(collection)
            # print(collection[0]['stats']['thirty_day_average_price'])

            for j in collection:
                name = j['name']
                thirty_day_average_price = j['stats']['thirty_day_average_price']
                thirty_day_change = j['stats']['thirty_day_change']
                thirty_day_difference = j['stats']['thirty_day_difference']
                thirty_day_sales = j['stats']['thirty_day_sales']
                thirty_day_volume = j['stats']['thirty_day_volume']
                data_dic = {
                    'name': name,
                    'thirty_day_average_price': thirty_day_average_price,
                    'thirty_day_change': thirty_day_change,
                    'thirty_day_difference': thirty_day_difference,
                    'thirty_day_sales': thirty_day_sales,
                    'thirty_day_volume': thirty_day_volume
                }
                # print(thirty_day_average_price, thirty_day_change, thirty_day_difference, thirty_day_sales, thirty_day_volume,
                #       sep=' | ')
                # print(data_dic)

                # append的内容会成为列表中单独的一个元素，下一个append的内容会成为列表新的一个元素
                array.append(data_dic)
                # print(array)

        except Exception:
            pass

    save_data(array)


# url = f'https://api.uniq.cx/api/collections/?page=0'
#
# headers = {
#     'Referer': 'https://uniq.cx/',
#     'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
# }
#
# response = requests.get(url=url, headers=headers)
#
# # html_data = response.text
# # print(html_data)
#
# data = response.json()
# # print(data)
# collection = data['collections']
# # print(collection)
# # print(collection[0]['stats']['thirty_day_average_price'])
#
# for i in collection:
#     thirty_day_average_price = i['stats']['thirty_day_average_price']
#     thirty_day_change = i['stats']['thirty_day_change']
#     thirty_day_difference = i['stats']['thirty_day_difference']
#     thirty_day_sales = i['stats']['thirty_day_sales']
#     thirty_day_volume = i['stats']['thirty_day_volume']
#     print(thirty_day_average_price, thirty_day_change, thirty_day_difference, thirty_day_sales, thirty_day_volume,
#           sep=' | ')

if __name__ == '__main__':
    # print(get_page_num())
    get_data()
