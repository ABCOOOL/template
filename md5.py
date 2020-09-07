import hashlib

target_string = "1234512345S^H8"

#md5方法需传入二进制，用encode()默认以utf-8形式编码
after_md5 = hashlib.md5(target_string.encode())

#hash相关算法一般以16进制输出
print(after_md5.hexdigest())
