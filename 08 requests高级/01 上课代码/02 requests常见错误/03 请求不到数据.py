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
    'token': 'fbc312ca55885286c5109fa72ab968c6',
    'domain': 'common',
}

headers = {
    'Acs-Token': '1673251572751_1673272498736_g/6mSzLifSgrvS9aigTiHRYmDw36XKiG++ojk2cz7o0ahzFoX7PBhrB4Bky+B4nToDzvkZjYzvttA+ZuJnSV1r1yl2HfKkT0pnAtp6dMyT6h/qeEMafeAo/DP0tbXmpACcTs2Pxwf0ctFeHrfBNSbFS6yyfdJtNleJnQYkKLAoRfWTMHCiHUDh5uYGdV0ywNKNfhY4iSXZj8EjeK1gBhnCXC3vrIRqKIJwNrhGMQTOOLDNSS+QnyOTa+T1vI+gP+4e7y1CS5WsnIKVeBqqADjYcEWTIGjswBqcc2cvUIWnkgFvUoJbNQHghTPCZVajY5IQVXEa5Gkw0KdbjwZIfZhg==',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

cookies = {
    # 'BAIDUID': '963EC08DDD8CA5647A50D2ED99D0CCF2:SL=0:NR=10:FG=1',
    # 'BAIDUID_BFESS': '963EC08DDD8CA5647A50D2ED99D0CCF2:SL=0:NR=10:FG=1',
    'ZFY': 'YcKoCPvg:AtdhP20uu:B7X4npHvE5Hz0Xr1QnyDMiU178:C',
    'REALTIME_TRANS_SWITCH': '1',
    'SOUND_SPD_SWITCH': '1',
    'HISTORY_SWITCH': '1',
    'FANYI_WORD_SWITCH': '1',
    'SOUND_PREFER_SWITCH': '1',
    'PSTM': '1657895499',
    'BIDUPSID': 'D26C29435949C22624426B7C5A1F52F3',
    'BDUSS': 'UtTVEZhbDhBUFowNDJsZ25yNlotVVBpc29CaXlCbmlCTzJQRThBMmFxVkFNWEpqSVFBQUFBJCQAAAAAAAAAAAEAAAD9hL2nuti-~M~oMzEzNjQxOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAECkSmNApEpjN',
    'APPGUIDE_10_0_2': '1',
    'BDUSS_BFESS': 'UtTVEZhbDhBUFowNDJsZ25yNlotVVBpc29CaXlCbmlCTzJQRThBMmFxVkFNWEpqSVFBQUFBJCQAAAAAAAAAAAEAAAD9hL2nuti-~M~oMzEzNjQxOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAECkSmNApEpjN',
    'H_WISE_SIDS': '219946_232280_231979_222624_234085_234044_219623_232777_234572_238145_234020_230584_232357_131861_238265_239761_234208_114551_232244_219566_234296_234426_235174_235513_236239_238755_240305_237837_236538_236653_239947_240889_240939_240447_240466_240742_241208_241177_240782_241248_240597_241282_240649_241296_241328_241349_240035_238226_241460_216839_224267_227932_213356_229967_211986_239898_238444_215730_237893_214799_239101_238511_223064_219943_238507_213033_228650_229154_234781_204916_226628_241245_241565_238073_240905_230288_239492_232628_241757_241794_241153_234433_241815_241850_241864_240204_241970_240734_241780_232630_242055_242218_242224_242271_242379_242374_241601_242267_241892_241698_242473_241785_222222_237964_237821_241548_242489',
    'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
    'BA_HECTOR': '2g81808ka024240hak8ha1gc1hro5sp1l',
    'delPer': '0',
    'PSINO': '7',
    'H_PS_PSSID': '36558_37645_37559_37623_36920_37990_37799_37920_37874_38041_26350_37957_38009_37881',
    'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1670934026,1673272488',
    'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574': '1673272488',
    'ab_sr': "1.0.1_NjJkNTY0NTVhNTYxZDk1MDYyNjc1NTk0ZTQzNWM3YTNhMDFjZGI2ZTQ1NGY1MDFkZTkxNWY3ZDQzNThmYjVjMzk1MzUyMzEyZWYxZjI2MjE1NzlkMGZjNDg5YzgyNTBjODg1NGRhZjg3NGI1YTRiMDIwMmRmMmEzZDA3YjYzOGRjMTJiNzA3MDcxZjI2YjQ4ZmI0YTBkYjE3NzcyZTJkNDNhYTRjNzQ1MTI5OTVhZmE0MzI3NDkxZGNjNTQwZWVk'",
}

# cookies 可以提交cookies字段进行请求
response = requests.post(url=url, data=data, headers=headers, cookies=cookies)
pprint.pprint(response.json())


"""讨论: 请求不到数据的时候, 怎么办?"""

'''
反扒了 --> headers proxies cookies
'''

'''
参数 --> params 查询参数 data/json 请求参数
'''


'''
加密: 需要逆向解密
'''
