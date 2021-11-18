import cv2
import mediapipe as mp
import time
import numpy as np

mpfacemesh=mp.solutions.face_mesh
facemesh=mpfacemesh.FaceMesh(max_num_faces=2)

mpfacemesh=mp.solutions.face_mesh
facemesh=mpfacemesh.FaceMesh(max_num_faces=2)



 # Deawing Specifications
mpdraw=mp.solutions.drawing_utils
drawspect=mpdraw.DrawingSpec(thickness=1,circle_radius=1)

cap=cv2.VideoCapture(0)
pTime=0


while( cap.isOpened()):
    ret , frame=cap.read()

    if ret == True:
        npframe = np.ones(frame.shape)

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cTime=time.time()

        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(frame,f"FPS : {fps}",(20,70),cv2.FONT_HERSHEY_SIMPLEX,0.8,(225,225,225),3)



        result=facemesh.process(image)

        # This is to see if there are multiple  face land marks
        if result.multi_face_landmarks:

             # this for loop is for multiple face detection
            for facelandmarks in result.multi_face_landmarks:
                mpdraw.draw_landmarks(npframe,facelandmarks,mpfacemesh.FACEMESH_TESSELATION,landmark_drawing_spec=drawspect)

        cv2.imshow("VIDEO", frame)
        cv2.imshow("VIDEO White", npframe)

        if cv2.waitKey(1)==27:
            break

    else:
        break
cap.release()
cv2.destroyAllWindows()