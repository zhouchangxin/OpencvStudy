import cv2 as cv
imsrc = cv.imread('/Users/zhouchangxin/Desktop/opencv-python图像/coins.jpg')
print('test')
cv.namedWindow('input test', cv.WINDOW_AUTOSIZE)
cv.imshow('input test', imsrc)
cv.waitKey(0)
cv.destroyAllWindows()