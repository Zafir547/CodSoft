import cv2  #OpenCV

alg = "haarcascade_frontalface_default.xml"     # Accessed the Model file
haar_cascade = cv2.CascadeClassifier(alg)       # Loading the Model With cv2
cam = cv2.VideoCapture(0)     # Initializing Camera

while True:
    _,img = cam.read()     # Read the frame the Camera
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)      # Converting Color into Gray Scale Image
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)      # Get Coordinate of face
    for (x,y,w,h) in face: # Segregating x,y,w,h                            
        cv2.rectangle(img, (x,y), (x+w,y+h), (155,155,250),2)
    cv2.imshow("Face Detection",img)
    key = cv2.waitKey(10)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()