import xlrd

if __name__ == "__main__":
    file = 'C:\\Users\\anve\\Desktop\\orderInfo\\NOV\\2018-11-01~2018-12-01_0.xlsx'

    wb = xlrd.open_workbook(file)

    sheet = wb.sheet_by_name('Export')

    # 取数据共有三种方式
    print(sheet.cell(3, 1).value)
    print(sheet.cell_value(3, 1))
    print(sheet.row(3)[1].value)

