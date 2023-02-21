import re

string = 'Pythonasdkjasd 123456 adhuiaghsdk 654321 akjsdhkashdkja'

"""
pattern     根据语法匹配到的字符串分割
string      需要在哪个字符串分割数据
maxsplit    指定最大分割次数
flags       匹配模式
"""
result = re.split('\d+', string, maxsplit=1)
print(result)
print(string)
