import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model

# Prepare Model

dir_path = os.path.dirname(os.path.realpath('10epoch.h5'))
preprocessed = os.path.join(os.getcwd(), 'james_code', '10epoch.h5')

classList = ['medium', 'ripe', 'unriped']

# Predicting


def predict(IMG_PATH):
    try:
        model = load_model(preprocessed)
        image = cv2.imread(IMG_PATH)
        image = cv2.resize(image, (150, 150))
        image = image.astype("float") / 255.0
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)

        res = model.predict(image)
        label = np.argmax(res)
        print("Label", label)
        labelName = classList[label]
        print("Label name:", labelName)
        return {"labelName": labelName, "value": float(label)}
    except Exception as err:
        return err
