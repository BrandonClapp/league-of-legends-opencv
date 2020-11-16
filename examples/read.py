import cv2 as cv

# # Reading images
# img = cv.imread('images/map1.png')
# cv.imshow('Map', img)

# Reading videos
# capture = cv.VideoCapture(0) # can do this to capture a webcam
capture = cv.VideoCapture('videos/game1.mp4')

while True:
    isTrue, frame = capture.read()
    
    # cv.circle(frame, (frame.shape[1]//2, frame.shape[0]//2), 40, (0, 255, 0), thickness=3)
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


# cv.waitKey(0)