import cv2  # OpenCV
import os # Library os

haar_file = "haarcascade_frontalface_default.xml"
datasets = "dataset"
sub_data = "Zafir Abdullah" # Write First,Middle,Last name after Recognition on your face everywhere

path = os.path.join(datasets, sub_data) # /datasets/Zafir Abdullah

if not os.path.isdir(path):  #  if this folder is not present
    os.mkdir(path)   # Create that folder

(width, height) = (130, 100)

face_cascade = cv2.CascadeClassifier(haar_file)  # Loading face Detection alg.
webcam = cv2.VideoCapture(0)  # Camera Initialization

count = 1

while count < 31:
    print(count)
    (_, im) = webcam.read()  # Read frame from camera
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # Color from to Gray
    faces = face_cascade.detectMultiScale(gray, 1.3, 4) # Detect Face.
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(150,180, 250),2)  # Draw rectangle around face
        face = gray[y:y + h, x:x + w]   # Crop only face part
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('%s/%s.png' % (path,count), face_resize)
        count += 1

    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()