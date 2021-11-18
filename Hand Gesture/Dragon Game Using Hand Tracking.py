import numpy as np
import mediapipe as mp
import cv2,time,math,pyautogui


cap= cv2.VideoCapture(0)

widthCam,heightCam=700,700
cap.set(3,widthCam)
cap.set(4,heightCam)
ptime=0

mpHands=mp.solutions.hands
hands=mpHands.Hands(min_detection_confidence=0.5)
draw=mp.solutions.drawing_utils



def handTrack(frame):
    frameHand = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result=hands.process(frameHand)
    if result.multi_hand_landmarks:
        for handNo in result.multi_hand_landmarks:
            for id,coordinates in enumerate(handNo.landmark):
                #print(id,coordinates)
                h, w, c = frame.shape
                # By multipulying withj height and width we get pixal value
                cx, cy = int(coordinates.x * w), int(coordinates.y * h)

                #print(f'{id} --> {cx},{cy}')

                if id==4:
                    x1,y1=cx,cy
                    cv2.circle(frame, (cx, cy), 10, (225, 225, 225), -1)
                if id==8:
                    x2, y2 = cx, cy
                    cv2.circle(frame, (cx, cy), 10, (225, 225, 225), -1)


                    length=math.hypot(x2-x1,y2-y1)
                    # print(length)
                    if length < 120:
                        cv2.line(frame, (x1, y1), (x2, y2), (225, 225, 225), 3)
                    elif length>=120:
                        cv2.line(frame, (x1, y1), (x2, y2), (210, 110, 20), 3)
                        pyautogui.press('space')
                        cv2.putText(frame, "JUMP", (250, 100), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    (0, 225, 0), 2)
                draw.draw_landmarks(frame,handNo,mpHands.HAND_CONNECTIONS)
            return length




while cap.isOpened():
    ret,frame=cap.read()

    if ret==True:
        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        length=handTrack(frame)
        print("Hand Length : - " ,length)
        # print("Length")
        # print(length)
        # hand range 15-200
        # VOLUME RANGE(-65, 0)


                # cv2.imshow("Video", frame)


        cv2.putText(frame,"FPS : "+str("{:.2f}".format(fps)),(80,100),cv2.FONT_HERSHEY_SIMPLEX,0.8,(150,120,120),2)
        cv2.imshow("Video",frame)
        if cv2.waitKey(1)==27:
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()