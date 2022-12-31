import keras
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image
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
# model=cnn_model.get_model(in_shape,nb_classes)
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

def check_photo_str(path, number):
    idx, per = check_photo(path)
    st.text("この写真は、{}で、カロリーは{}kcal".format(LABELS[idx], CALORIES[idx]*VALUE[number]))
    st.text("可能性は、{}%".format(per))

"""
if __name__=='__main__':
    # List = [チョコケーキ、チーズケーキ、ティラミス、シュークリーム、ショートケーキ、ロールケーキ、パウンドケーキ、モンブラン]
    ans = ["tyokoke-ki.jpg", "ti-zuke-ki.jpg", "teliramisu.jpg", "syu-kuri-mu.jpg", "syo-toke-ki.jpg", "ro-ruke-ki.jpg", "paunndoke-ki.jpg", "monburan.jpg"]
    
    for i in ans:
        print(str(i))
        check_photo_str(i)
    ##check_photo_str('tyokoke-ki.jpg')
    ##check_photo_str('ti-zuke-ki.jpg')
    ##check_photo_str('teliramisu.jpg')
    ##check_photo_str('syu-kuri-mu.jpg')
    #check_photo_str('syo-toke-ki.jpg')
    #check_photo_str('ro-ruke-ki.jpg')
    #check_photo_str('paunndoke-ki.jpg')
    #check_photo_str('monburan.jpg')
"""