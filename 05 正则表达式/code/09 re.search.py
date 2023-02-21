import re  # 内置

string = '0000PythonahsdgjasghPythonasdjajsk'

# Python  需要匹配的字符串;   string 需要在哪个字符串中匹配内容
# re.search 在字符串中任意位置到符合条件的结果, 找到了就返回, 只会找一次
# 如果找到了就返回 re.Match 对象, 可以使用 对象.group()
result = re.search('Python', string)
print(result)
print(result.group())

'''
<re.Match object; span=(4, 10), match='Python'> --> span 范围
'''
