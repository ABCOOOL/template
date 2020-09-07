import re

s = "curl 'https://u.faloo.com/regist/Login.aspx?txtUserID=15238332120&txtPwd=dfa33646584833b64c4172f9514b2782&txtPwd4temp=&verifyCode=zu2h&ts=1590543187&t=2&Eo181062=0527&backurl=https%3A%2F%2Fb.faloo.com%2Fl%2F0%2F1.html%3Ft%3D1%26k%3D%25u626b%25u5730%25u50e7' \
  -H 'Connection: keep-alive' \
  -H 'Pragma: no-cache' \
  -H 'Cache-Control: no-cache' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-User: ?1' \
  -H 'Sec-Fetch-Dest: document' \
  -H 'Referer: https://u.faloo.com/regist/login.aspx?backurl=https%3A%2F%2Fb.faloo.com%2Fl%2F0%2F1.html%3Ft%3D1%26k%3D%25u626b%25u5730%25u50e7' \
  -H 'Accept-Language: zh-CN,zh;q=0.9' \
  -H 'Cookie: curr_url=https%3A//b.faloo.com/l/0/1.html%3Ft%3D1%26k%3D%25u626b%25u5730%25u50e7; host4chongzhi=b.faloo.com' \
  --compressed"

temp = re.findall(r"'(.*?)'", s)
url = temp[0]
del temp[0]
result = {}
for i in temp:
    list = i.split(":", 1)
    result[list[0]] = list[1][1:]

print(result)
print(url)
