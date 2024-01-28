from deepface import DeepFace

img_path = r"C:\Users\16134\iCloudPhotos\Photos\IMG_0091.JPG"

try:
    objs = DeepFace.analyze(img_path = img_path, actions = ['age', 'gender', 'race', 'emotion'])
    print(objs)

except ValueError:
    print("Face not found")