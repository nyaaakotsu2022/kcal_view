import sqlite3

dbname = "dataset.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

ans=cur.execute("SELECT * FROM nutrients WHERE dish_name='ハンバーグ'")
print(type(ans))
ans=list(ans)

print(ans)
print(ans[0])
print(ans[0][1])
print(ans[0][2])
print(ans[0][6])
# アップロード
#conn.commit()

# 接続切断
cur.close()
conn.close()