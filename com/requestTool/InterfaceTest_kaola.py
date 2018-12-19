from urllib import request, parse

if __name__ == "__main__":
    req = request.Request('http://oauthuc-test.supergina.cn/user/sendCoupon')
    data = parse.urlencode([('phone', 17710324432), ('requestId', 'nsjdl'),
                            ('sign',
                             'NCLQ49zd2Nuq6vZ9R9/F/YU0J7rXqQvoQeTufhY5R1h+Be4xQM1/2THd9zGx8syABfhoES2y7jp8N6dSiIIpPOXzmveEJAsaJSPE9JFcFFw\u003d'),
                            ("appkey", 'f47967e9e88a3644'), ('timestamp', 1545209593)])
    req.add_header('Content-Type', 'application/json')

    with request.urlopen(req, data.encode('utf-8')) as f:
        result = f.read().decode('utf-8')
        print('response code:'+str(f.status)+',content'+f.reason)
        print(result)