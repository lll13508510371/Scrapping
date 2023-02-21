import csv

list_dict = [{'first_name': 'Baked', 'last_name': 'Beans'},
             {'first_name': 'Lovely'},
             {'first_name': 'Wonderful', 'last_name': 'Spam'}]

with open('data2.csv', mode='a', encoding='utf-8', newline='') as f:

    """
    DictWriter 字典对象的操作
        第一个参数传文件对象
        第二个参数传列表, 列表里面指定字典的键
    """
    csv_write = csv.DictWriter(f, fieldnames=['first_name', 'last_name'])

    # 字典操作对象有提供表头的写入方法, 以指定的 fieldnames 作为表头
    # 表头指定的键不能错, 一旦错误程序就会报错 （因为写入的字典里面的键包含了这些字段, writeheader()是和之后writerow写入字典的键相关的）
    # e.g. ValueError: dict contains fields not in fieldnames: 'last_name' --> 字典包含了不在字段名中的字段：'last_name'
    # 键不能少
    csv_write.writeheader()  # 写入表头

    # 写数据
    for i in list_dict:
        csv_write.writerow(i)  # 循环写入一条一条字典
