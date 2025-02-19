import numpy as np
import cv2

def BalanceContrastEnhancementTechnique(gray_image):
    #I = cv2.imread('images/filter_median.jpg')  # READ THE INPUT IMAGE
    x = im2double(gray_image)  # INPUT IMAGE
    Lmin = np.min(x.ravel()) # MINIMUM OF INPUT IMAGE
    Lmax =np.max(x.ravel())  # MAXIMUM OF INPUT IMAGE
    Lmean = np.mean(x)       # MEAN OF INPUT IMAGE
    LMssum = np.mean(pow(x,2))  # MEAN SQUARE SUM OF INPUT IMAGE

    Gmin = 0   # MINIMUM OF OUTPUT IMAGE
    Gmax = 255  # MAXIMUM OF OUTPUT IMAGE
    Gmean =85 # MEAN OF OUTPUT IMAGE 80 (Recomended)

    bnum = pow(Lmax,2) * (Gmean - Gmin) - LMssum * (Gmax - Gmin) + pow(Lmin,2) * (Gmax - Gmean)
    bden = 2 * (Lmax * (Gmean - Gmin) - Lmean * (Gmax - Gmin) + Lmin * (Gmax - Gmean))

    b = bnum / bden

    a = (Gmax - Gmin) / ((Lmax - Lmin) * (Lmax + Lmin - 2 * b))

    c = Gmin - a *  pow((Lmin - b), 2)

    y = a *pow((x - b),2)+ c  # PARABOLIC FUNCTION
    y = y.astype(np.uint8)

    cv2.imwrite('images/BCET.jpg', y)
    #cv2.imshow('image', y)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    return y



def im2double(im):
    min_val = np.min(im.ravel())
    max_val = np.max(im.ravel())
    out = (im.astype('float') - min_val) / (max_val - min_val)
    return out

'''image = cv2.imread('images/resize.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
BalanceContrastEnhancementTechnique(gray_image)'''