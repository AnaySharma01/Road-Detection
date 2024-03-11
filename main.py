#Imports necessary packages
import ImageReading
import ImageProcessing
import ImageDisplaying

#Loads the image
file = "RoadDetectionVideo.mp4"
frame = ImageReading.readImage(file)

#Applies image detection
ImageProcessing.processImage(frame)

#Displays image with hough lines
ImageDisplaying.displayImage(frame)
