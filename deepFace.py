from deepface import DeepFace

img_path1 = r"C:\Users\16134\OneDrive\Documents\Learning\Software\Courses\OpenCV\Photos\Dharma\Dharma8.jpg" # Me
img_path2 = r"C:\Users\16134\OneDrive\Documents\Learning\Software\Courses\OpenCV\Photos\Dharma\Dharma22.jpg" # Me
img_path3 = r"C:\Users\16134\iCloudPhotos\Photos\IMG_0252.JPG" # ryan lefevbre
img_path4 = r"C:\Users\16134\iCloudPhotos\Photos\IMG_0210.JPG" # relay team w me
img_path5 = r"C:\Users\16134\iCloudPhotos\Photos\IMG_1427.PNG" # young me in collage
img_path6 = r"C:\Users\16134\iCloudPhotos\Photos\5E69A4C1-0748-4314-B9E6-A19B1F906A44.jpg" # Tennis team wo me
img_path7 = r"C:\Users\16134\Downloads\IMG_4892.jpg" # Hasan

Dharma = [img_path1, img_path2,img_path4]
Ryan = [img_path3]
David = [img_path6]
Hasan = [img_path7]
images = [Dharma, Ryan, David, Hasan]

# Get emotion of people (get rid of age, emotion and gender)
# try:
#     objs = DeepFace.analyze(img_path = img_path7, actions = ['age', 'gender', 'race', 'emotion'])
#     print(objs)

# except ValueError:
#     print("Face not found")

for person in images:
    # Verify if two images contain the same person
    result = DeepFace.verify(img1_path = person[0], img2_path = img_path5) #0.68 is threshold for similarity between faces, 0 (identical) and 1 (dissimilarity)
    if result.get('verified'):
        print(person)
        break


    