import requests
url='http://www.crowdfunder.com/browse/deals&template=false'
data={
    'entity_only':'true',
    'page':2
}
html_post=requests.post(url,data=data)
#再用正则来解析