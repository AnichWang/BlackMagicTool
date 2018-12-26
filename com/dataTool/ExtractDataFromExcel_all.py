import xlrd
import os
import sqlite3

"""
订单状态枚举：
    public static final int ORDER_STATUS_UNPAID = 10;  //待支付
    public static final int ORDER_STATUS_PAY_OVERTIME = 12; //支付超时
    public static final int ORDER_STATUS_CANCEL = 13; //订单取消
    public static final int ORDER_STATUS_IN_PAYMENT = 14; //付款中
    public static final int ORDER_STATUS_PAY_FAILURE = 15; //付款失败
    public static final int ORDER_STATUS_PAY_AUDIT_IN = 16; //付款审核中
    public static final int ORDER_STATUS_PAY_AUDIT_FAILURE = 17; //付款审核不通过
    public static final int ORDER_STATUS_PAY_SUCCESS = 20; //付款成功
    public static final int ORDER_STATUS_PAY_SUCCESS_OF_OVERTIME = 22; //付款成功,交易超时
    public static final int ORDER_STATUS_PAY_NO = 21; //无需付款
    public static final int ORDER_STATUS_COMPLETE = 30; //已完成
    public static final int ORDER_STATUS_WAIT_REFUND = 40; //待退款
    public static final int ORDER_STATUS_IN_REFUND = 41; //退款中
    public static final int ORDER_STATUS_REFUND_FAILURE = 42; //退款失败
    public static final int ORDER_STATUS_REFUND_SUCCESS = 50; //退款成功
    public static final int REFUND_STATUS_WAIT_REFUND = 40; //待退款
    public static final int REFUND_STATUS_IN_REFUND = 41; //退款中
    public static final int REFUND_STATUS_REFUND_FAILURE = 42; //退款失败
    public static final int REFUND_STATUS_REFUND_SUCCESS = 50; //退款成功

"""

if __name__ == "__main__":
    file_name = 'C:\\Users\\anve\\Desktop\\orderInfo\\export_2018-12-19_15-07-03_52_5384.xlsx'

    wb = xlrd.open_workbook(file_name)
    sheet = wb.sheet_by_name('export')
    row_num = sheet.nrows

    # 连接数据库
    conn = sqlite3.connect('C:\Document\BlackMagic.db')
    cursor = conn.cursor()
    row_list = []

    for row_position in range(1, row_num):
        order_num = sheet.cell(row_position, 1).value
        business_type = sheet.cell(row_position, 6).value
        order_status = sheet.cell(row_position, 9).value
        order_business_status = sheet.cell(row_position, 30).value
        order_time = sheet.cell(row_position, 27).value
        coupon_amount = float(sheet.cell(row_position, 14).value)
        coupon_num = int(sheet.cell(row_position, 15).value)
        column_tuple = (order_num, business_type, order_status, order_business_status, order_time, coupon_amount, coupon_num)
        row_list.append(column_tuple)

    cursor.executemany('insert into orderInfo_all(orderNum,businessType,orderStatus,orderBusinessStatus,orderTime,couponAmount,couponNum) '
                       'values(?,?,?,?,?,?,?)', row_list)
    conn.commit()
    cursor.close()
    conn.close()

    print(file_name, '提取完成')


