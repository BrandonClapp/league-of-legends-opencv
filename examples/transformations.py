import cv2 as cv

capture = cv.VideoCapture('videos/game1.mp4')

while True:
    isTrue, frame = capture.read()

    # Cropping
    h = frame.shape[1]
    w = frame.shape[0]
    
    cropped = frame[w-200:w, h-200:h]
    resized = cv.resize(cropped, (400, 400))

    cv.imshow('Minimap', resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()