import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

# json数据本质上是字符串类型
# json() --> 转对象 []  {}


"""将Python字典/列表转成json字符串"""
"""
将Python字典/列表转成json字符串, 叫做json序列化
"""
json_str = json.dumps(data)
print(json_str)
print(type(json_str))


"""将json字符串转成Python字典/列表"""
"""
将json字符串转成Python字典/列表, 叫做json反序列化
"""
json_obj = json.loads(json_str)
print(json_obj)
print(type(json_obj))

"""字典或者列表是可以直接进行json数据的序列化或者反序列化操作"""