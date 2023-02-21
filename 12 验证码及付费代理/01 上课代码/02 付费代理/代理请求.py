import requests


def get_proxy():
    url = 'http://zltiqu.pyhttp.taolop.com/getip?count=1&neek=13873&type=2&yys=0&port=2&sb=&mr=2&sep=0&ts=1'
    response = requests.get(url=url)
    json_data = response.json()
    # print(json_data)

    ip_port = json_data['data'][0]['ip'] + ":" + str(json_data['data'][0]['port'])
    # print(ip_port)

    proxies = {
        "http": "http://" + ip_port,
        "https": "http://"  + ip_port,
    }
    return proxies



# get_proxy()
if __name__ == '__main__':
    url = 'https://www.baidu.com'
    response = requests.get(url=url, proxies=get_proxy())
    print(response.text)
    print(response.status_code)
"""
代理形式
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}
"""