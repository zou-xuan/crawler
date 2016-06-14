import requests
import sys
import re
reload(sys)

headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
html=requests.get('http://jp.tingroom.com/yuedu/yd300p/',headers=headers)
html.encoding='utf-8'
chinese = re.findall('color: #039;">(.*?)</a>',html.text,re.S)
for each in chinese:
    print each

