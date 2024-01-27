# This file is responsible for obtianing the date on all images and clustering them based on the user defined range 


import os 
import time

# Specify the file path 
file_path = r'C:\Users\evanh\Software\UofTHacks\NostalgicMobilePhotoAlbum\FacialDetection\faceDetection.py'

#  Get creation time 
creation_time = os.path.getctime(file_path)

# convert to readable format
readable_creation_time = time.ctime(creation_time)

print(f'Creation time of file is {readable_creation_time}')