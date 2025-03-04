import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import os
import cv2
import numpy as np
from time import time



def FCM(image_AMF):
    list_img = []
    img = cv2.imread("images/"+str(image_AMF))
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rgb_img = img.reshape((img.shape[0] * img.shape[1], 3))
    list_img.append(rgb_img)
    n_data = len(list_img)
    clusters = [2]

    # looping every images
    for index, rgb_img in enumerate(list_img):
        img = np.reshape(rgb_img, (256, 256, 3)).astype(np.uint8)
        shape = np.shape(img)

        # initialize graph
        #plt.figure(figsize=(20, 20))
        #plt.subplot(1, 4, 1)
        #plt.imshow(img)
        # looping every cluster
        print('Image ' + str(index + 1))
        for i, cluster in enumerate(clusters):
            # Fuzzy C Means
            new_time = time()

            # error = 0.005
            # maximum iteration = 1000
            # cluster = 2,3,6,8

            cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
                rgb_img.T, cluster, 2, error=0.005, maxiter=1000, init=None, seed=42)

            new_img = change_color_fuzzycmeans(u, cntr)

            fuzzy_img = np.reshape(new_img, shape).astype(np.uint8)

            #print("size", np.max(fuzzy_img))

            ret, seg_img = cv2.threshold(fuzzy_img, np.max(fuzzy_img) - 1, 255, cv2.THRESH_BINARY)
            #cv2.imwrite('images/fuzzy.jpg', seg_img.astype(np.uint8))

            print('Fuzzy time for cluster', cluster)
            print(time() - new_time, 'seconds')
            seg_img_1d = seg_img[:, :, 1]

           # cv2.imwrite('images/k.jpg', seg_img_1d.astype(np.uint8))

            bwfim1 = bwareaopen(seg_img_1d, 500)
            #cv2.imwrite('images/border11.jpg', bwfim1)
            bwfim2 = imclearborder(bwfim1)
            #cv2.imwrite('images/border.jpg', bwfim2)
            bwfim3 = imfill(bwfim2)
            cv2.imwrite('images/FCM.jpg', bwfim3)
            print('Bwarea : ' + str(bwarea(bwfim3)))
            print()
            #plt.subplot(1, 4, i + 2)
            #plt.imshow(bwfim3)
            #plt.show()
            #name = 'Cluster' + str(cluster)
            #plt.title(name)

        #name = 'segmented' + str(index) + '.png'
        #plt.savefig(name)
        #print()
        return bwfim3

def change_color_fuzzycmeans(cluster_membership, clusters):
    img = []
    for pix in cluster_membership.T:
        img.append(clusters[np.argmax(pix)])
    return img


def bwarea(img):
    row = img.shape[0]
    col = img.shape[1]
    total = 0.0
    for r in range(row - 1):
        for c in range(col - 1):
            sub_total = img[r:r + 2, c:c + 2].mean()
            if sub_total == 255:
                total += 1
            elif sub_total == (255.0 / 3.0):
                total += (7.0 / 8.0)
            elif sub_total == (255.0 / 4.0):
                total += 0.25
            elif sub_total == 0:
                total += 0
            else:
                r1c1 = img[r, c]
                r1c2 = img[r, c + 1]
                r2c1 = img[r + 1, c]
                r2c2 = img[r + 1, c + 1]

                if (((r1c1 == r2c2) & (r1c2 == r2c1)) & (r1c1 != r2c1)):
                    total += 0.75
                else:
                    total += 0.5
    return total


def imclearborder(imgBW):
    # Given a black and white image, first find all of its contours
    radius = 2
    imgBWcopy = imgBW.copy()
    contours, hierarchy = cv2.findContours(imgBWcopy.copy(), cv2.RETR_LIST,
                                                  cv2.CHAIN_APPROX_SIMPLE)

    # Get dimensions of image
    imgRows = imgBW.shape[0]
    imgCols = imgBW.shape[1]

    contourList = []  # ID list of contours that touch the border

    # For each contour...
    for idx in np.arange(len(contours)):
        # Get the i'th contour
        cnt = contours[idx]

        # Look at each point in the contour
        for pt in cnt:
            rowCnt = pt[0][1]
            colCnt = pt[0][0]

            # If this is within the radius of the border
            # this contour goes bye bye!
            check1 = (rowCnt >= 0 and rowCnt < radius) or (rowCnt >= imgRows - 1 - radius and rowCnt < imgRows)
            check2 = (colCnt >= 0 and colCnt < radius) or (colCnt >= imgCols - 1 - radius and colCnt < imgCols)

            if check1 or check2:
                contourList.append(idx)
                break

    for idx in contourList:
        cv2.drawContours(imgBWcopy, contours, idx, (0, 0, 0), -1)

    return imgBWcopy


#### bwareaopen definition
def bwareaopen(imgBW, areaPixels):
    # Given a black and white image, first find all of its contours
    imgBWcopy = imgBW.copy()
    contours, hierarchy = cv2.findContours(imgBWcopy.copy(), cv2.RETR_LIST,
                                                  cv2.CHAIN_APPROX_SIMPLE)

    # For each contour, determine its total occupying area
    for idx in np.arange(len(contours)):
        area = cv2.contourArea(contours[idx])
        if (area >= 0 and area <= areaPixels):
            cv2.drawContours(imgBWcopy, contours, idx, (0, 0, 0), -1)

    return imgBWcopy


def imfill(im_th):
    im_floodfill = im_th.copy()
    # Mask used to flood filling.

    # Notice the size needs to be 2 pixels than the image.
    h, w = im_th.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0, 0), 255);
    #cv2.imwrite('images/flood.jpg', im_floodfill)
    # Invert floodfilled image
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    #cv2.imwrite('images/flood1.jpg', im_floodfill_inv)
    #cv2.imwrite('images/imth.jpg', im_th)

    # Combine the two images to get the foreground.
    im_out = im_th | im_floodfill_inv
    #cv2.imwrite('images/im_out.jpg', im_out)

    return im_out


#FCM("AMF.jpg")