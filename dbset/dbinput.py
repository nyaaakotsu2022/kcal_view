import sqlite3

dbname = "dbset\dataset.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

#ans=cur.execute("SELECT protein, lipid, carbohydrate, sugar, dietaryfiber FROM nutrients WHERE dish_name = '{}'".format("ハンバーグ"))
#print(type(ans))
#ans=list(ans)
#print(ans)
#print(ans[0])
#print(ans[0][0])
#print(type(ans[0][0]))

cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ナポリタンスパゲティ', 16.8,  14.4,  75.8,  68.1,  7.8)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('そば', 4.8,  1.0,  26.0,  0.0,  2.9 )")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('焼き鳥', 7.53,  6.3,  1.73,  1.73,  0.0)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('しゃぶしゃぶ', 26.7,  29.2,  25.7,  19.4,  6.2)")     
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('カツ丼', 28.8,  37.1,  113.7,  105.8,  5.0)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('お好み焼き', 17.1,  25.7,  73.2,  69.1,  4.2)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('親子丼', 22.4,  8.5,  109.3,  104.3,  4.9)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('エクレア', 4.4,  11.2,  24.3,  23.6,  0.7)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ショートケーキ', 4.0,  16.1,  26.9,  26.3,  0.6)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('シュークリーム', 5.0,  16.2,  16.8,  16.5,  0.3)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('チョコレート', 0.3,  1.6,  2.8,  2.6,  0.2)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('クッキー', 0.7,  2.7,  6.0,  5.7,  0.3)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('バウムクーヘン', 5.6,  23.0,  41.0,  40.6,  0.4)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('チョコレートケーキ', 6.5,  19.0,  47.6,  45.2,  2.4)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('プリン', 5.3,  4.5,  14.0,  14.0,  0.0)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('モンブラン', 5.7,  21.4,  56.5,  53.9,  2.6)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ミルフィーユ', 4.93,  15.12,  33.63,  21.94, 0.83)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('タルト', 4.1,  12.3,  30.5,  29.1,  1.4)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('アップルパイ', 3.7,  16.0,  32.8,  31.6,  1)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('パフェ', 5.5,  19.2,  52.0,  50.5,  1.5)")
cur.execute("INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('アヒージョ', 19.61,  25.42,  1.72,  0.93,  0.25)")

# アップロード
conn.commit()

# 接続切断
cur.close()
conn.close()