import keras
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import RMSprop

LABELS = ["お好み焼き", "ラーメン", "そば", "すき焼き", "しゃぶしゃぶ", "たこ焼き", "天ぷら", "うどん", "焼きそば"]
CALORIES = [545, 403, 296, 490, 445, 317, 167, 242, 469]
VALUE = {"1人前": 1, "2人前": 2, "3人前": 3, "4人前": 4}
BASEDIR = os.path.dirname(os.path.abspath(__file__))

def def_model(in_shape, nb_classes):
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation="relu", input_shape=in_shape))
    model.add(Conv2D(32, kernel_size=(3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))

    model.add(Conv2D(64, kernel_size=(3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(512, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes, activation="softmax"))
    return model


def get_model(in_shape, nb_classes):
    model = def_model(in_shape, nb_classes)
    model.compile(loss='categorical_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])
    return model


im_rows = 64
im_cols = 64
im_color = 3
in_shape = (im_rows, im_cols, im_color)
nb_classes = 9

model = get_model(in_shape, nb_classes)
model.load_weights(BASEDIR + '/wasyoku2_photos-model.hdf5')


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
    per = int(pre[idx]*100)
    return (idx, per)


def check_photo_wasyoku3(path, number):
    idx, per = check_photo(path)
    return LABELS[idx], CALORIES[idx]*VALUE[number], per
