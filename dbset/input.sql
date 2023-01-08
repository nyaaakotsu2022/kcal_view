-- テーブル
CREATE TABLE nutrients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dish_name TEXT UNIQUE NOT NULL,
    protein REAL NOT NULL,
    lipid REAL NOT NULL,
    carbohydrate REAL NOT NULL,
    sugar REAL NOT NULL,
    dietaryfiber REAL NOT NULL
);

-- 追加したもの
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ナポリタンスパゲッティ', 16.0, 14.4, 75.8, 68.1, 7.8);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ハンバーグ', 18.6, 21.3, 14.6, 13.6, 1.0);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ステーキ', 18, 28.51, 0.56, 0.56, 0.0);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('オムライス', 28.83, 29.66, 107.74, 105.93, 1.81);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('カレーライス', 21.03, 26.51, 129.17, 124.5, 4.67);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ピザ', 39.73, 35.72, 97.9, 90.64, 7.26);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('グラタン', 18.4, 23.3, 35.8, 33.0, 2.8);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('エビフライ', 4.1, 2.1, 2.4, 2.3, 0.1);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ローストビーフ', 8.68, 4.68, 0.36, 0.36, 0.0);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('鶏の唐揚げ', 19.3, 16.2, 12.5, 11.8, 0.8);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ドリア', 21.85, 26.95, 60.52, 59.32, 1.2);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('コーンポタージュ', 4.0, 18.4, 18, 16.4, 1.7);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('カルボナーラ', 22.5, 48.9, 61.3, 56.9, 4.3);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('コロッケ', 4.8, 12.3, 18.3, 15.5, 2.8);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('メンチカツ', 19.2, 31.5, 15.3, 14.3, 1.0);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ビーフシチュー', 20.5, 66.9, 30.3, 26.4, 2.6);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ハヤシライス', 31.82, 45.8, 122.1, 117.44, 4.66);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('たらこパスタ', 32.19, 33.58, 72, 67.88, 4.12);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('オムレツ', 23.08, 22.44, 11.16, 22.44, 1.18);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('スクランブルエッグ', 15.84, 23.24, 2.02, 2.02, 0.0);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('チキンソテー', 24.6, 41.16, 1.14, 0.96, 0.18);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ペペロンチーノ', 10.2, 14.0, 62.2, 55.5, 6.7);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ビーフストロガノフ', 25.0, 37.6, 17.1, 15.6, 1.6);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ポテトサラダ', 2.8, 12.3, 12.7, 10.2, 2.5);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ポークソテー', 21.98, 28.15, 10.43, 9.14, 1.29);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ハムエッグ', 10.46, 11.08, 0.96, 0.96, 0.0);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ピラフ', 2.8, 2.2, 29.8, 28.6, 1.2);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('チキンカツ', 19.9, 12.2, 8.4, 8.0, 0.4);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('クリームシチュー', 16.1, 27.9, 22.4, 18.5, 3.9);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ロールキャベツ', 11.15, 7.98, 12.07, 9.98, 2.09);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('餃子', 14.6, 21.0, 28.0, 25.3, 2.8);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('エビチリ', 12.8, 13.2, 10.5, 13.2, 1.2);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('麻婆豆腐', 18.6, 22.9, 10.1, 7.1, 3.0);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('炒飯', 11.1, 27.4, 95.6, 91.2, 4.4);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('小籠包', 10.6, 10.1, 39.0, 37.8, 1.3);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('春巻き', 8.7, 24.2, 33.7, 29.8, 3.9);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ごま団子', 1.8, 5.0, 24.8, 23.9, 0.8);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('油淋鶏', 45.72, 68.83, 30.92, 30.37, 0.55);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ラーメン', 20.4, 8.8, 70.5, 63.7, 7.1);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('肉まん・豚まん', 8.3, 4.4, 41.2, 38.2, 3.0);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('杏仁豆腐', 1.9, 1.9, 40.5, 39.4, 1.1);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('酢豚', 12.9, 33.7, 38.9, 36.2, 2.7);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('チンジャオロースー', 15.6, 26.7, 13.4, 9.8, 3.6);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('シュウマイ', 14.4, 18.1, 14.4, 13.5, 0.9);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('冷やし中華', 20.9, 11.8, 74.6, 67.1, 7.6);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('天津飯', 14.3, 13.9, 99.2, 94.0, 5.2);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('八宝菜', 11.1, 15.4, 15.2, 11.6, 3.8);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('レバニラ炒め', 14.4, 12.8, 16.6, 15.3, 1.3);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('タンタンメン', 34.34, 35.12, 82.52, 74.3, 8.22);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ホイコーロウ', 7.45, 19.16, 9, 7.13, 1.87);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('寿司', 19.3, 4.5, 45.5, 42.7, 2.2);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('天ぷら', 11.53, 9.32, 8.46, 7.64, 0.82);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('とんかつ', 21.4, 36.33, 8.57, 8.18, 0.39);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('うどん', 10.4, 1.0, 69.0, 63.2, 4.7);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('刺身', 126.86, 35.93, 3.38, 3.38, 0.0);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('肉じゃが', 5.28, 7.33, 19.35, 18.03, 1.32);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('すき焼き', 27.37, 25.32, 31.05, 25.32, 5.73);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('焼肉', 27.4, 79.6, 18.1, 14.7, 3.4);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('豚汁', 5.54, 8.4, 5.26, 3.96, 1.3);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('うな重', 41.78, 32.26, 110.54, 109.76, 0.78);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('味噌汁', 1.63, 0.36, 5.02, 4.35, 0.67);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('たこ焼き', 12.57, 8.19, 44.98, 43.14, 1.84);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('焼きそば', 15.28, 13.48, 67.95, 63.57, 4.38);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('海鮮丼', 52.8, 16.05, 101.4, 99.9, 1.5);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('お茶漬け', 6.95, 1.35, 56.63, 55.86, 0.77);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('だし巻き', 7.84, 6.3, 0.35, 0.35, 0.0);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('しょうが焼き', 20.82, 25.22, 8.06, 7.98, 0.08);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('おでん', 46.49, 30.94, 41.28, 36, 5.28);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('茶碗蒸し', 10.23, 7.01, 7.04, 6.45, 0.59);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('さばのみそ煮', 32.6, 27.8, 13.2, 13.2, 0.0);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('納豆', 8.25, 5, 6.05, 2.7, 3.35);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('塩鮭', 15.5, 7.8, 0.1, 0.1, 0.0);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ロールケーキ', 4.1, 9.3, 20.9, 20.7, 0.2);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('マカロン', 1.5, 2.8, 10.7, 10.2, 0.5);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ティラミス', 5.6, 27.8, 40.1, 40.0, 0.5);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('フィナンシェ', 2.2, 12.8, 15.1, 14.4, 0.7);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('クレープ', 8.7, 23.5, 46.2, 44.9, 1.3);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('マドレーヌ', 1.3, 5.8, 12.0, 11.8, 0.2);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('チーズケーキ', 4.4, 21.0, 12.8, 12.8, 0.1);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ドーナツ', 4.3, 7.3, 39.1, 38.4, 0.8);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('パウンドケーキ', 2.0, 8.8, 22.0, 21.6, 0.5);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('カップケーキ', 3.7, 12.0, 28.8, 28.3, 0.5);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('クレーム・ブリュレ', 3.4, 21.8, 9.8, 9.8, 0.0);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('スコーン', 2.0, 4.6, 16.2, 15.8, 0.5);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('いちご大福', 2.49, 0.33, 33.1, 31.68, 1.42);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('わらび餅', 2.8, 2.0, 37.8, 36.3, 1.5);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('みたらし団子', 2.48, 0.32, 36.16, 35.92, 0.24);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('どら焼き', 4.5, 2.1, 43.4, 42.0, 1.4);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('たい焼き', 4.5, 1.0, 53.1, 51.6, 1.5);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('カステラ', 3.3, 2.2, 30.9, 30.7, 0.3);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('三色団子', 3.1, 0.3, 43.0, 40.9, 2.1);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('大福', 2.9, 0.2, 37.2, 36.0, 1.3);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('あんみつ', 2.3, 0.1, 65.0, 61.4, 3.5);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('おはぎ', 2.7, 0.2, 33.6, 31.6, 2.0);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ようかん', 1.9, 0.1, 41.9, 40.1, 1.9);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('焼き魚', 17.8, 3.5, 0.1, 0.1, 0.0);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ハンバーガー', 10.9, 10.9, 35.8, 33.9, 1.9);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('ビビンバ', 14.0, 16.2, 107.2, 98.5, 8.8);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('もんじゃ焼き', 8.8, 34.9, 37.5, 34.8, 3.0);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('サンドイッチ', 11.2, 22.4, 24.9, 22.7, 2.2);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('おにぎり', 2.2, 0.2, 40.8, 39.2, 1.7);
INSERT INTO nutrients(dish_name, protein, lipid, carbohydrate, sugar, dietaryfiber) VALUES ('白米', 2.5, 0.3, 37.1, 35.6, 1.5);