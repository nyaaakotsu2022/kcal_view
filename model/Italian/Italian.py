import keras
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import RMSprop

LABELS = ["アヒージョ", "ハンバーガー", "カルボナーラ", "ナポリタンスパゲッティ", "ペペロンチーノ", "ピザ", "ローストビーフ", "サンドイッチ"]
CALORIES = [329, 446, 779, 590, 505, 872, 78, 314]
VALUE = {"1人前": 1, "2人前": 2, "3人前": 3, "4人前": 4}


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
nb_classes = 8

model = get_model(in_shape, nb_classes)
model.load_weights('./itarian_photos-model.hdf5')


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


def check_photo_Italian(path, number):
    idx, per = check_photo(path)
    return LABELS[idx], CALORIES[idx]*VALUE[number], per
