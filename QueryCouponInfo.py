import sqlite3


def fetch_coupon_data():
    pass


if __name__ == "__main__":
    conn = sqlite3.connect('C:\Document\BlackMagic.db')
    cursor = conn.cursor()

    cursor.execute("select * from coupon_info;")
    values = cursor.fetchall()
    print(values)
    print(type(values))
    print(values[0][4])
    print(type(values[0][4]))
    cursor.close()