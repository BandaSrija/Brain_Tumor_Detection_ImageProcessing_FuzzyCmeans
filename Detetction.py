import cv2
import imutils
import numpy as np
from AMF import AdaptiveMedianFilter
from BCET import BalanceContrastEnhancementTechnique
#from FuzzyClustering import FCM
def read():
    image = cv2.imread('images/image5.jpg')  # READ THE INPUT IMAGE
    image=cv2.resize(image,(256, 256),interpolation=cv2.INTER_AREA)
    print(image.shape)
    cv2.imwrite('images/resize.jpg',image)
    #cv2.imshow("img",image)
    #cv2.waitKey(0)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(gray_image.shape)

    # Adaptive Median Filter
    #image_amf = AdaptiveMedianFilter(gray_image)

    # Balance Contrast Enhancement Technique
    #image_bcet=BalanceContrastEnhancementTechnique(gray_image)

    # Otsu's thresholding
    #ret2, th2 = cv2.threshold(image_bcet, 200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    #cv2.imwrite('images/OTSU.jpg', th2.astype(np.uint8))

    #Fuzzy C-means
    #FCM(image_amf)









read()