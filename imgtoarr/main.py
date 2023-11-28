import os
from fuction222 import *
print('Setting UP')
cv2.setUseOptimized(True)
# cv2.setImreadModes(['cv2.IMREAD_UNCHANGED', 'cv2.IMREAD_COLOR', 'cv2.IMREAD_GRAYSCALE', 'cv2.IMREAD_ANYDEPTH', 'cv2.IMREAD_ANYCOLOR', 'cv2.IMREAD_LOAD_GDAL', 'cv2.IMREAD_REDUCED_GRAYSCALE_2', 'cv2.IMREAD_REDUCED_COLOR_2', 'cv2.IMREAD_REDUCED_GRAYSCALE_4', 'cv2.IMREAD_REDUCED_COLOR_4', 'cv2.IMREAD_REDUCED_GRAYSCALE_8', 'cv2.IMREAD_REDUCED_COLOR_8'])
# cv2.setImwriteFlags(['cv2.IMWRITE_JPEG_QUALITY', 'cv2.IMWRITE_JPEG_PROGRESSIVE', 'cv2.IMWRITE_JPEG_OPTIMIZE', 'cv2.IMWRITE_JPEG_RST_INTERVAL', 'cv2.IMWRITE_JPEG_LUMA_QUALITY', 'cv2.IMWRITE_JPEG_CHROMA_QUALITY', 'cv2.IMWRITE_PNG_COMPRESSION', 'cv2.IMWRITE_PNG_STRATEGY', 'cv2.IMWRITE_PNG_BILEVEL', 'cv2.IMWRITE_PNG_STRATEGY_DEFAULT', 'cv2.IMWRITE_PNG_STRATEGY_FILTERED', 'cv2.IMWRITE_PNG_STRATEGY_HUFFMAN_ONLY', 'cv2.IMWRITE_PNG_STRATEGY_RLE', 'cv2.IMWRITE_PNG_STRATEGY_FIXED'])
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
pathImage = 'imgtoarr/sudoku_capture.png'

img = cv2.imread(pathImage)

heightImg = 720
widthImg = 720
model = intializePredectionModel()


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