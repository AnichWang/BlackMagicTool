from urllib import request, parse
import json
import sqlite3
import time

"""
礼券数据截止到12月19日，共993条礼券数据
"""

def fetch_coupon_data(url, form_data):
    req = request.Request(url)
    # 添加登录状态cookie
    req.add_header('Cookie', '_ga=GA1.2.97311877.1544515217; connect.sid=s%3AfDszDdpN4qFDsyhXYvn69Ds_'
                             'UBYqK3B7.%2BBaJVb4S2QnBFSIeU1ZSPCLWqnlWyz3336JS5pDvtbI')
    with request.urlopen(req, form_data.encode('utf-8')) as f:
        couponInfo = f.read().decode('utf-8')
    return couponInfo


def database_tool(data_dic):
    conn = sqlite3.connect('C:\Document\BlackMagic.db')
    cursor = conn.cursor()

    column = list(data_dic.keys())
    print(column)

    coupon_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data_dic[column[1]]/1000))

    sql = 'insert into coupon_info (' + column[1] + ',' + column[0] + ',' + column[3] + ',' + column[4] + ',' + column[5] \
          + ',' + column[6] + ',' + column[8] + ', couponid)values( \'' + coupon_time + '\',' + str(data_dic[column[0]]) +\
          ',\'' + data_dic[column[3]] + '\',' + str(data_dic[column[4]]) + ',' + str(data_dic[column[5]]) + ',\'' + str(data_dic[column[6]]) +\
          '\',' + str(data_dic[column[8]]) + ',' + str(data_dic[column[2]]) + ');'

    print(sql)

    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()


def persistent_data(json_data):
    # 解析json数据
    format_data = json.loads(json_data)
    coupon_list = format_data['data']['list']
    for t in coupon_list:
        database_tool(t)


def parse_coupon_info(business):
    """
    :param business: 业务信息，
        业务字段(bid)枚举：
            电商:1，机票:2，火车票:3，酒店:4，特权卡:6，专车:7，门票:8
    :return:
    """
    pass


if __name__ == "__main__":

    fetch_url = 'http://cos.ultimavip.org/project/remote/coupon/%2F1.0%2Fcoupon%2Fcoupon%2FgetCoupons/false/form'

    for i in range(1, 101):
        print('开始获取第', i, '页数据')
        coupon_data = parse.urlencode([('pageNum', i)])
        result = fetch_coupon_data(fetch_url, coupon_data)
        persistent_data(result)
