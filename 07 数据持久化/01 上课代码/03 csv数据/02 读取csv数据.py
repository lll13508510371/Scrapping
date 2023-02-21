"""
csv数据, 每一行是一条数据, 每一个数据中的字段用逗号<英文>隔开
"""
import csv  # 内置

# newline 指定新行
with open('data.csv', mode='r', encoding='utf-8', newline='') as f:

    # 创建csv数据读取对象
    csv_read = csv.reader(f)  # 传入打开的文件对象
    print(csv_read)  # csv_read是一个对象, 可以通过遍历的方式取值

    for i in csv_read:
        print(i)


"""以上csv操作的是 列表或者元组 """
