import re

curl = "curl 'https://passport.iqiyi.com/apis/reglogin/login.action' \
  -H 'Connection: keep-alive' \
  -H 'Pragma: no-cache' \
  -H 'Cache-Control: no-cache' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Origin: https://www.iqiyi.com' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://www.iqiyi.com/iframe/loginreg?ver=1' \
  -H 'Accept-Language: zh-CN,zh;q=0.9' \
  -H 'Cookie: JSESSIONID=B88E6A811E47F3F0522A23E970D23C34; QC006=nhu5d4xheqhht86tmyv4kpmr; QC005=355846b22559b49468e9cc1c51c19dc5; QC173=0; QC007=DIRECT; QC008=1591086782.1591086782.1591086782.1; nu=0; QC010=198868011; P00004=.1591086782.5767fa99d0; QC160=%7B%22u%22%3A%22%22%2C%22lang%22%3A%22%22%2C%22local%22%3A%7B%22name%22%3A%22%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%22%2C%22init%22%3A%22Z%22%2C%22rcode%22%3A48%2C%22acode%22%3A86%7D%7D; __dfp=a0ce8b12003d7c4b5b89fc1cd9015878f1f0b3b24650fca4622d1d2399d4c85f6a@1592290952173@1590994953173' \
  --data-raw 'email=15517328931&fromSDK=1&sdk_version=1.0.0&passwd=028d4c1305a6a9baaed3947bade99d4205337fdcabef59b6f7b073f11a220339768b359fd8c8999b934fbf008ee75b9435f23741d3e9251cab8358de6cfde4ac&agenttype=1&__NEW=1&checkExist=1&lang=&ptid=01010021010000000000&nr=2&verifyPhone=1&area_code=86&env_token=9593ffb55dca482598946c09b8439900&dfp=a0ce8b12003d7c4b5b89fc1cd9015878f1f0b3b24650fca4622d1d2399d4c85f6a' \
  --compressed"

data = re.findall("--data-raw '(.*?)'", curl)[0]
data_dic = {}
for i in data.split("&"):
    data_dic[i.split("=", 1)[0]] = i.split("=", 1)[1]
print(data_dic)