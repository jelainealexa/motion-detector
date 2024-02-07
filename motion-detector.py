# Initialize camera capture

import cv2
import imutils

# Set camera properties

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Read the 1st frame as the starting frame

_, start_frame = cap.read()
start_frame = imutils.resize(start_frame, width=500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)

# Main loop
while True:

    # Capture frame from the camera
    _, frame = cap.read()
    frame = imutils.resize(frame, width=500)

    # Convert frame to grayscale
    frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise

    # Compute the difference between the current frame and the start frame
    # Apply threshold to the difference to highlight motion
    
    # Display the thresholded frame
    
    # Key press to exit loop