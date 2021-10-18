import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model

# Prepare Model

dir_path = os.path.dirname(os.path.realpath('kengi-papaya-model.h5'))
preprocessed = os.path.join(os.getcwd(), 'james_code', 'kengi-papaya-model.h5')

model = load_model(preprocessed)

# Predicting


def predict(sendedPictures):
    try:
        answers = []

        classList = ['medium', 'ripe', 'unripe']
        base_test = os.path.join(os.getcwd(), 'content', 'raw-data/')
        # pictures = list(map(lambda x: base_test+x, sendedPictures))

        # for i in pictures:
        # if(i == base_test+'.DS_Store'):
        #     continue
        # img = tf.keras.preprocessing.image.load_img(
        #     sendedPictures, target_size=(150, 150)
        # )
        img_array = tf.keras.preprocessing.image.img_to_array(
            float(sendedPictures.decode()))
        img_array = img_array / 255
        img_array = img_array.reshape(1, 150, 150, 3)
        predictions = model.predict(img_array)
        answers.append(classList[np.argmax(predictions[0])])
        return answers
    except Exception as err:
        return err
