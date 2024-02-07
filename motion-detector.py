# Import libraries

import winsound
import threading
import cv2
import imutils
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from envs import APP_PASSWORD
from datetime import datetime

# Email parameters
subject = "Motion Detected!"
sender = "jelaine.alexa0903@gmail.com"
recipients = ["coffeeejln@gmail.com"]

# Define a function to send an email
def send_email(subject, sender, recipients, body, image_filename=None):
    # Create a message object
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)

# Initialize camera capture

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Read the 1st frame as the starting frame

_, start_frame = cap.read()
start_frame = imutils.resize(start_frame, width=500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)

# Beep the alarm
def beep_alarm():
    for _ in range(5):
        print("ALARM")
        winsound.Beep(2750, 1000)

# Main loop
while True:

    # Capture frame from the camera
    _, frame = cap.read()
    frame = imutils.resize(frame, width=500)

    # Convert frame to grayscale
    frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)

    # Compute the difference between the current frame and the start frame
    difference = cv2.absdiff(frame_bw, start_frame)

    # Apply threshold to the difference to highlight motion
    threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
    start_frame = frame_bw

    # If motion is detected
    if threshold.sum() > 300:
        # Start a new thread to beep the alarm
        threading.Thread(target=beep_alarm).start()
    
    # Display the thresholded frame
    cv2.imshow("Cam", threshold)
    
    # Key press to exit loop
    key_pressed = cv2.waitKey(30)
    if key_pressed == ord("q"):
        break