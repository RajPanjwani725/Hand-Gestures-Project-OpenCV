import cv2
import mediapipe as mp
import time
import numpy as np
cap=cv2.VideoCapture('dance.mp4')

mpPose=mp.solutions.pose
pose=mpPose.Pose()
mpDraw=mp.solutions.drawing_utils


while(cap.isOpened()):
    ret,frame=cap.read()
    image = np.zeros(frame.shape)


    if ret==True:
        poseFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result=pose.process(poseFrame)
        print(result.pose_landmarks)
        if result.pose_landmarks:
            mpDraw.draw_landmarks(image, result.pose_landmarks, mpPose.POSE_CONNECTIONS)
        cv2.imshow('Video',frame)
        cv2.imshow('Image', image)
        if cv2.waitKey(1)==27:
            break
    else:
        break
cap.read()
cv2.destroyAllWindows()