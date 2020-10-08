import cv2
import os
import numpy as np
from keras.models import load_model
from random import choice


Class_map = {
    0: "rock",
    1:"paper",
    2:"scissors",
    3:"none"
    }

def mapper(val):
    return Class_map[val]


def get_winner(user_move, comp_move):
    if(user_move == comp_move):
        return "Tie"

    if(user_move == "rock"):
        if(comp_move == "paper"):
            return "Computer"
        if(comp_move == "scissors"):
            return "You"

    if(user_move == "paper"):
        if(comp_move == "rock"):
            return "You"
        if(comp_move == "scissors"):
            return "Computer"

    if(user_move == "scissors"):
        if(comp_move == "paper"):
            return "You"
        if(comp_move == "rock"):
            return "Computer"
    
    
    


model = load_model("rock_paper_scissors_model.h5")

cap = cv2.VideoCapture(0)
cap.set(3, 3000)
cap.set(4, 3000)

prev_move_name = None

while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if(ret == False):
        continue
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, "Put your signs here --> ",(100, 80), font, 0.7, (0, 255, 255), 3, cv2.LINE_AA)
    cv2.putText(frame, "Computer Move --> ", (800, 80), font, 0.7, (0, 255, 255), 3, cv2.LINE_AA)
    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 1)
    cv2.rectangle(frame, (800, 100), (1200, 500), (255, 255, 255), 1)

    roi = frame[100:500, 100:500]
    img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (227, 227))

    pred = model.predict(np.array([img]))
    img_code = np.argmax(pred[0])
    img_move_name = mapper(img_code)

    if(prev_move_name != img_move_name):
        if(img_move_name !="none"):
            computer_move_name = choice(["rock", "paper", "scissors"])
            winner = get_winner(img_move_name, computer_move_name)

        else:
            computer_move_name = "none"
            winner = "Waiting ..."

    prev_move_name = img_move_name


    cv2.putText(frame, "Winner is : "+winner, (400, 600), font, 2,(0, 255, 255), 1, cv2.LINE_AA)

    if(computer_move_name != "none"):
        comp_img = cv2.imread("computer_moves/{}.png".format(computer_move_name), 1)
        comp_img = cv2.resize(comp_img, (400, 400))
        frame[100:500, 800:1200] = comp_img

    cv2.imshow("Game", frame)


    
        
    k = cv2.waitKey(1)&0xFF
    if(k==ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
    



