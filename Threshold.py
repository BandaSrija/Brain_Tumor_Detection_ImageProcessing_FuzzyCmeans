import cv2
from matplotlib import pyplot as plt

image = cv2.imread('images/BCET.jpg')
#brain = cv2.imread('images/border1.jpg')
blur = cv2.GaussianBlur(image,(5,5),0)

T, thresh_f =  cv2.threshold(blur,200,255,cv2.THRESH_BINARY)
cv2.imshow("canny",thresh_f)
cv2.imwrite('images/th.jpg', thresh_f)
cv2.waitKey()

img = cv2.imread('images/th.jpg') # Load image
img_median = cv2.medianBlur(img, 5)
cv2.imshow("img_median",img_median)
'''img = cv2.addWeighted(brain, 0.5, thresh_f, 0.7, 0)
detected_edges = cv2.Canny(img, 10, 10*3, 5)

plt.subplot(1,3,1),plt.imshow(thresh_f,cmap = 'gray')
plt.title('Threshold'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(img,cmap = 'gray')
plt.title('Segmented'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(img,cmap = 'RdYlGn')
plt.title('OUTPUT'), plt.xticks([]), plt.yticks([])
plt.show()
colour = cv2.applyColorMap(img, cv2.COLORMAP_JET)
cv2.imshow("canny",detected_edges)
cv2.imshow("final",img)
cv2.imshow("color",colour)
cv2.waitKey()'''