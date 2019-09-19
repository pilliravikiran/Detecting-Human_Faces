import cv2
image = cv2.imread("33.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
rects= detector.detectMultiScale(gray,scaleFactor=1.3,minSize=(45,45))
for(i,(x,y,w,h))in enumerate (rects):
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)	
cv2.imshow("Faces Of Humans",image)
cv2.waitKey(0)



