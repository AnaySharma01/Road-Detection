# Imports necessary packages
import cv2 as cv
import numpy as np
def processImage(image):
    # Applies gaussian blur, median blur, and canny edge detection on the image
    # https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Lines 35-38
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray_scale = cv.GaussianBlur(gray, (15, 15), 0)
    median_blur = cv.medianBlur(gray_scale, 5)
    canny_image = cv.Canny(median_blur, 100, 20)
    # https://www.geeksforgeeks.org/python-opencv-cv2-polylines-method/ #Lines 19-38
    # Creates coordinates of mask
    points = np.array([[1000, 2100], [2200, 2100], [1700, 1500], [1700, 1500]],
    points = np.array([[800, 2100], [2300, 2100], [1800, 1500], [1600, 1500]],
                      np.int32)
    points = points.reshape((-1, 1, 2))
    # Displays the mask
    cv.polylines(image, [points],
                 True, (0, 255, 0), 5)
    # Creates a mask around desired area
    # https://pyimagesearch.com/2021/01/19/image-masking-with-opencv/ Lines 20-26
    roi = np.zeros(image.shape[:2], dtype="uint8")
    cv.polylines(roi, [points],
                 True, (0, 255, 0), 5)
    cv.rectangle(roi, (1200, 1800), (2100, 2100), 1, -1)
    mask = cv.bitwise_and(canny_image, canny_image, mask=roi)

    # Displays the mask
    cv.rectangle(image, (1200, 1800), (2100, 2100), (255, 0, 0), 5)
    # cv.rectangle(image, (1200, 1800), (2100, 2100), (255, 0, 0), 5)

    # Creates hough lines around image
    # Creates the hough lines used for the line detection
    # https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Line 42
    lines = cv.HoughLinesP(mask, 1, np.pi / 180, threshold=10, minLineLength=10, maxLineGap=15)

    # Displays hough lines

    # https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Line 14-19

    # Prevents program from crashing if no lines detected
    if lines is not None:
        # Variables needed to find the centerline
        slope_arr = []
        lines_list = []
        for line in lines:
            # Creates array of lines
            x1, y1, x2, y2 = line[0]
            lines_list.append(line[0])
            # Displays the lines
            cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 10)
            # https://www.geeksforgeeks.org/program-find-slope-line/ Line 4
            # Calculates the slopes of the lines
            slope = 0
            if x2 - x1 != 0:
                slope = (y2 - y1) / (x2 - x1)
            slope_arr.append(slope)
        # https://www.geeksforgeeks.org/python-nested-loops/ Example 2 Lines 3 and 7
        # Loops through the slope array to calculate the centerline
        for i in range(len(slope_arr)):
            for j in range(len(slope_arr)):
                x1, y1, x2, y2 = lines_list[i]
                x3, y3, x4, y4 = lines_list[j]
                # Calculates and displays the centerline
                cv.line(image, ((x1 + x3) // 2, (y1 + y3) // 2), ((x2 + x4) // 2, (y2 + y4) // 2), (255, 0, 0), 5)
