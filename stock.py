import sqlite3


class StockDB:
    def __init__(self):
        # 建立連線
        self.conn = sqlite3.connect(r'C:\py\SQLiteDatabaseBrowserPortable\MyDb2.db')
        print('連線 STOCKDB.db 成功')
        # 取得游標
        self.c = self.conn.cursor()


    def 新增(self, 股票代號, 日期, 開盤):
        # 設定所要執行的 SQL 語句
        s = "INSERT INTO stock(股票代號, 日期, 開盤) VALUES({}, '{}', {})"
        s = s.format(股票代號, 日期, 開盤)
        print(s)
        # 嘗試處理可能發生的錯誤
        try:
            self.c.execute(s)
            # 提交 SQL 語句
            self.conn.commit()
            print('新增成功')
        except sqlite3.IntegrityError:  # PK ( Primary Key ) 重複
            print('新增失敗：', 股票代號, 日期)


    def close(self):
        # 關閉連線
        self.conn.close()
        print('連線關閉 成功')
