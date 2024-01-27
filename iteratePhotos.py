from PIL import Image
from PIL.ExifTags import TAGS
import requests
import os
from datetime import datetime
import time

def ImageDetails(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    exif = {TAGS.get(tag, tag): value for tag, value in exif_data.items()} if exif_data else {}
    GPSInfo = exif.get('GPSInfo')
    timeInfo = exif.get('DateTime')
    
    return GPSInfo, timeInfo

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
    
def location_filter(database, city):
    filtered_images = {image: details for image, details in database.items() if details['Location'].lower() == city.lower()}
    return filtered_images

def time_filter(database, week):
    filtered_images = {image: details for image, details in database.items() if details['Date'].lower() == week.lower()}
    return filtered_images

def main():
    DIR = r"C:\Users\16134\iCloudPhotos\Photos"
    start_time = time.time()
    image_dict = {}
    image_cities = set()
    image_time = set()

    for index, i in enumerate(os.listdir(DIR)):
        file_type = i[-3:].lower()
        img_path = os.path.join(DIR, i)

        if file_type == 'jpg':
            current_GPS_info, current_time_info = ImageDetails(img_path)

            city = None
            if current_GPS_info != None:
                latitude = dms_to_decimal(current_GPS_info[2], current_GPS_info[1])
                longitude = dms_to_decimal(current_GPS_info[4], current_GPS_info[3])
                city = get_city_name(float(latitude), float(longitude))

            image_date = None
            if current_time_info != None:
                image_date = datetime.strptime(current_time_info, "%Y:%m:%d %H:%M:%S").date()
            image_dict[img_path] = {'Location': city, 'Date': image_date}

    ottawa_images = location_filter(image_dict, 'Ottawa')
    print(ottawa_images)

    print(index)
    # print(image_cities)
    # print(image_time)
    end_time = time.time()
    total_time = (end_time - start_time)/60
    print("Total execution time = %5.2f" % (total_time))

if __name__ == '__main__': 
    main()