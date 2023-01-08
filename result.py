import math
import keras
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from dbset.nutrients import nutrients
from PIL import Image
from collections import defaultdict
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten
from keras.layers import Conv2D,MaxPooling2D
from keras.optimizers import RMSprop

im_rows = 128 #変更
im_cols = 128 #変更
im_color = 3
in_shape = (im_rows, im_cols, im_color)
nb_classes = 8

LABELS=["モンブラン", "パウンドケーキ", "ロールケーキ", "ショートケーキ", "シュークリーム", "ティラミス", "チーズケーキ", "チョコケーキ"]
VALUE = {"1人前" : 1, "2人前" : 2, "3人前" : 3, "4人前" : 4}
CALORIES=[358, 207, 251, 366, 228, 381, 300, 370]#記入


def def_model(in_shape, nb_classes):
    model = Sequential()
    model.add(Conv2D(64, kernel_size=(3, 3), activation="relu", input_shape=in_shape))
    model.add(Conv2D(64, kernel_size=(3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))
    
    model.add(Conv2D(64, kernel_size=(3, 3), activation="relu"))
    model.add(Conv2D(64, kernel_size=(3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(512, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes, activation="softmax"))
    return model

def get_model(in_shape,nb_classes):
    model = def_model(in_shape, nb_classes)
    model.compile(loss='categorical_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])
    return model

model = get_model(in_shape, nb_classes)
model.load_weights('dezato2_photos-model.hdf5')


def check_photo(path):
    img = Image.open(path)
    img = img.convert("RGB")
    img = img.resize((im_cols, im_rows))
    plt.show()
    x = np.asarray(img)
    x = x.reshape(-1, im_rows, im_cols, im_color)
    x = x/255

    pre = model.predict([x])[0]
    idx = pre.argmax()
    per = int(pre[idx] * 100)
    return (idx, per)

def show_chart(foodvalue):
    values = nutrients(foodvalue)
    labels = ["たんぱく質", "脂質", "炭水化物", "糖質", "食物繊維"]
    # 多角形を閉じるためにデータの最後に最初の値を追加する。
    radar_values = np.concatenate([values, [values[0]]])
    # プロットする角度を生成する。
    angles = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)
    # メモリ軸の生成
    rgrids = [0, 20, 40, 60, 80, 100]


    fig = plt.figure(facecolor="w")
    # 極座標でaxを作成
    ax = fig.add_subplot(1, 1, 1, polar=True)
    # レーダーチャートの線を引く
    ax.plot(angles, radar_values)
    #　レーダーチャートの内側を塗りつぶす
    ax.fill(angles, radar_values, alpha=0.2)
    # 項目ラベルの表示
    ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels, fontname="MS Gothic")
    # 円形の目盛線を消す
    ax.set_rgrids([])
    # 一番外側の円を消す
    ax.spines['polar'].set_visible(False)
    # 始点を上(北)に変更
    ax.set_theta_zero_location("N")
    # 時計回りに変更(デフォルトの逆回り)
    ax.set_theta_direction(-1)

    # 多角形の目盛線を引く
    for grid_value in rgrids:
        grid_values = [grid_value] * (len(labels)+1)
        ax.plot(angles, grid_values, color="gray",  linewidth=0.5)

    # メモリの値を表示する
    for t in rgrids:
        # xが偏角、yが絶対値でテキストの表示場所が指定される
        ax.text(x=0, y=t, s=t)

    # rの範囲を指定
    ax.set_rlim([min(rgrids), max(rgrids)])

    ax.set_title("{}1個あたりの栄養素".format(foodvalue), pad=20, fontname="MS Gothic")
    st.pyplot(fig)


def check_photo_str(path, number):
    idx, per = check_photo(path)
    st.text("この写真は、{}で、カロリーは{}kcal".format(LABELS[idx], CALORIES[idx]*VALUE[number]))
    st.text("可能性は、{}%".format(per))
    show_chart(LABELS[idx])
