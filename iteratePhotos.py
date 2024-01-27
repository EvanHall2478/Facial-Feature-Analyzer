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
        pass
        # return f'File Path: {self.file_path}, Creation Time: {self.time_taken}, Location: {self.location}'

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
            degreees_lat, degrees_long = raw_GPS_Info[2][0], raw_GPS_Info[4][0]
            minutes_lat, minutes_long = raw_GPS_Info[2][1], raw_GPS_Info[4][1]
            seconds_lat, seconds_long = raw_GPS_Info[2][2], raw_GPS_Info[4][2]
            direction_lat, direction_long = raw_GPS_Info[1], raw_GPS_Info[3]

        decimal_lat = degreees_lat + minutes_lat / 60 + seconds_lat / 3600
        decimal_long = degrees_long + minutes_long / 60 + seconds_long / 3600

        if direction_lat == 'S':
            decimal_lat = -decimal_lat
        if direction_long == 'W':
            decimal_long = -decimal_long

        return [decimal_lat, decimal_long]

    def get_city_name(self):
        # Take in decimal latitude and longitude and return city name
        latitude, longitude = self.__dms_to_decimal__()

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

# Usage example:
image_path = "/path/to/image.jpg"
imageClass = ImageData(image_path)
imageClass.process_image()




# # Create a class which stores the data and file paths for the images 
# class ImageData:
#     def __init__(self, image_path):
#         self.image_path = image_path
#         # self.time_taken = creation_time
#         self.time_taken = self.__ImageDetails__()[1] 
#         self.location = self.get_location()
        
#     # Return the all metadata of the image
#     def __strAll__(self):
#         return f'File Path: {self.file_path}, Creation Time: {self.time_taken}, Location: {self.location}'
    
#     # Get specific metadata from image
#     def __ImageDetails__(self):
#         image = Image.open(self.image_path)
#         exif_data = image._getexif()
#         exif = {TAGS.get(tag, tag): value for tag, value in exif_data.items()} if exif_data else {}
#         GPSInfo = exif.get('GPSInfo')
#         timeInfo = exif.get('DateTime')
#         return GPSInfo, timeInfo
    
#     def __dms_to_decimal__(sel):
#         raw_GPS_Infor = self.__ImageDetails__()[0]
        
#         degrees = coordinates[0]
#         minutes = coordinates[1]
#         seconds = coordinates[2]

#         decimal = degrees + minutes / 60 + seconds / 3600
#         if direction in ['S', 'W']:
#             decimal = -decimal
#         return decimal
    
#     # Convert DMS to decimal for latitude and longitude
#     def get_location(self):
#         # Do dms conversion for both latitude and longitude

#         # latitude = dms_to_decimal(current_GPS_info[2], current_GPS_info[1])
#         # longitude = dms_to_decimal(current_GPS_info[4], current_GPS_info[3])
#         # city = get_city_name(float(latitude), float(longitude))
#         # for i in range(4)+1:
#         raw_GPS_Infor = self.__ImageDetails__()[0]

#         if raw_GPS_Infor != None:
#                 latitude = dms_to_decimal(current_GPS_info[2], current_GPS_info[1])
#                 longitude = dms_to_decimal(current_GPS_info[4], current_GPS_info[3])
#                 city = get_city_name(float(latitude), float(longitude))
        
#         degrees = coordinates[0]
#         minutes = coordinates[1]
#         seconds = coordinates[2]

#         decimal = degrees + minutes / 60 + seconds / 3600

#         if direction in ['S', 'W']:
#             decimal = -decimal
        
#         url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}"
#         response = requests.get(url)
        
#         if response.status_code == 200:
#             data = response.json()
#             address_components = data.get('address', {})
            
#             city = address_components.get('city', 
#                 address_components.get('town', 
#                 address_components.get('village', 'Unknown')))
            
#             return city
#         else:
#             print(f"Error: {response.status_code}")
#             return None
        
#         # return decimal
    

#     # From GPS information, get city name associated with image
#     # def get_city_name(latitude, longitude):
        


# imageClass = ImageData()
# print(imageClass.__strAll__())



# # Get specific metadata from image
# def ImageDetails(image_path):
#     image = Image.open(image_path)
#     exif_data = image._getexif()
#     exif = {TAGS.get(tag, tag): value for tag, value in exif_data.items()} if exif_data else {}
#     GPSInfo = exif.get('GPSInfo')
#     timeInfo = exif.get('DateTime')
    
#     return GPSInfo, timeInfo




def main():
    DIR = r"C:\Users\16134\iCloudPhotos\Photos"
    start_time = time.time()
    image_cities = set()
    image_time = set()

    for index, i in enumerate(os.listdir(DIR)):
        file_type = i[-3:].lower()
        img_path = os.path.join(DIR, i)

        if file_type == 'jpg':
            current_GPS_info, current_time_info = ImageDetails(img_path)

            if current_GPS_info != None:
                latitude = dms_to_decimal(current_GPS_info[2], current_GPS_info[1])
                longitude = dms_to_decimal(current_GPS_info[4], current_GPS_info[3])
                city = get_city_name(float(latitude), float(longitude))
                image_cities.add(city)

            if current_time_info != None:
                image_date = datetime.strptime(current_time_info, "%Y:%m:%d %H:%M:%S").date()
                image_time.add(image_date)


    print(index)
    print(image_cities)
    print(image_time)
    end_time = time.time()
    total_time = (end_time - start_time)/60
    print("Total execution time = %5.2f" % (total_time))

if __name__ == '__main__': 
    main()