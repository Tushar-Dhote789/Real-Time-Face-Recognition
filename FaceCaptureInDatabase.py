import cv2
import os
alg="haarcascade_frontalface_default.xml"

haar=cv2.CascadeClassifier(alg)

cam= cv2.VideoCapture(0)

dataset="datasets"
name="Tushar"

path=os.path.join(dataset,name)

if not os.path.isdir(path):
    os.mkdir(path)

(width,height)=(220,200)
count=1

while (count<=30):
    _,img=cam.read()
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces= haar.detectMultiScale(grayImg,1.3,4)
    for(x,y,w,h) in faces:
        print(count)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),2)

        onlyFace=grayImg[y:y+h,x:x+w]
        resizeImg=cv2.resize(onlyFace,(width,height))
        cv2.imwrite("%s/%s.jpg"%(path,count),resizeImg)
        count+=1
    cv2.imshow("FaceDetection",img)
    key=cv2.waitKey(10)&0xFF
    if key==ord("q"):
        break

print("Images captured")
cam.release()
cv2.destroyAllWindows()
