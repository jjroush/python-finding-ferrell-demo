# Manipulate images with the Pillow Library
from PIL import Image, ImageFont, ImageDraw
# import face detection from when we installed with pip
import face_recognition

ferrellReferencePhoto = face_recognition.load_image_file("./Will-Ferrell.jpg")

# This variable stores all the facial features encoded in an array which face_recognition will use to compare
ferrellReferencePhotoEncoded = face_recognition.face_encodings(
    ferrellReferencePhoto)[0]

numberPicker = input("Pick a number 1-5: ")

newPhoto = face_recognition.load_image_file(
    "./examples/ferrell-" + numberPicker + ".jpg")

# locations are saved as top, bottom, left, right. Get encoding of new photo
newPhotoFaceLocations = face_recognition.face_locations(newPhoto)
newPhotoEncoded = face_recognition.face_encodings(
    newPhoto, newPhotoFaceLocations)

newPhotoModified = Image.open("./examples/ferrell-" + numberPicker + ".jpg")

# All of our drawing
canvas = ImageDraw.Draw(newPhotoModified)

# Gives an array of which faces are Will's
results = face_recognition.compare_faces(
    ferrellReferencePhotoEncoded, newPhotoEncoded)

font = ImageFont.truetype("Roboto-Black.ttf", 38, encoding="unic")
# enumerate gives an index value

for index, faces in enumerate(newPhotoFaceLocations):
    color = "black"
    if (results[index]):
        color = "red"
        canvas.text((faces[3], faces[2]), "Ferrell Located", "White", font)

    canvas.rectangle(
        ((faces[3], faces[0]), (faces[1], faces[2])), outline=color)

newPhotoModified.save("output.jpg", "JPEG")
