import hmac
import hashlib


def hmac_sha256(value, key):
    """
    hmacsha256加密
    return:加密结果转成16进制字符串形式
    """
    message = value.encode('utf-8')
    return hmac.new(key.encode('utf-8'), message, digestmod=hashlib.sha256).hexdigest()
