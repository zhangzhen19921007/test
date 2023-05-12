import re
import requests
url='https://www.baidu.com/'
htmlUrl=requests.get(url)
#print(htmlUrl.text)
if htmlUrl.status_code==requests.codes.ok:
    partem=input("请输入你要搜索的字符串:")
    if partem  in htmlUrl.text:
        print("搜索%s 成功" %partem)
    else:
        print("搜索%s 失败" %partem)

    name=re.findall(partem,htmlUrl.text)
    if name!=None:
        print("%s 出现%d次"%(partem,len(name)))
    else:
        print("%s出现0次" %partem)
else:
    print("下载失败")