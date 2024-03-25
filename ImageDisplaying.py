#Imports necessary packages
import cv2 as cv

def displayImage(frame):
    #Returns the processed frame
    #https://www.geeksforgeeks.org/python-play-a-video-using-opencv/ lines 20 - 23
    cv.imshow("Detected Lines", frame)
    cv.waitKey(1)
