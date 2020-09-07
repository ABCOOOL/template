import base64
from Crypto.Cipher import AES


# 密钥（key）, 密斯偏移量（iv） CBC模式加密

def AES_Encrypt(data):
    key = '021b587ca2e41588'
    iv = 'qwertyuiopasdfgh'
    # PKCS7Padding
    pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    data = pad(data)
    # 以CBC模式加密，ECB模式则没有iv参数
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, iv.encode('utf8'))
    # 加密后得到的是bytes类型的数据
    encryptedbytes = cipher.encrypt(data.encode('utf8'))

    # 使用Base64进行编码,返回byte字符串
    # encodestrs = base64.b64encode(encryptedbytes)
    # enctext = encodestrs.decode('utf8')
    # 对byte字符串按utf-8进行解码
    # return enctext

    # 以hex形式输出
    return encryptedbytes.hex()


def AES_Decrypt(data):
    vi = 'qwertyuiopasdfgh'
    key = '021b587ca2e41588'

    # data = data.encode('utf8')
    # 将加密数据转换位bytes类型数据
    # encodebytes = base64.decodebytes(data)

    encodebytes =bytes.fromhex(data)

    # 以CBC模式解密，ECB同上加密
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    text_decrypted = cipher.decrypt(encodebytes)
    unpad = lambda s: s[0:-s[-1]]
    text_decrypted = unpad(text_decrypted)
    # 去补位
    text_decrypted = text_decrypted.decode('utf8')
    return text_decrypted


key = '021b587ca2e41588'
data = r'{"t":1591677393528,"token":"20a339d5e6b24d05b775ccb245ac0bfd","width":360,"height":222,"clientVersion":1,"dfp":"a062738f4918d74138ae4823c01ac130198afb37aed5a0d16ae3f1cf481b88dda0","extend":"{\"dfp\":\"a062738f4918d74138ae4823c01ac130198afb37aed5a0d16ae3f1cf481b88dda0\",\"ptid\":\"01010021010000000000\",\"agentType\":1,\"deviceId\":\"18eaa795d4cb9d3a6676e4be6e9a701c\",\"areaCode\":\"86\"}"}'
enctext = AES_Encrypt(data)
print(enctext)
text_decrypted = AES_Decrypt(enctext)
print(text_decrypted)