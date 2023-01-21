import sqlite3

dbname = "dbset\dataset.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# L = ["protein", "lipid", "carbohydrate", "sugar", "dietaryfiber"]
# for i in L:
#     cur.execute("UPDATE nutrients SET {}=100 WHERE {}>=100".format(i, i))

#ans=cur.execute("SELECT protein, lipid, carbohydrate, sugar, dietaryfiber FROM nutrients WHERE dish_name = '{}'".format("ハンバーグ"))
# print(type(ans))
# ans=list(ans)
# print(ans)
# print(ans[0])
# print(ans[0][0])
# print(type(ans[0][0]))

# print(list(cur.execute("SELECT * FROM nutrients WHERE dish_name = 'カレーライス'")))

# アップロード
# conn.commit()

# 接続切断
cur.close()
conn.close()
