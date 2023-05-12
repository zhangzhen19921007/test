import requests
url='http://www.baidu.com'
url1='http://aaa.baidu.com'
webSite=requests.get(url)
print(type(webSite))
print(webSite)

html1=requests.get(url1)
html1.raise_for_status()