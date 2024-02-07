import cv2
import numpy as np

img = cv2.imread('Fig0219(rose1024).tif')

# # 128x128 resample 
# img = cv2.resize(img, (128, 128))
# img = cv2.resize(img, (1024, 1024))

# cv2.imwrite("result of 128.tif", img)
# cv2.imshow('resampling', img)
# cv2.waitKey()

# print(img.shape)

# # 64x64 resample 
# img = cv2.resize(img, (64, 64))
# img = cv2.resize(img, (1024, 1024))

# cv2.imwrite("result of 64.tif", img)
# cv2.imshow('resampling', img)
# cv2.waitKey()

# print(img.shape)

# 32x32 resample 
img = cv2.resize(img, (32, 32))
img = cv2.resize(img, (1024, 1024))

cv2.imwrite("result of 32.tif", img)
cv2.imshow('resampling', img)
cv2.waitKey()

print(img.shape)