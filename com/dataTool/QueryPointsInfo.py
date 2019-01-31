from urllib import request, parse
import json
import sqlite3
import time

"""
获取自由币单日数据脚本
"""


def fetch_data(url):
    req = request.Request(url)
    # 添加cookie信息
    req.add_header('cookie', '_ga=GA1.2.97311877.1544515217; JSESSIONID=3D2979DA8471BD0786FC7F1BBD5E1712')
    # 获取连接
    with request.urlopen(req) as f:
        pointsInfo = f.read().decode('utf-8')
    return pointsInfo


def persistent_data(json_data):
    # 解析json数据
    format_data = json.loads(json_data)
    points_list = format_data['data']
    for t in points_list:
        database_tool(t)


def database_tool(data_dic):
    conn = sqlite3.connect('C:\Document\BlackMagic.db')
    cursor = conn.cursor()

    column = list(data_dic.keys())
    print(column)


    sql = 'insert into points_info (' + column[1] + ',' + column[2] + ',' + column[3] + ',' + column[4] + ',' + column[5] \
          + ',' + column[6] + ',' + column[7] + ', ' + column[8] + ',' + column[9] + ',' + column[10] +')values( \''+\
          data_dic[column[1]] + '\',\'' +str(data_dic[column[2]])+ '\',\'' +str(data_dic[column[3]])+ '\',\'' +str(data_dic[column[4]])+ '\',\'' +str(data_dic[column[5]])+ '\',\'' +str(data_dic[column[6]]) +'\',\'' +str(data_dic[column[7]]) +'\',\'' +str(data_dic[column[8]]) +'\',\'' +str(data_dic[column[9]]) +'\',\'' +str(data_dic[column[10]])+'\');'

    print(sql)

    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    start = 0
    for pageNum in range(27,28):
        fetch_url = 'http://gold.ultimavip.org/statistics/select?draw=' + str(pageNum) \
                    + '&columns%5B0%5D%5Bdata%5D=subBusiTypeStr&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable' \
                      '%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0' \
                      '%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=dateStr&columns%5B1%5D%5Bname%5D=&col' \
                      'umns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%' \
                      '5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=send&columns%5' \
                      'B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&column' \
                      's%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bd' \
                      'ata%5D=used&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borde' \
                      'rable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=fals' \
                      'e&columns%5B4%5D%5Bdata%5D=refund&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&' \
                      'columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsear' \
                      'ch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=cancel&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%' \
                      '5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&' \
                      'columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=totalSend&columns%5B6%5D%5B' \
                      'name%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%' \
                      '5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=tot' \
                      'alUse&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%' \
                      '5D=false&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&colu' \
                      'mns%5B8%5D%5Bdata%5D=radioStr&columns%5B8%5D%5Bname%5D=&columns%5B8%5D%5Bsearchable%5D=true&colum' \
                      'ns%5B8%5D%5Borderable%5D=false&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D' \
                      '%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=&columns%5B9%5D%5Bname%5D=&columns%5B9%5D%5Bsearchabl' \
                      'e%5D=true&columns%5B9%5D%5Borderable%5D=false&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9' \
                      '%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start='+ str(start) +'&le' \
                      'ngth=10&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1548928800495'
        print('开始获取第', pageNum, '页数据')
        result = fetch_data(fetch_url)
        persistent_data(result)
        start += 10
