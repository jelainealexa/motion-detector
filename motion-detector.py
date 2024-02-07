# Initialize camera capture

import cv2
import imutils

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Set camera properties

# Read the 1st frame as the starting frame

# Main loop
    # Capture frame from the camera
    # Convert frame to grayscale
    # Apply Gaussian blur to reduce noise

    # Compute the difference between the current frame and the start frame
    # Apply threshold to the difference to highlight motion
    
    # Display the thresholded frame
    
    # Key press to exit loop