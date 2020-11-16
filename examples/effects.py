import cv2 as cv

# # Reading images
# img = cv.imread('images/map1.png')
# cv.imshow('Map', img)

# Reading videos
# capture = cv.VideoCapture(0) # can do this to capture a webcam
capture = cv.VideoCapture('videos/game1.mp4')

while True:
    isTrue, frame = capture.read()
    # Grayscale
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Blur
    # blur = cv.GaussianBlur(frame, (3, 3), cv.BORDER_DEFAULT)

    # # Edge Cascade (edges)
    # canny = cv.Canny(blur, 125, 175)

    # # Dilating the image
    # dilated = cv.dilate(canny, (7, 7), iterations=3)

    # # Eroding
    # eroded = cv.erode(dilated, (7, 7), iterations=1)

    # Resizing (ignores aspect ration - causes stretching)
    # resized = cv.resize(frame, (500, 500))

    # Cropping
    h = frame.shape[1]
    w = frame.shape[0]
    
    cropped = frame[w-200:w, h-200:h]
    resized = cv.resize(cropped, (400, 400))

    cv.imshow('Video', resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


# cv.waitKey(0)