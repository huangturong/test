#coding = utf-8
import requests
url = "https://test.ouxuanzhineng.cn/stadium/coach/login"
data1 = {"account":"123456",
         "password":"123456",
         "brand_id":"63"
       #  "isSkipCheck": "ture"
         }
haeder1 = {"Content-Type":"	application/x-www-form-urlencoded"}
aa=requests.get(url=url,params = data1,json = haeder1)
print(aa.text)