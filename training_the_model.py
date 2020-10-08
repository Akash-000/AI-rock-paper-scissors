import cv2
import os
from keras.models import Sequential
from keras_squeezenet import SqueezeNet
from keras.layers import Activation, Dropout, GlobalAveragePooling2D, Convolution2D
import numpy as np
from keras.utils import np_utils
from keras.optimizers import Adam


image_data = 'image data'


Class_map = {
    "rock":0,
    "paper" : 1,
    "scissors":2,
    "none":3
    }

num_class = len(Class_map)

def mapper(val):
    return Class_map[val]


def get_model():
    model = Sequential([
        SqueezeNet(input_shape = (227, 227, 3), include_top = False),
        Dropout(0.5),
        Convolution2D(num_class, (1, 1)),
        Activation('relu'),
        GlobalAveragePooling2D(),
        Activation('softmax')
        ]
        )
    return model

dataset = []

for directory in os.listdir(image_data):
    into_labels = os.path.join(image_data, directory)

    for imgs in os.listdir(into_labels):
        img = cv2.imread(os.path.join(into_labels, imgs))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (227, 227))

        dataset.append([img, directory])

data, labels = zip(*dataset)

labels = list(map(mapper, labels))

labels = np_utils.to_categorical(labels)

model = get_model()

model.compile(optimizer = Adam(lr= 0.0001), loss = 'categorical_crossentropy', metrics = ['accuracy'])

model.fit(np.array(data), np.array(labels), epochs = 10,)
model.save('rock_paper_scissors_model.h5')
