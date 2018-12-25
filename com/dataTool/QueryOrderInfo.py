from urllib import request, parse
import json

if __name__ == "__main__":
    url = 'http://172.16.10.90:8066/order/query/getOrderList'

    form_data = parse.urlencode({'businessType': -1,
                                 'state': -1,
                                 'pageIndex': 0,
                                 'pageSize': 30,
                                 'startTime': 'Thu Nov 01 2018 00:00:00 GMT+0800',
                                 'endTime': 'Sat Nov 03 2018 00:00:00 GMT+0800'}).encode('utf-8')

    req = request.Request(url)
    req.add_header('Cookie', 'JSESSIONID=24A6E6D22D6A005CBA267281333CBFB0')

    with request.urlopen(req, form_data) as f:
        json_order_info = f.read()

    order_info = json.loads(json_order_info)

    print(order_info)