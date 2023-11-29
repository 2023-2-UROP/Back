# import os
# from fuction222 import *
# # print('Setting UP')
# cv2.setUseOptimized(True)
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# pathImage = 'imgtoarr/sudoku_capture.png'
#
# img = cv2.imread(pathImage)
#
# heightImg = 720
# widthImg = 720
# model = intializePredectionModel()
#
#
# img = cv2.resize(img,(widthImg,heightImg))
# imgThreshold = preProcess(img)
# contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# imgContours = img.copy()
# imgBigContour = img.copy()
#
# biggest, maxArea = biggestContour(contours)
# if biggest.size != 0:
#     biggest = reorder(biggest)
#     cv2.drawContours(imgBigContour, biggest, -1, (0, 0, 255), 20)
#     pts1 = np.float32(biggest)
#     pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
#     matrix = cv2.getPerspectiveTransform(pts1, pts2)
#     imgWarpBinary = cv2.warpPerspective(imgThreshold, matrix, (widthImg, heightImg))
#
#     boxes = splitBoxes(imgWarpBinary)
#
#     numbers = getPredection(boxes, model)
#
#     # numbers = np.asarray(numbers)
#     # print("numbers= {}".format(numbers))
#     narr = "numbers= {}".format(numbers)
#     print(narr)

# import os
# from fuction222 import *
# import cv2
# import numpy as np
# image_path = 'imgtoarr/sudoku_capture.png'
# def img_make_arr(image_path):
#     # Set up
#     cv2.setUseOptimized(True)
#     os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
#
#     # Read image
#     img = cv2.imread(image_path)
#     height_img = 720
#     width_img = 720
#     model = intializePredectionModel()
#
#     img = cv2.resize(img, (width_img, height_img))
#     img_threshold = preProcess(img)
#     contours, hierarchy = cv2.findContours(img_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     img_big_contour = img.copy()
#
#     biggest, max_area = biggestContour(contours)
#     if biggest.size != 0:
#         biggest = reorder(biggest)
#         cv2.drawContours(img_big_contour, biggest, -1, (0, 0, 255), 20)
#         pts1 = np.float32(biggest)
#         pts2 = np.float32([[0, 0], [width_img, 0], [0, height_img], [width_img, height_img]])
#         matrix = cv2.getPerspectiveTransform(pts1, pts2)
#         img_warp_binary = cv2.warpPerspective(img_threshold, matrix, (width_img, height_img))
#
#         boxes = splitBoxes(img_warp_binary)
#
#         numbers = getPredection(boxes, model)
#
#         return numbers

# result_numbers = img_make_arr(image_path)

import os
from fuction222 import *
import cv2
import numpy as np
image_path = 'imgtoarr/sudoku_capture.png'
# pathImage = '/Users/zsu/PycharmProjects/pythonProject2/sudoku_capture.png'
def img_make_arr(image_path):
    # Set up
    cv2.setUseOptimized(True)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    # Read image
    img = cv2.imread(image_path)
    height_img = 720
    width_img = 720
    model = intializePredectionModel()

    img = cv2.resize(img, (width_img, height_img))
    img_threshold = preProcess(img)
    contours, hierarchy = cv2.findContours(img_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    img_big_contour = img.copy()

    biggest, max_area = biggestContour(contours)
    if biggest.size != 0:
        biggest = reorder(biggest)
        cv2.drawContours(img_big_contour, biggest, -1, (0, 0, 255), 20)
        pts1 = np.float32(biggest)
        pts2 = np.float32([[0, 0], [width_img, 0], [0, height_img], [width_img, height_img]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        img_warp_binary = cv2.warpPerspective(img_threshold, matrix, (width_img, height_img))

        boxes = splitBoxes(img_warp_binary)

        numbers = getPredection(boxes, model)

        return numbers

print(img_make_arr(pathImage))
