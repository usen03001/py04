from py03.lab13.stock import StockDB
import DownloadStock


db = StockDB()  # 建立物件 __init__()

代號 = 2880  #2330
所有記錄 = DownloadStock.取得所有記錄(代號)

for a in 所有記錄:
   print(a)
   db.新增(代號,
         a[0].replace('/', '-'),
         float(a[1]))

db.close()
