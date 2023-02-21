import re


string = 'Pythonasdkjasd Java adhuiaghsdk Java akjsdhkashdkja'

"""
pattern 正则语法
repl    通过正则匹配的数据需要替换的内容
string  在哪个字符串中替换, 可以写一个函数作为替换规则, 根据函数对象返回值结果做替换
count   替换次数
flags   模式
"""

def func(x):
    return '你好'

'''
repl can be either a string or a callable-->可调用对象（e.g.函数对象）所以不能够直接调用函数对象得到返回值
'''
result = re.sub('Java', 'python', string, count=1)
print(result)

result = re.sub('Java', 'python', string, count=2)
print(result)

result = re.sub('Java', func, string, count=1)
print(result)

'''
re.sub 和 re.findall用的最多，其它做一个了解
'''

