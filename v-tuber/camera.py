import cv2,os
import mediapipe as mp
facemesh = mp.solutions.face_mesh.FaceMesh()

webcam = cv2.VideoCapture(0)


def getFace():
    while True:
        s,img = webcam.read()
        if s:
            if s:
                bgr=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                res = facemesh.process(bgr)
                try:
                    face = {}
                    for det in res.multi_face_landmarks:
                        face['nose'] = [det.landmark[4].x,det.landmark[4].y]
                        face['lip'] = [det.landmark[11].x,det.landmark[11].y]
                        face['blip'] = [det.landmark[14].x,det.landmark[14].y]
                        face['forhead'] = [det.landmark[10].x,det.landmark[10].y]
                        return face
                except: pass
        cv2.waitKey(1)

# 46 full right brow 
# 52 right brow

# 276 full left brow 
# 282 middle left brow