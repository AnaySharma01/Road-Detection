# Imports necessary packages
import cv2 as cv
import numpy as np


def processImage(image):
    # Applies gaussian blur, median blur, and canny edge detection on the image
    # https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Lines 35-38
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray_scale = cv.GaussianBlur(gray, (15, 15), 0)
    median_blur = cv.medianBlur(gray_scale, 5)
    canny_image = cv.Canny(median_blur, 75, 20)
    # Creates a mask around desired area
    # https://pyimagesearch.com/2021/01/19/image-masking-with-opencv/ Lines 20-26
    roi = np.zeros(image.shape[:2], dtype="uint8")
    cv.rectangle(roi, (1300, 1800), (2100, 2100), 1, -1)
    mask = cv.bitwise_and(canny_image, canny_image, mask=roi)
    # Displays the mask
    # cv.rectangle(image, (1300, 1800), (2100, 2100), (255, 0, 0), 5)

    # Detects the contours
    # https://www.tutorialspoint.com/opencv_python/opencv_python_image_contours.htm Line 10
    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    # Prevents program from crashing if no contours detected
    if len(contours) > 0:
        # Displays the contours
        # https://www.tutorialspoint.com/opencv_python/opencv_python_image_contours.htm Line 15
        cv.drawContours(image, contours, -1, (0, 255, 0), 5)
        # Finds minimum length of contours
        # https://www.geeksforgeeks.org/python-length-of-shortest-string-in-string-list/ Method 1 Line 13
        min_length = min(len(cnt) for cnt in contours)

        # Calculates the average of the contour points
        # https://www.geeksforgeeks.org/numpy-mean-in-python/ Code 2 Line 15
        midpoint_x_arr = np.mean([contour[:, 0, :][:min_length][:, 0] for contour in contours], axis=0).astype(int)
        midpoint_y_arr = np.mean([contour[:, 0, :][:min_length][:, 1] for contour in contours], axis=0).astype(int)

        # Displays the centerline
        # https://www.geeksforgeeks.org/python-opencv-cv2-line-method/ Example 1 Line 33
        for i in range(len(midpoint_x_arr) - 1):
            cv.line(image, (midpoint_x_arr[i], midpoint_y_arr[i]), (midpoint_x_arr[i + 1], midpoint_y_arr[i + 1]),
                    (0, 0, 255), 5)

        # https://www.geeksforgeeks.org/draw-a-triangle-with-centroid-using-opencv/
        # Sets the points of the arrows
        point1 = (700, 900)
        point2 = (1400, 1500)
        point3 = (500, 1500)
        # Draws the triangle with the points
        cv.line(image, point1, point2, (255, 0, 0), 3)
        cv.line(image, point2, point3, (255, 0, 0), 3)
        cv.line(image, point1, point3, (255, 0, 0), 3)

        # https://www.geeksforgeeks.org/python-opencv-cv2-arrowedline-method/?ref=lbp
        # Creates the start and end point
        start_point = (900, 1000)
        end_point = (900, 200)
        # Red color in BGR
        color = (255, 0, 0)
        # Sets the thickness of the arrow
        thickness = 5
        # Draws the arrow
        cv.arrowedLine(image, start_point, end_point,
                       color, thickness, tipLength=0.5)
