

import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte
from skimage import data
from skimage.exposure import histogram
from skimage.io import imread
from skimage import filters
from skimage.morphology import disk, octagon, erosion, dilation

opcion = 1
tamaño = 15
img = imread('circunferencias.png')
noisy_image = rgb2gray(img)
binaria = 0.25 <= noisy_image
binaria = ~binaria

if opcion == 0:
    erosionada = erosion(binaria, disk(tamaño))
    imagen_final = dilation(erosionada, disk(tamaño))
if opcion == 1:
    erosionada = erosion(binaria, octagon(tamaño,int(tamaño/2)))
    imagen_final = dilation(erosionada, octagon(tamaño,int(tamaño/2)))


plt.imshow(binaria,cmap='gray',vmin=0,vmax=1)
plt.title('Binaria')
plt.show()
plt.imshow(imagen_final,cmap='gray',vmin=0,vmax=1)
plt.title('Tratada')
plt.show()