import os
path=os.path.abspath('map.txt') #返回绝对路径
print(path)

import socket
import requests
import json


h=open('E:\pycharm_len\py_learn\projects\JSON_map\map.txt','r')
appid = '565af5128afe62f23d115337cdfdfe38'
url='https://webapi.amap.com/maps?v=1.4.14&key='+ appid
response=requests.get(url)
print(response.text)
data= json.loads(response.text)

# jsonData= json.loads(response.text)
# jsonData = response.json()
# print(type(jsonData))

# city = jsonData.get('city')
# print(city)


# recordLine=h.readlines()
# for record in recordLine:
#     name,domin = record.split()
#     print(name)
#     print(domin)
#     ip = socket.gethostbyname(domin)
#     urlip='https://webapi.amap.com/maps?v=1.4.14&key='