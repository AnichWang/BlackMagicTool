import xlrd
import os
import sqlite3

if __name__ == "__main__":
    file_path = 'C:\\Users\\anve\\Desktop\\orderInfo\\JUL\\'

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

        for row_position in range(2, row_num):
            order_num = sheet.cell(row_position, 1).value
            business_type = sheet.cell(row_position, 3).value
            order_status = sheet.cell(row_position, 4).value
            order_time = sheet.cell(row_position, 6).value
            coupon_amount = sheet.cell(row_position, 14).value
            coupon_num = int(sheet.cell(row_position, 22).value)
            column_tuple = (order_num, business_type, order_status, order_time, coupon_amount, coupon_num)
            row_list.append(column_tuple)

        cursor.executemany('insert into orderInfo_JUL(orderNum,businessType,orderStatus,orderTime,couponAmount,couponNum) '
                           'values(?,?,?,?,?,?)', row_list)
        conn.commit()
        cursor.close()
        conn.close()

        print(file_name, '提取完成')


