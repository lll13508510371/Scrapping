import json

data = {
    'name': '青灯',
    'shares': 100,
    'price': 542.23
}

with open('data.json', mode='w', encoding='utf-8') as f:
    # ensure_ascii=False   不使用json的默认编码  默认为True unicode编码写入中文会得到unicode码
    result = json.dumps(data, ensure_ascii=False)
    f.write(result)