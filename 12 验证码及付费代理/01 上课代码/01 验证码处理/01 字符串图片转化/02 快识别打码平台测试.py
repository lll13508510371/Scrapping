import base64
import requests
from constants import KUAI_USERNAME, KUAI_PASSWORD

'''
模拟表单提交 --> 通过post提交
'''
# 一、图片文字类型(默认 3 数英混合)：
# 1 : 纯数字
# 1001：纯数字2
# 2 : 纯英文
# 1002：纯英文2
# 3 : 数英混合
# 1003：数英混合2
#  4 : 闪动GIF
# 7 : 无感学习(独家)
# 11 : 计算题
# 1005:  快速计算题
# 16 : 汉字
# 32 : 通用文字识别(证件、单据)
# 66:  问答题
# 49 :recaptcha图片识别
# 二、图片旋转角度类型：
# 29 :  旋转类型
#
# 三、图片坐标点选类型：
# 19 :  1个坐标
# 20 :  3个坐标
# 21 :  3 ~ 5个坐标
# 22 :  5 ~ 8个坐标
# 27 :  1 ~ 4个坐标
# 48 : 轨迹类型
#
# 四、缺口识别
# 18 : 缺口识别（需要2张图 一张目标图一张缺口图）
# 33 : 单缺口识别（返回X轴坐标 只需要1张图）
# 五、拼图识别
# 53：拼图识别


# def base64_api(uname, pwd, img, typeid):
#     """
#     打码封装的函数
#     :param uname: 用户名
#     :param pwd: 密码
#     :param img: 验证码路径
#     :param typeid: 验证码类型
#     :return:
#     """
#     with open(img, 'rb') as f:
#         # 打开图片, 把图片转换成字符串形式
#         base64_data = base64.b64encode(f.read())
#         b64 = base64_data.decode()
#
#
#     data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
#
#     result = requests.post("http://api.ttshitu.com/predict", json=data).json()
#     if result['success']:
#         return result["data"]["result"]
#     else:
#         #！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
#         return result["message"]

def base64_api(img, typeid: int):
    """
    打码封装的函数
    :param img: 验证码路径
    :param typeid: 验证码类型
    :return:
    """
    with open(img, 'rb') as f:
        # 打开图片, 把图片转换成字符串形式 --> 很多打码平台都会这么做，因为字符串上传之后是无法被修改的
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()

    data = {"username": KUAI_USERNAME, "password": KUAI_PASSWORD, "typeid": typeid, "image": b64}

    result = requests.post("http://api.ttshitu.com/predict", json=data).json()
    if result['success']:
        return result["data"]["result"]
    else:
        # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]


if __name__ == "__main__":
    img_path = "/Users/lujinghan/PycharmProjects/Scrapping/12 验证码及付费代理/01 上课代码/01 验证码处理/01 字符串图片转化/yzm.png"
    result = base64_api(img=img_path, typeid=3)
    print(result)
'''
！！！官方http接口文档给的typeid是str类型，但官方文档中python使用传的是int
！！！我试了这里传str或者int都行，好像传参数python对 字符串类型的数字 和 整型的数字 没有严格区别
'''