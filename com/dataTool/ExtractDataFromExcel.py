import xlrd
import os
import sqlite3

if __name__ == "__main__":
    file_path = 'C:\\Users\\anve\\Desktop\\Data\\orderInfo_2019\\JAN\\'

    file_list = os.listdir(file_path)

    for file_name in file_list:
        print('开始对', file_name, '进行数据提取')
        wb = xlrd.open_workbook(file_path+file_name)
        sheet = wb.sheet_by_name('Export')
        row_num = sheet.nrows

        # 连接数据库
        conn = sqlite3.connect('C:\Document\BlackMagic.db')
        cursor = conn.cursor()
        row_list = []

        for row_position in range(3, row_num):
            userNum = sheet.cell(row_position, 0).value
            orderNum = sheet.cell(row_position, 1).value
            childOrderNum = sheet.cell(row_position, 2).value
            businessType = sheet.cell(row_position, 3).value
            orderStatus = sheet.cell(row_position, 4).value
            orderTitle = sheet.cell(row_position, 5).value
            orderTime = sheet.cell(row_position, 6).value
            amount = sheet.cell(row_position, 7).value
            sellPrice = sheet.cell(row_position, 9).value
            costValue = sheet.cell(row_position, 10).value
            costPrice = sheet.cell(row_position, 11).value
            payType = sheet.cell(row_position, 12).value
            gold = sheet.cell(row_position, 13).value
            couponValue = sheet.cell(row_position, 14).value
            couponId = sheet.cell(row_position, 22).value
            column_tuple = (userNum, orderNum, childOrderNum, businessType, orderStatus, orderTitle,
                            orderTime, amount, sellPrice, costPrice, payType, gold, couponValue, couponId)
            row_list.append(column_tuple)

        cursor.executemany('insert into orderInfo_2019'
                           '(userNum, orderNum, childOrderNum, businessType, orderStatus, orderTitle, orderTime, '
                           'amount, sellPrice,costPrice, payType, gold, couponValue, couponId) '
                           'values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row_list)
        conn.commit()
        cursor.close()
        conn.close()

        print(file_name, '提取完成')


