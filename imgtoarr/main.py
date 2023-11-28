import os
from fuction222 import *
print('Setting UP')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
pathImage = '/Users/zsu/mysite/imgtoarr/sudoku_capture.png'

img = cv2.imread(pathImage)

heightImg = 720
widthImg = 720
model = intializePredectionModel()


img = cv2.imread(pathImage)
img = cv2.resize(img,(widthImg,heightImg))
imgThreshold = preProcess(img)
contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

imgContours = img.copy()
imgBigContour = img.copy()

biggest, maxArea = biggestContour(contours)
if biggest.size != 0:
    biggest = reorder(biggest)
    cv2.drawContours(imgBigContour, biggest, -1, (0, 0, 255), 20)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgWarpBinary = cv2.warpPerspective(imgThreshold, matrix, (widthImg, heightImg))

    boxes = splitBoxes(imgWarpBinary)

    numbers = getPredection(boxes, model)

    numbers = np.asarray(numbers)
    print(numbers)