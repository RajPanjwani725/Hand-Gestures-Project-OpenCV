import cv2
import mediapipe as mp
import time
import numpy as np

cap = cv2.VideoCapture('dance.mp4')

start_point=(0, 0)
end_point = (0, 0)
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils
flag=0
while (cap.isOpened()):
    ret, frame = cap.read()


    if ret == True:
        image = np.zeros(frame.shape)
        poseFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = pose.process(poseFrame)


        #print(result.pose_landmarks)\


        if result.pose_landmarks:
            mpDraw.draw_landmarks(image, result.pose_landmarks, mpPose.POSE_CONNECTIONS)
            for id, coordinates in enumerate( result.pose_landmarks.landmark):
                #print("------------")
                #print(id,coordinates)
                #print("====")
                h, w, c = frame.shape
                # By multipulying withj height and width we get pixal value
                cx, cy = int(coordinates.x * w), int(coordinates.y * h)
                if id==0:
                    cv2.circle(image, (cx, cy), 23, (225, 225, 225), -1)
                # elif id == 7 or id==8:
                #     cv2.circle(image, (cx, cy), 3, (0,0,0), -1)
                # elif id == 9 or id == 10:
                #     # global cx9,cx10,cy9,cy10
                #     if id==9:
                #         start_point = (cx, cy)
                #     if id==10:
                #         end_point = (cx, cy)
                #         color = (0, 0, 225)
                #
                #         thickness = 1
                #
                #         image = cv2.rectangle(image, start_point, end_point, color, thickness)





                else:
                    cv2.circle(image, (cx, cy), 3, (225, 225, 225), -1)


        cv2.imshow('Video', frame)
        cv2.imshow('Image', image)
        if cv2.waitKey(1) == 27:
            break
    else:
        break
cap.read()
cv2.destroyAllWindows()