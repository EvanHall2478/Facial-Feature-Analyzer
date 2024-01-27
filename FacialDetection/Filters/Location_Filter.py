# This file is responsible for obtianing the date on all images and clustering them based on the user defined range 
import os 
import time

# Specify the file path 
# file_path = r'C:\\Users\\evanh\\Software\\UofTHacks\\NostalgicMobilePhotoAlbum\\Photos\Dharma'

#  Relative path
file_path = r'Photos\Dharma'

#  Get creation time 
creation_time = os.path.getctime(file_path)
# convert to readable format
readable_creation_time = time.ctime(creation_time)



print(f'Creation time of file is {readable_creation_time}')

# Create a class which stores the data and file paths for the images 
class ImageData:
    def __init__(self, file_path, creation_time):
        self.file_path = file_path
        self.time_taken = creation_time
        self.location = None #Replace and add location variable
    
    # Return the all metadata of the image
    def __strAll__(self):
        return f'File Path: {self.file_path}, Creation Time: {self.time_taken}, Location: {self.location}'

imageClass = ImageData()
print(imageClass.__strAll__())

