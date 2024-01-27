from PIL import Image
from PIL.ExifTags import TAGS
import requests
import os
from datetime import datetime
import time
from deepface import DeepFace

# Global Image Data handler class
class ImageData:
    def __init__(self, image_path):
        self.image_path = image_path
        self.time_taken = self.get_time_taken()
        self.location = self.get_city_name()
        self.emotion = self.get_emotion()

    def __strAll__(self):
        # Implement the logic to return all metadata of the image in a string format
        print (f'File Path: {self.image_path}, Creation Time: {self.time_taken}, Location: {self.location}, Emotion: {self.emotion}')

    def __ImageDetails__(self):
        # Implement the logic to get specific metadata from the image
        image = Image.open(self.image_path)
        exif_data = image._getexif()
        exif = {TAGS.get(tag, tag): value for tag, value in exif_data.items()} if exif_data else {}
        GPSInfo = exif.get('GPSInfo')
        timeInfo = exif.get('DateTime')
        return GPSInfo, timeInfo

    def get_time_taken(self):
        raw_time_info = self.__ImageDetails__()[1]
        if raw_time_info != None:
            raw_time_info = datetime.strptime(raw_time_info, "%Y:%m:%d %H:%M:%S").date()

        return raw_time_info

    def __dms_to_decimal__(self):
        # Take in raw GPS info and convert to decimal 
        # Return decimal latitude and longitude in list format
        raw_GPS_Info = self.__ImageDetails__()[0]

        # If GPS info exists then convert to decimal
        if raw_GPS_Info != None:
            degrees_lat, degrees_long = raw_GPS_Info[2][0], raw_GPS_Info[4][0]
            minutes_lat, minutes_long = raw_GPS_Info[2][1], raw_GPS_Info[4][1]
            seconds_lat, seconds_long = raw_GPS_Info[2][2], raw_GPS_Info[4][2]
            direction_lat, direction_long = raw_GPS_Info[1], raw_GPS_Info[3]

            decimal_lat = degrees_lat + minutes_lat / 60 + seconds_lat / 3600
            decimal_long = degrees_long + minutes_long / 60 + seconds_long / 3600

            if direction_lat == 'S':
                decimal_lat = -decimal_lat
            if direction_long == 'W':
                decimal_long = -decimal_long

            return [float(decimal_lat), float(decimal_long)]

        return None, None

    def get_city_name(self):
        # Take in decimal latitude and longitude and return city name
        latitude, longitude = self.__dms_to_decimal__()

        # Ensure that latitude and longitude are not None before making the API request
        if latitude is not None and longitude is not None:
            url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}"
            response = requests.get(url)    

            if response.status_code == 200:
                data = response.json()
                address_components = data.get('address', {})

                city = address_components.get('city',
                                            address_components.get('town',
                                                                    address_components.get('village', 'Unknown')))
                return city
            else:
                print(f"Error: {response.status_code}")
                return None
        else:
            # Return None or a default value if latitude or longitude is None
            return None
        
    def get_emotion(self):
        # Get emotion of people in picture otherwise return None
        try:
            objs = DeepFace.analyze(img_path = self.image_path, actions = ['emotion'])
            objs = objs[0].get('dominant_emotion')
        except ValueError:
            objs = None
        
        return objs


if __name__ == '__main__': 
    DIR = r"C:\Users\16134\iCloudPhotos\Photos"
    start_time = time.time()
    
    for index, image in enumerate(os.listdir(DIR)):
        file_type = image[-3:].lower()
        img_path = os.path.join(DIR, image)

        if file_type == 'jpg':
            current_image = ImageData(img_path)
            current_image.__strAll__()

    print(index)
    end_time = time.time()
    execution_time = (end_time - start_time) / 60.0
    print("Total execution time = %5.2f" % (execution_time))    