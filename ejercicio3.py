
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte
from skimage import data
from skimage.exposure import histogram
from skimage.io import imread
from skimage import filters
from skimage.morphology import disk, octagon, erosion, dilation

# Variables
img = imread('estructura.png')
img = rgb2gray(img)
imgray = 0.88 <= img
h,b = img.shape
elem = h*b

#Patrones
b2 = np.array([[1,2,0],[1,0,0],[1,2,0]])
b1 = np.array([[0,2,1],[0,0,1],[0,2,1]])
b4 = np.array([[0,0,0],[2,0,2],[1,1,1]])
b3 = np.array([[1,1,1],[2,0,2],[0,0,0]])
b7 = np.array([[0,0,2],[0,0,1],[2,1,1]])
b8 = np.array([[2,1,1],[0,0,1],[0,0,2]])
b5 = np.array([[1,1,2],[1,0,0],[2,0,0]])
b6 = np.array([[2,0,0],[1,0,0],[1,1,2]])

altb1 = np.array([[1,0,0],[1,0,1],[0,1,1]])
altb2 = np.array([[0,0,1],[0,0,1],[1,1,0]])
altb3 = np.array([[0,1,0],[1,0,1],[0,1,0]])
altb4 = np.array([[0,1,0],[0,1,0],[1,0,1]])


# Algoritmo de adelgazamiento
def skeleton(img,fig,h,b,ver):
    i = 1
    j = 1
    cimg = img.copy()
    while True:
        while True:
            if cimg[j,i] == 0:
                l_y_s = j-1
                l_y_i = j+2
                l_x_s = i-1
                l_x_i = i+2
                
                a = cimg[l_y_s:l_y_i,l_x_s:l_x_i]
    
                c = a == fig
                count = np.sum(c==1)
                if count == ver:
                    img[j,i] = 1
                
            j = j+1
            if j == (h-1):
                break
        j = 1
        i = i+1
        if i == (b-1):
            break
    return img


# Loop de 8 patrones        
def ske_loop(img,b1,b2,b3,b4,b5,b6,b7,b8,h,b,ver1,ver2):
    pro1 = skeleton(img,b1,h,b,ver1)
    pro2 = skeleton(pro1,b2,h,b,ver1)
    pro3 = skeleton(pro2,b3,h,b,ver1)
    pro4 = skeleton(pro3,b4,h,b,ver1)
    pro5 = skeleton(pro4,b5,h,b,ver2)
    pro6 = skeleton(pro5,b6,h,b,ver2)
    pro7 = skeleton(pro6,b7,h,b,ver2)
    pro8 = skeleton(pro7,b8,h,b,ver2)
    return pro8

# Loop de 6 patrones  
def ske_loop2(img,b1,b2,b3,b4,b5,b6,h,b,ver1):
    pro1 = skeleton(img,b1,h,b,ver1)
    pro2 = skeleton(pro1,b2,h,b,ver1)
    pro3 = skeleton(pro2,b3,h,b,ver1)
    pro4 = skeleton(pro3,b4,h,b,ver1)
    pro5 = skeleton(pro4,b5,h,b,ver1)
    pro6 = skeleton(pro5,b6,h,b,ver1)
    return pro6


pritera = ske_loop(imgray,b1,b2,b3,b4,b5,b6,b7,b8,h,b,9,7)
res = pritera.copy()

#Iteración hasta no haber cambios
plt.imshow(pritera,cmap='gray',vmin=0,vmax=2)
plt.title('Uno')
plt.show()
cuenta = 0
while True:
    pritera = ske_loop(imgray,altb1,altb2,altb3,altb4,b5,b6,b7,b8,h,b,9,7)
    #pritera = ske_loop2(imgray,b1,b2,b5,b6,b7,b8,h,b,7)
    plt.imshow(pritera,cmap='gray',vmin=0,vmax=2)
    plt.title('Dos')
    plt.show()
    print("C",cuenta)
    c = pritera == res
    count = np.sum(c==1)
    res = pritera.copy()
    if count == elem:
        break
pritera = pritera*255 
plt.imshow(pritera,cmap='gray',vmin=0,vmax=2)
plt.title('Dos')
plt.show()
cv2.imwrite('imagen.png',pritera)