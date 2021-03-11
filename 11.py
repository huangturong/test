import loca
import requests
url = loca.htlc()+"/admin/user/login"
print(url)
login_data = {
    'username':'admin168',
    "password":"admin"
                        }
login_headers = {"content-type":"application/json;charset=UTF-8"}
login_rep = requests.get(url=url,params=login_data,json=login_headers)
print(login_rep.text)