import execjs  # 安装模块名 pyexecjs  导入模块名  execjs

"""读取js代码"""
with open('/Users/lujinghan/PycharmProjects/Scrapping/15 js解密入门/01 上课代码/01 案例-百度翻译js解密案例/1.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()

"""编译js代码"""
compile_result = execjs.compile(js_code)
print(compile_result)

"""调用js函数"""
decrypt_result = compile_result.call('fanyi', '你好')
print(decrypt_result)
