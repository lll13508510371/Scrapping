import requests

response = requests.get(url='https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76',
                        headers={...})

# requests.options()
"""
method: 请求方法 ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.

url: 请求的地址

headers: (可选的) 构建请求头字段的关键字参数, 需要构建成字典对象
cookies: (可选的) 构建cookies字段的关键字, 需要构建成字典对象
proxies: (可选的) ip代理的关键字参数, 需要构建成字典对象

params: (可选的) 查询参数, 地址中的查询参数可以通过这个关键字构建, 需要构建成字典对象
data: (可选的) 请求参数, 在请求的时候如果是post请求, 一般需要指定请求参数, 请求参数用此关键字指定, 需要构建成字典对象
json: (可选的) post请求提交的请求参数, 其数据是一个json数据格式, 那么需要用json指定

timeout: (可选的) 在请求的时候设置请求响应的时间, 一旦超过这个时间, 程序会报错
allow_redirects: (可选的) 是否允许重定向 300
verify: (可选的) http协议会有证书, 默认会验证网站证书  ca  ssl  , 证书验证的开关

files: (可选的) 操作文件上传下载
auth: (可选的) 权限认证
stream: (可选的) 数据是否是数据流传输
"""
