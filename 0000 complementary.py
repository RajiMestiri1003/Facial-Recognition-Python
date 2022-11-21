import numpy as np
import cv2
print (cv2.__version__)
img = cv2.imread("dog.png")
from matplotlib import pyplot as plt
plt.imshow(img)
plt.show()
newImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(newImg)
plt.show()
print(img)
img2 = cv2.imread("dog.png")
gray = cv2.imread("dog.png",cv2.IMREAD_GRAYSCALE)
cv2.imshow('RustamGray',gray)
cv2.imshow('Rustam',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Lire une diffusion vidéo à partir d'une webcam

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if ret == False:
        continue
        
    cv2.imshow("Video Frame",frame)
    cv2.imshow("Gray Frame",gray_frame)
    
    #Attendre l'input de l'utilisateur - q, puis arreter la boucle
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()

#Cascade Haar

# Lire une diffusion video à partir d'une webcam (image par image)
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if ret == False:
        continue
        
    faces = face_cascade.detectMultiScale(frame,1.3,5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.rectangle(gray_frame,(x,y),(x+w,y+h),(255,54,80),2)
        
    cv2.imshow("Video Frame",frame)
    cv2.imshow("Gray Frame",gray_frame)  
    
    #Attendre l'input de l'utilisateur - q, puis arreter la boucle
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()