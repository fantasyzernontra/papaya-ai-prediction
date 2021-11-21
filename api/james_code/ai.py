import tensorflow as tf
import os
import numpy as np
from keras.models import load_model

# Prepare Model

dir_path = os.path.dirname(os.path.realpath('augmentation.h5'))
preprocessed = os.path.join(os.getcwd(), 'james_code', 'augmentation.h5')

classList = ['medium', 'ripe', 'unriped']

# Predicting


def predict(IMG_PATH):
    try:
        model = load_model(preprocessed)
        img = tf.keras.preprocessing.image.load_img(
        IMG_PATH, target_size=(150, 150)
        )
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = img_array / 255
        img_array = img_array.reshape(1,150,150,3)

        res = model.predict(img_array)
        label = np.argmax(res)
        labelName = classList[label]
        
        return {"labelName": labelName, "value": float(label)}
    except Exception as err:
        return err
