import cv2 as cv

# Reading images
# img = cv.imread('images/map1.png')
# cv.imshow('Map', img)

def rescaleFrame(frame, scale=0.75):
    # Images, video, & Live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    # resize the frame to a particular dimension
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture('videos/game1.mp4')

while True:
    isTrue, frame = capture.read()

    resized = rescaleFrame(frame, 1)
    cv.imshow('Video', resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
