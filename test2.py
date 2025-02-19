import numpy as np
import cv2
import math
from skimage import exposure as ex
import sys
def AdaptiveMedianFilter(grayimage):
    try:
        img_out = grayimage.copy()

        height = grayimage.shape[0]
        width = grayimage.shape[1]

        for i in np.arange(5, height - 5):
            for j in np.arange(5, width - 5):
                neighbors = []
                for k in np.arange(-6, 6):
                    for l in np.arange(-6, 6):
                        a = grayimage.item(i + k, j + l)
                        neighbors.append(a)
                neighbors.sort()
                median = neighbors[24]
                b = median
                img_out.itemset((i, j), b)

        cv2.imwrite('images/threshld.jpg', img_out.astype(np.uint8))
        cv2.imshow('image', img_out)
        cv2.waitKey(0)
        # cv2.destroyAllWindows()

    except Exception as e:
        print("Error=" + e.args[0])
        tb = sys.exc_info()[2]
        print(tb.tb_lineno)
    return img_out.astype(np.uint8)



# Adaptive Median Filter by CV2
'''import cv2

img = cv2.imread('images/image5.jpg') # Load image
img_median = cv2.medianBlur(img, 5) # Add median filter to image

cv2.imshow('img', img_median) # Display img with median filter
cv2.waitKey(0)        # Wait for a key press to
cv2.destroyAllWindows # close the img window.'''

image = cv2.imread('images/threshld.jpg')  # READ THE INPUT IMAGE
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
AdaptiveMedianFilter(gray_image)




