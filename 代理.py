import urllib.request
import random

url = 'http://www.whatismyip.com.tw'

#创建ip列表
iplist = ['218.249.45.162:35586','117.88.5.140:3000','183.167.217.152:63000']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
#为opener添加头部
opener.addheaders = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15')]

#
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
