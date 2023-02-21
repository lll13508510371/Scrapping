import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

with open('data.json', mode='w', encoding='utf-8') as f:
    f.write(json.dumps(data))

with open('data.json', mode='r', encoding='utf-8') as f:
    print(f.read())

