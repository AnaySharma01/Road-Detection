# Imports necessary packages
import cv2 as cv

# Imports function for reading images
import ImageProcessing
import ImageDisplaying


def readImage(image):
    # https://geeksforgeeks.org/python-play-a-video-using-opencv/ lines 15 - 20
    # Variable needed for displaying the video
    videoIsPlaying = True

    # Starts the video capture
    video = cv.VideoCapture(image)

    # Prevents program from crashing error
    # try:
    # While the video is playing, read the frame, process it & display it
    while videoIsPlaying:
        videoIsPlaying, frame = video.read()
        ImageProcessing.processImage(frame)
        ImageDisplaying.displayImage(frame)
    cv.destroyAllWindows()

# Prints message when video is done
# except: print("The video is done.")
# finally: exit()
