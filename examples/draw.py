import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('blank', blank)

# Paint the image a certain color
# blank[:] = 0, 255, 0 # Make all of the pixels green
# cv.imshow('Green', blank)

# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
# cv.imshow('Rect', blank)

cv.circle(blank, (250, 250), 40, (0, 255, 0), thickness=3)
cv.imshow('Circle', blank)

cv.waitKey(0)