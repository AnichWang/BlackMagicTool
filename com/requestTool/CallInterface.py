from urllib import request, parse

if __name__ == "__main__":
    req = request.Request('http://oauthuc-test.supergina.cn/user/sendCoupon')
    data = parse.urlencode([('phone', '17710324432'), ('requestId', '11111'),
                            ('sign',
                             'Vd1uBSroocp0NLqY2ZFshyi5peWtZ4uJAXQl+LC6DhoxyDGwIC2iepZtmVRAdkQfYGe9edfb7SLrlNGJ+r/iypfUNmlADbAPpuEaJSI3SQ0FdLJAG2CDDFBUGo70cK6W'),
                            ("appkey", 'f47967e9e88a3644'), ('timestamp', '1545199854')])
    req.add_header('Content-Type', 'application/json')

    with request.urlopen(req, data.encode('utf-8')) as f:
        result = f.read().decode('utf-8')
        print(f.status, f.reason)
        print(result)