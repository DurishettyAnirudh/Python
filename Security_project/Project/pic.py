import cv2 
import subprocess
def takephoto():
        # Initialize the camera
        cam = cv2.VideoCapture(0)

        # Capture a single frame
        ret, frame = cam.read()

        # Release the camera
        cam.release()

        # Check if the frame was captured successfully
        if not ret:
            print("Frame not captured")
        else:
            # Save the captured frame as an image
            img_name = "Culprit.jpg"
            cv2.imwrite(img_name, frame)
            print("Image captured")

