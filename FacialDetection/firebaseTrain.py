import os
import cv2 as cv
import numpy as np

people = []
for i in os.listdir(r'C:\Users\16134\OneDrive\Documents\Learning\Software\Courses\OpenCV\Photos'): #this adds the name of the folders to the people list 
    people.append(i) #append adds a single item to the list
print(people) 

#you could also choose to just manually fill the names in the list

DIR = r'C:\Users\16134\OneDrive\Documents\Learning\Software\Courses\OpenCV\Photos' #set DIR to the path of the folder w the mandem
haar_cascade = cv.CascadeClassifier(r'haar_face.xml')

features = [] #image arrays
labels = [] #who the image array corresponds to (label of the array)

def create_train(): #this will visit every folder, and every image in the folders and add it to the training set
    for person in people: 
        path = os.path.join(DIR, person) #youre joining the path of the main folder DIR, with the names of the folder (people list) to read them in
        label = people.index(person) #varialbe holding the position of that person in the people index
        print(label)

        for img in os.listdir(path): #this reads in all the images in each folder/person
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path) #reading in the image
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4) #getting the rectangular coordinates of face

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] #youre saving the faces using the rectangular coordinates
                #basically cropping the rectangle and saving it

                features.append(faces_roi) #saving the rectaing in the features list 
                labels.append(label) #saving the name of the person (they have the same index)

create_train()
print('Training done ---------------')

features = np.array(features, dtype='object') #converting the lists to arrays 
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features,labels)

#saving everything as their seperate files
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)