import base64
import requests
from constants import KUAI_PASSWORD, KUAI_USERNAME


def base64_api(img, typeid: int):
    """
    打码封装的函数
    :param img: 验证码路径
    :param typeid: 验证码类型
    :return:
    """
    with open(img, 'rb') as f:
        # 打开图片, 把图片转换成字符串形式
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()

    data = {"username": KUAI_USERNAME, "password": KUAI_PASSWORD, "typeid": typeid, "image": b64}

    result = requests.post("http://api.ttshitu.com/predict", json=data).json()
    if result['success']:
        return result["data"]["result"]
    else:
        # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
