
"""
    根据下方出现的电话号码进行加密
    
    需求:
        最终效果: 181****5458
"""
import re

tel = "18123115458"

def func(x):
    print(x)
    print(x.group())
    str_ = x.group()
    return str_[:3] + '****' + str_[-4:]

# sub方法中第二个参数可以传函数规则, 函数规则的返回值结果就是替换结果
result = re.sub('\d{11}', func, tel)
print(result)

result2 = re.sub('\d{11}', lambda x:x.group()[:3] + '****' + x.group()[-4:], tel)
print(result2)
