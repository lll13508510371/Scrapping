import pprint

import requests

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'

data = {
    'from': 'zh',
    'to': 'en',
    'query': '你好',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '232427.485594',
    'token': 'c711c98a2a66ea875f14117cde6fcce8',
    'domain': 'common',
}

headers = {
    'Acs-Token': '1676970007776_1676984857902_m+HVNRlgvQNNM+B1S+cYUdXdp6RxSzte02NvimUHY05MygT6QpR1ZAFbwjCjcaAyTRESSipGD9j5/fqFqj2BBN2in8dHXszfFIifI8SiKyb6CSXS7JY5z1TjDFO1SYpeLNUMvB1WhCn2ci0c+pLUeCjhsYLCEJG7rysD39itl5M7w6xy17nmd/4RQ45+Jnn+k79BJI2NNk06jHgDfTprXWXibAVj16KI7NMACQ7GVnJYBcC2Yy5Q/Ax8cjhNPuJN+AeQkGoN1NiOUTbP4Vo3D5mQrNjafHJhRdVZ9YUdEXi4rBAbId2PCb0LvVbn3o5gbR8xUS/u4V2pM2Z3B/8uBSTVJXSFhuOM+n9gLfbOGzk=',
    'Cookie': 'BIDUPSID=9B79289047C65A05233432B75D0321A6; PSTM=1673192806; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=lMY3JBMWJPSUs3TTBHRWlGNGdvRWl-ajdRMmFKWVF-SFk5elZtOXdhSGRUZXBqSVFBQUFBJCQAAAAAAAAAAAEAAADtJ3JdVGhlc2t5saaxpgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN3AwmPdwMJjUn; __bid_n=185c0764e4f4f0dfed4207; sensorsdata2015jssdkcross={"distinct_id":"185fc89f5411045-0e498f94cc1153-16525635-1296000-185fc89f5421c94","first_id":"","props":{},"$device_id":"185fc89f5411045-0e498f94cc1153-16525635-1296000-185fc89f5421c94"}; BAIDUID_BFESS=C36BFB04A6FED70ADDB40ECDBFF4E601:FG=1; BDUSS_BFESS=lMY3JBMWJPSUs3TTBHRWlGNGdvRWl-ajdRMmFKWVF-SFk5elZtOXdhSGRUZXBqSVFBQUFBJCQAAAAAAAAAAAEAAADtJ3JdVGhlc2t5saaxpgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN3AwmPdwMJjUn; ZFY=n8qsXvopMbBQYGyR1YbjWIjxFa:AbSn2VjKG7E87KupA:C; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1676119881,1676609850,1676624208,1676632619; FPTOKEN=NJmJQaypIDkkG9YMZwbViALL6eSqj5DWsGsW3su1iosOlYdbDJwjO4BAa6QP6ltc+lTOEcemqlJ1ssAyjJT4yNuO/mSVfSR6nBRC4EZdkaiHaO3D7PagIW3/t/MyrEIOOMcr8Rvgq+YEQPfmG8Wg9SKovDAxeI6m2lbL/3w/os8F3B2+wgOtvjNd2xYapgAWi7THgjiiFYfKcCNjW25N5PGRd6rD3OBA7/ZVCr/d0Rw0ITNKRxVpuIht3Ce9IUzv04olmczokb90/7+buBcbTl/+SqjMWT0XRb+Ds7IDSwJgUzCQMxGEaGKWNGLd+YG8h3opITDF1jaVBfyrepJ2zShesB9P3XZPJEQFxlAaQ2o7tSdr7Hc+hnETRnAUqYU2RZSs1XUjQjdjqsYBKIBLcQ==|2KQWPWzR/S9HTZ3EqfuCxo8KZKkSVA3kEq86RlO3Mgs=|10|d5aa6076175ee5ac01b725164a96e198; RT="z=1&dm=baidu.com&si=e65f18d5-eab2-4870-83ef-180c44b49a10&ss=lecsds40&sl=3&tt=2j8&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=8ik&ul=bea&hd=bf2"; ab_sr=1.0.1_NDliZjExNTY4OTM5ZWEyMGQzZmE5NzRjNWRiNzM2ZjdjNTFiNzMxNzJmZWVlZGE4M2RhYTBmYjg4NWUxMTI2N2RiZjFmMThhYTdmM2Y5YzI4YmRlNjE0YjVlNzZlZmE4NzQ4ZWZhZTUxMjc4ODlkZDFhYmZmYTg0YjdiNjQ2OGFlMGZhNzg4ODE5NDI4MWM4Mjk5ZDY4NjkwMTk4YmE0YTczMzhhYjliNjU1ZjgwMmQyNTE5ODE4ZDgxNGNjZTU3; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1676984857',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

response = requests.post(url=url, data=data, headers=headers)
response.encoding = response.apparent_encoding
pprint.pprint(response.json())
# print(response.text)