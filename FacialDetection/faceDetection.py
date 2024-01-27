import os
import cv2 as cv
import numpy as np

def create_train(): 
    DIR = r'C:\Users\16134\OneDrive\Documents\Learning\Software\Courses\OpenCV\Photos'
    faces_roi = None
    people = []
    for i in os.listdir(DIR): 
        people.append(i) 
    print(people) 

    haar_cascade = cv.CascadeClassifier(r'haar_face.xml')
    features = [] 
    labels = []
    
    for person in people: 
        path = os.path.join(DIR, person) 
        label = people.index(person)
        print(label)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path) 
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4) 

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] 
                features.append(faces_roi) 
                labels.append(label) 

    return features, labels