from urllib import request, parse
import json

if __name__ == "__main__":
    req = request.Request('http://oauthuc-test.supergina.cn/user/sendCoupon')
    #phone = "13301165332"
    phone = "17710324432"
    sign = "y0oJmCP5ia0NNic4vzZr17aM97y7bcIxPZND6Saca7B+l0dZPSu4qLLBfzp0U5LV0vZImIh4GjpXmCN+qPKgw8LyHgyXU5EMsV28j5Twm04="
    #sign = "NCLQ49zd2Nuq6vZ9R9/F/YU0J7rXqQvoQeTufhY5R1h+Be4xQM1/2THd9zGx8syABfhoES2y7jp8N6dSiIIpPOXzmveEJAsaJSPE9JFcFFw\u003d"
    json_data = json.dumps({"phone": phone,
                            "requestId":"nsjdl",
                            "sign": sign,
                            "appkey":"f47967e9e88a3644",
                            "timestamp":1545209593})
    format_data = bytes(json_data, 'utf8')

    req.add_header('Content-Type', 'application/json')

    with request.urlopen(req, format_data) as f:
        result = f.read().decode('utf-8')
        print('response code:'+str(f.status)+',content'+f.reason)
        print(result)