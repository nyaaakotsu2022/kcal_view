import sqlite3, math, numpy as np

def nutrients(foodname):
    dbname = "dbset\dataset.db"
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    ans = []

    tmp = list(cur.execute("SELECT protein, lipid, carbohydrate, sugar, dietaryfiber FROM nutrients WHERE dish_name = '{}'".format(foodname)))
    for i in range(len(tmp[0])): ans.append(tmp[0][i])
    ans = np.array(list(map(lambda x: math.ceil(x), ans)))
    conn.close()
    
    return ans