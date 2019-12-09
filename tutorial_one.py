import cv2 as cv
import numpy as np

def image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)

def video_demo():
    capture = cv.VideoCapture('/Users/zhouchangxin/Desktop/opencvtest.mp4')
    while(True):
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if 27 == c:
            break

imsrc = cv.imread('/Users/zhouchangxin/Desktop/opencv-python图像/coins.jpg')

cv.namedWindow('input test', cv.WINDOW_AUTOSIZE)
cv.imshow('input test', imsrc)
#image_info(imsrc)
video_demo()
cv.waitKey(0)
cv.destroyAllWindows()