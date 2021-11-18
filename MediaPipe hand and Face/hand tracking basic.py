import cv2
import mediapipe as mp
import time
cap=cv2.VideoCapture(0)
# Use to detect hands
# https://google.github.io/mediapipe/getting_started/python.html
mpHands = mp.solutions.hands
hands = mpHands.Hands()

# used for create points and line on hands
mpDraw=mp.solutions.drawing_utils

prevTime=0
currentTime=0

while(cap.isOpened()):
    ret,frame=cap.read()

    if ret==True:

        frameHand = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frameHand)
        print(result.multi_hand_landmarks)
        # here result.multi_hand_landmarks is in decimals  i.e ratio of Image
        # this is used to see if there are land MARKS
        if result.multi_hand_landmarks:
            # mpHands.HAND_CONNECTIONS --> use to connect lines between points
            # handNo(Hand Number) use to get number of hands in  frame default 2

            # THIS LOOP IS FOR MULTI HAND
            for handNo in result.multi_hand_landmarks:
                for id,coordinates in enumerate(handNo.landmark):

                    # print(id,coordinates)
                    h,w,c=frame.shape
                    # By multipulying withj height and width we get pixal value
                    cx,cy=int(coordinates.x*w),int(coordinates.y*h)

                    print(f'{id} --> {cx},{cy}')

                    for i in range(0,id+1):
                        cv2.circle(frame,(cx,cy),10,(225,225,225),-1)


                mpDraw.draw_landmarks(frame,handNo,mpHands.HAND_CONNECTIONS)

            currentTime=time.time()
            fps=1/(currentTime-prevTime)
            prevTime=currentTime
            cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,255),2)


        cv2.imshow("Video",frame)
        #cv2.imshow("Video RGB", frameHand)

        # cv2.imshow("Video Hand",result)


        if cv2.waitKey(1)==27:
            break
cap.release()
cv2.destroyAllWindows()
