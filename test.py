
import cv2
import numpy as np
'''img = cv2.imread('images/resize.jpg') # Load image
img_median = cv2.medianBlur(img, 5) # Add median filter to image

cv2.imshow('img', img_median) # Display img with median filter
cv2.imwrite('images/AMF.jpg', img_median.astype(np.uint8))
cv2.waitKey(0)        # Wait for a key press to
cv2.destroyAllWindows # close the img window.'''

image = cv2.imread("Y7.jpg")  # READ THE INPUT IMAGE
#image = cv2.resize(image, (256, 256), interpolation=cv2.INTER_AREA)
print(image.shape)
#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#print("Resize=", gray_image.shape)
#cv2.imwrite('images/gray.jpg', image)



img = cv2.imread('images/BCET.jpg',0)
blur = cv2.GaussianBlur(img,(5,5),0)
hist = cv2.calcHist([blur],[0],None,[256],[0,256])
hist_norm = hist.ravel()/hist.max()
Q = hist_norm.cumsum()
bins = np.arange(256)
fn_min = np.inf
thresh = -1
for i in range(1,256):
        p1,p2 = np.hsplit(hist_norm,[i]) # probabilities
        q1,q2 = Q[i],Q[255]-Q[i] # cum sum of classes
        b1,b2 = np.hsplit(bins,[i]) # weights

        m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
        v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2

        # calculates the minimization function
        fn = v1*q1 + v2*q2
        if fn < fn_min:
            fn_min = fn
            thresh = i

# find otsu's threshold value with OpenCV function
ret, otsu = cv2.threshold(blur,200,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("otsu",otsu)
cv2.waitKey()
#print thresh,ret