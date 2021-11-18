import cv2
import numpy as np
import mediapipe as mp

import cv2,time,math

cap=cv2.VideoCapture(0)
cap. set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
cap. set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)
canvas = np.zeros((1000,1000,3))


mpHands=mp.solutions.hands
hands=mpHands.Hands(min_detection_confidence=0.85)
draw=mp.solutions.drawing_utils

drawColor=[(100,100,25)]


x1,y1,x2,y2=0,0,0,0

xp,yp=0,0
while cap.isOpened():

    ret,frame=cap.read()

    frame=cv2.flip(frame,1)

    if ret==True:
        frameHand = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frameHand)
        if result.multi_hand_landmarks:
            for handNo in result.multi_hand_landmarks:
                # print(result.multi_hand_landmarks)


                for id, coordinates in enumerate(handNo.landmark):
                    # print(id,coordinates)
                    pos = []
                    h, w, c = frame.shape

                    cx, cy = int(coordinates.x * w), int(coordinates.y * h)

                    # 1 Find Land Marks


                    if id==8:
                        # print("--------------Start------------")
                        # print(id, cx, cy)
                        x1,y1=cx,cy
                    if id==12:
                        # print(id, cx, cy)
                        # print("--------------End------------")
                        x2,y2=cx,cy



                draw.draw_landmarks(frame, handNo, mpHands.HAND_CONNECTIONS)
                # 2- Number of Finger are up
                if y1 > y2:
                    cv2.circle(frame, (x1, y1), 10, drawColor[0], -1)
                    xp,yp=0,0

                    if 40 < x1 < 120 and 40 < y1 < 120:
                        drawColor.pop(0)
                        drawColor.append((225, 225, 225))
                        print(drawColor)
                    elif 200 < x1 < 280 and 40 < y1 < 120:
                        drawColor.pop(0)
                        drawColor.append((0, 0, 225))
                        print(drawColor)
                    elif 360 < x1 < 440 and 40 < y1 < 120:
                        drawColor.pop(0)
                        drawColor.append((225, 0, 0))
                        print(drawColor)

                    elif 480 < x1 < 560 and 40 < y1 < 120:
                        drawColor.pop(0)
                        drawColor.append((0, 225, 0))
                        print(drawColor)

                    elif 640 < x1 < 720 and 40 < y1 < 120:
                        drawColor.pop(0)
                        drawColor.append((0, 0, 0))
                        print(drawColor)
                    elif 770 < x1 < 890 and 52 < y1 < 120:
                        drawColor.pop(0)
                        drawColor.append((0, 0, 0))
                        print(drawColor)
                elif y1 < y2:
                    print('0000000000000000000000000000')
                    print(drawColor[0])
                    if xp==0 and yp==0:
                        xp,yp=x1,y1
                    cv2.line(canvas, (xp,yp), (x1,y1), drawColor[0], 8)
                    xp,yp=x1,y1

        cv2.circle(frame, (80, 80), 40, (225, 225, 225),-1)
        cv2.circle(frame, (240, 80), 40, (0, 0, 225), -1)
        cv2.circle(frame, (400, 80), 40, (225, 0, 0), -1)
        cv2.circle(frame, (520, 80), 40, (0, 225, 0), -1)
        cv2.circle(frame, (680, 80), 40, (0, 0, 0), -1)
        cv2.rectangle(frame, (760, 50), (890,120),(0,0,0), 4)
        cv2.putText(frame,"Eraser",(770, 90),cv2.FONT_HERSHEY_SIMPLEX,1,(1,1,1),2,cv2.LINE_AA,)



        # 3 Select when Two fingers are Up
        # 4 Draw Lines

        cv2.imshow("Video",frame)
        # img=cv2.addWeighted()
        cv2.imshow("Canvas", canvas)
        if cv2.waitKey(1)==27:
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()