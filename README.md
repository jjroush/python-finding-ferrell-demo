# Finding Ferrell Python Demo

Learn just how powerful and fun it is to write in Python by using the `face_recognition` library to detect Will Ferrell in photos and modify the image using `pillow`.

![alt text](https://roush-image.s3.amazonaws.com/face-detect-example.gif "Face Detection")

## How to Run

1. Verify Python and Pip is installed on your machine by running `python -V` and `pip -V` (version 2 or 3 should work).

    A good guide for install python can be found [here](https://realpython.com/installing-python/#step-1-download-the-python-3-installer).

    *If you have installed but cannot access via command line, this typically means Python hasn't been set to your [PATH](https://datatofish.com/add-python-to-windows-path/) variable.*

2. Install Pillow, dlib and facial_recognition are  via `pip`
   
   `pip install pillow dlib facial_recognition`

3. Run the app with `python ./face-detect.py`

## How it Works

We first load a reference image `Will-Ferrell.jpg` into `face_detection` then encode the image using:

```python
face_recognition.face_encodings(
    ferrellReferencePhoto)[0]
```

This gives an array which can be used to compare against other face encodings. Upon encoding the image we are then able to compare them with:

```python
face_recognition.compare_faces(
    ferrellReferencePhotoEncoded, newPhotoEncoded)
```

Comparing faces will give us an array with each index having a boolean value of the reference photo. Combining `compare_faces` and `face_locations` method, we have all the data we need to modify the image.

Everything else is done using `Pillow`. First we will create a new drawing which I assign as: 
```python
canvas = ImageDraw.Draw(newPhotoModified)
```
We will do all image modification via the canvas. When we are done drawing on the image, we will save it into a file with:
```python
newPhotoModified.save("output.jpg", "JPEG")
```
## Resources

Checkout the docs of the two main libraries used:

[Facial Recognition Library](https://github.com/ageitgey/face_recognition)

[Image Manipulation using Pillow](https://github.com/python-pillow/Pillow)

Also read up on the [Python docs](https://www.python.org/doc/).



## Ideas to expand upon the project.

1. Add the ability to detect John C. Reilly.
2. Add sunglasses to every face.
3. Swap Will and John's Faces.
4. Make a Meme Generator.