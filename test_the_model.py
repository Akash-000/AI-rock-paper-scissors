import sys
import os
from keras.models import load_model
import numpy as np
import cv2

img_path = sys.argv[1]

rev_class_map = {
    0:"rock",
    1:"paper",
    2:"scissors",
    3:"none"
    }


def mapper(val):
    return rev_class_map[val]



img = cv2.imread(img_path, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (227, 227))

model = load_model('rock_paper_scissors_model.h5')
pred = model.predict(np.array([img]))
#print(type(pred))
res_code = np.argmax(pred[0])

res_name = mapper(res_code)

print("Predicted : {}".format(res_name))
