from PIL import Image
from PIL.ExifTags import TAGS
import requests
import os

def dms_to_decimal(coordinates, direction):
    degrees = coordinates[0]
    minutes = coordinates[1]
    seconds = coordinates[2]

    decimal = degrees + minutes / 60 + seconds / 3600
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

def get_city_name(latitude, longitude):
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

if __name__ == '__main__': 
    image_path = r"C:\Users\16134\iCloudPhotos\Photos\IMG_1094.JPG"
    image = Image.open(image_path)
    exif_data = image._getexif()
    exif = {TAGS.get(tag, tag): value for tag, value in exif_data.items()} if exif_data else {}
    GPSInfo = exif.get('GPSInfo')
    print(GPSInfo)

    latitude = dms_to_decimal(GPSInfo[2], GPSInfo[1])
    longitude = dms_to_decimal(GPSInfo[4], GPSInfo[3])
    city = get_city_name(float(latitude), float(longitude))
    print(f"The city name is: {city}")

    DIR = r'C:\Users\16134\iCloudPhotos\Photos'
    for i in os.listdir(DIR): 
        print(i)