import os
import cv2
import sys
import numpy as np

try:
    label_name = sys.argv[1]
    num_samples = int(sys.argv[2])

except:
    print("Argument Missing")
    print("Please provide label_name and number of samples in cmd line to run the program")



img_data = 'image data'
img_label_path = os.path.join(img_data, label_name)

try:
    os.mkdir(img_data)

except(FileExistsError ):
    pass

try:
    os.mkdir(img_label_path)
except(FileExistsError):
    print("Directory already present")
    
cap = cv2.VideoCapture(0)
cap.set(3, 3000)
cap.set(4, 3000)

start = False
count = 0

while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    if(ret == False):
        continue
    
    if(count == num_samples):
        break
    
    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 3)
    
    if(start):
        roi = frame[100:500, 100:500]
        img_cap = os.path.join(img_label_path, "{}.jpg".format(count+1))
        cv2.imwrite(img_cap, roi)
        count+=1

    
    font = cv2.FONT_HERSHEY_SIMPLEX
    frame = cv2.putText(frame, 'Collecting : {} image'.format(count), (100, 550), font ,0.5, (0, 255, 255), 1, cv2.LINE_AA)

    frame = cv2.imshow('Collecting-images',frame)
    
    k = cv2.waitKey(1)& 0xFF

    if(k == ord('a')):
        start = True

    if(k == ord('q')):
        cap.release()
        break



cap.release()
if(count == 0):
    print("No images saved....")
else:
    print("Image Saved successfully !!!")
cv2.destroyAllWindows()



