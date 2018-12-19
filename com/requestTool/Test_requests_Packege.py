import requests
import json

data = json.dumps({"phone":"17710324432","requestId":"nsjdl","sign":"NCLQ49zd2Nuq6vZ9R9/F/YU0J7rXqQvoQeTufhY5R1h+Be4xQM1/2THd9zGx8syABfhoES2y7jp8N6dSiIIpPOXzmveEJAsaJSPE9JFcFFw\u003d","appkey":"f47967e9e88a3644","timestamp":1545209593})

#r = requests.post('http://oauthuc-test.supergina.cn/user/sendCoupon', data={"phone": "17710324432", "requestId": "nsjdl", "sign": "NCLQ49zd2Nuq6vZ9R9/F/YU0J7rXqQvoQeTufhY5R1h+Be4xQM1/2THd9zGx8syABfhoES2y7jp8N6dSiIIpPOXzmveEJAsaJSPE9JFcFFw\\u003d", "appkey": "f47967e9e88a3644", "timestamp": 1545209593} )
r = requests.post('http://oauthuc-test.supergina.cn/user/sendCoupon',data)
print(r.json)