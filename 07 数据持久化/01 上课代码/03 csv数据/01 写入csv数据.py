"""
csv数据, 每一行是一条数据(一串字符串）, 每一个数据中的字段用逗号<英文>隔开
"""
import csv  # 内置

ll = [[1, 2, 3, 4],
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [5, 6, 7, 8]]

# newline 指定新行
with open('data.csv', mode='a', encoding='utf-8', newline='') as f:
    '''当文件写入内容后有数据空行就用newline这个参数  -->  设置为newline=''  '''
    # 创建csv数据写入对象
    csv_write = csv.writer(f)  # 传入打开的文件对象
    for l in ll:
        # writerow(l)  传入列表或者元组, 整行写入数据
        csv_write.writerow(l)
