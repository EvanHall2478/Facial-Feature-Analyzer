from PIL import Image
from PIL.ExifTags import TAGS
import requests
import os
from datetime import datetime
import time

# Global Image Data handler class
class ImageData:
    def __init__(self, image_path):
        self.image_path = image_path
        self.time_taken = self.__ImageDetails__()[1]
        self.location = self.get_city_name()

    def __strAll__(self):
        # Implement the logic to return all metadata of the image in a string format
        print (f'File Path: {self.image_path}, Creation Time: {self.time_taken}, Location: {self.location}')

    def __ImageDetails__(self):
        # Implement the logic to get specific metadata from the image
        image = Image.open(self.image_path)
        exif_data = image._getexif()
        exif = {TAGS.get(tag, tag): value for tag, value in exif_data.items()} if exif_data else {}
        GPSInfo = exif.get('GPSInfo')
        timeInfo = exif.get('DateTime')
        return GPSInfo, timeInfo

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
            print("Invalid latitude or longitude.")
            return None

if __name__ == '__main__': 
    image_path = r"C:\Users\16134\iCloudPhotos\Photos\IMG_0252.JPG"
    image = ImageData(image_path)
    image.__strAll__()