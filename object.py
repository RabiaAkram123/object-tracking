import numpy as np
import cv2
def nothing(x):
    pass

cv2.namedWindow('frame', cv2.WINDOW_NORMAL)  # Create a resizable window named 'frame'
cv2.createTrackbar("LH", "frame", 0, 255, nothing)  # Create trackbar for lower hue
cv2.createTrackbar("LS", "frame", 0, 255, nothing) 
cv2.createTrackbar("LV", "frame", 0, 255, nothing) 
cv2.createTrackbar("UH", "frame", 255, 255, nothing) 
cv2.createTrackbar("US", "frame", 255, 255, nothing) 
cv2.createTrackbar("UV", "frame", 255, 255, nothing) 

while True:
    frame = cv2.imread("bubble.png")  # Load the image


    frame = cv2.resize(frame, (800, 600))  # Resize image to fit window

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert BGR image to HSV color space
    l_h= cv2.getTrackbarPos("LH", "frame")  # Get lower hue value from trackbar
    l_s= cv2.getTrackbarPos("LS", "frame")  # Get lower saturation value from trackbar
    l_v= cv2.getTrackbarPos("LV", "frame")  # Get lower value (brightness) from trackbar
    u_h= cv2.getTrackbarPos("UH", "frame")  # Get upper hue value from trackbar
    u_s= cv2.getTrackbarPos("US", "frame")  # Get upper saturation value from trackbar
    u_v= cv2.getTrackbarPos("UV", "frame")  # Get upper value (brightness) from trackbar

    l_b = np.array([l_h,l_s, l_v])  # Lower bound for blue color in HSV
    u_b = np.array([u_h, u_s, u_v])  # Upper bound for blue color in HSV

    mask = cv2.inRange(hsv, l_b, u_b)  # Create a binary mask where blue colors are white and others are black

    res = cv2.bitwise_and(frame, frame, mask=mask)  # Apply mask to original image to extract only blue parts

    cv2.imshow('frame', frame)  # Show original image
    cv2.imshow('mask', mask)  # Show mask (white = blue areas)
    cv2.imshow('res', res)  # Show result image with only blue areas visible

    KEY=cv2.waitKey(1)# Wait for ESC key to be pressed
    if KEY ==27: # Exit the loop
     break 
cv2.destroyAllWindows()  # Close all OpenCV windows

