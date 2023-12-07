import cv2 as cv
detect= cv.CascadeClassifier("content\haarcascade_frontalface_default.xml")
cam = cv.VideoCapture(0)
Id = input("enter id")
samplenum=0
while True:
    ret,img = cam.read()
    faces=detect.detectMultiScale(img,1.3,5)
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(144,1,1),3)
        samplenum = samplenum+1
        cv.imwrite("content\photos" +Id +'.' + str(samplenum) +".jpg",img[y:y + h, x:x + w])
        cv.imshow("frame", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    elif samplenum > 10:
        break
cam.release()
cv.destroyAllWindows()