#coding=utf-8
import requests
import loca
session=requests.session()
class Cms_api:
    def init(self):
        pass
    def cms_dl(self): #定义一个登录
        url = loca.htlc()+"/admin/user/login"
        print(url)
        data={
            "username":"admin168",
              "password":"admin"
        }
        headers ={"content-type":"application/json;charset=UTF-8"

        }
        # dl_rep=requests.post(url=url,data=data,json=headers)
        dl_rep =session.post(url=url,data=data,json=headers)
        print (dl_rep.text)#{“code”:“200”,“msg”:“登录成功！”,“model”:{}}
'''    def cms_yhgl(self): #定义一个用户管理接口
        uerlist_url=""
        uerlist_data={"startCreateDate": "","endCreateDate": "","searchValue": "","page": 1}
        uerlist_headers={"Content-Type": "application/x-www-form-urlencoded"}
        # uerlist_rep=requests.post(url=uerlist_url,data=uerlist_data,json=uerlist_headers)
        uerlist_rep=session.post(url=uerlist_url,data=uerlist_data,json=uerlist_headers)
        print (uerlist_rep.text) #{“code”:“200”,“msg”:“登录成功！”,“model”:{}}
'''

if __name__ == "main":
    a=Cms_api()
    a.cms_dl()
#    a.cms_yhgl()