# 制作実習II 第2期プログラム
# author 0J03003 石井悠輝
import streamlit as st
import numpy as np
from PIL import Image
import cv2
from streamlit_webrtc import webrtc_streamer
# import cnn_model
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import RMSprop


def main():
    block_list = ['カロリー']
    control_features = st.sidebar.selectbox('選択してください', block_list)
    st.header(f'{control_features}学習')

    if control_features == 'カロリー':
        padding_image()


def def_model(in_shape, nb_classes):
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3),
              activation="relu", input_shape=in_shape))
    model.add(Conv2D(32, kernel_size=(3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(32, kernel_size=(3, 3), activation="relu"))
    model.add(Conv2D(32, kernel_size=(3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes, activation="softmax"))
    return model


def get_model(in_shape, nb_classes):
    model = def_model(in_shape, nb_classes)
    model.compile(loss='categorical_crossentropy',
                  optimizer=RMSprop(), metrics=['accuracy'])
    return model


target_image = "test-omuraice.jpg"
im_rows = 128  # 変更
im_cols = 128  # 変更
im_color = 3
in_shape = (im_rows, im_cols, im_color)
nb_classes = 3
Labels = ["オムライス", "ローストビーフ"]
Calories = [588, 39]  # 記入

model = get_model(in_shape, nb_classes)
# model=cnn_model.get_model(in_shape,nb_classes)
model.load_weights('photos-model-light.hdf5')


def check_photo(x):
    plt.show()
    x = x.reshape(-1, im_rows, im_cols, im_color)
    x = x/255

    pre = model.predict([x])[0]
    idx = pre.argmax()
    per = int(pre[idx]*100)
    return (idx, per)


def check_photo_str(path):
    idx, per = check_photo(path)
    print("この写真は、", Labels[idx], "で、カロリーは", Calories[idx], "kcal")
    print("可能性は、", per, "%")


def padding_image():  # 水増し
    imgfile = st.file_uploader("ファイルアップロード", type='jpg')
    if imgfile is not None:
        image = Image.open(imgfile)
        st.image(image, caption='サムネイル画像', use_column_width=True)
        img_cv2 = np.asarray(image)  # pilからcv2
        check_photo_str(img_cv2)
    # check_photo_str('test-salad.jpg')


if __name__ == "__main__":
    main()
