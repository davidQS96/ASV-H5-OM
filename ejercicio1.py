
import cv2
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.io import imread
from skimage.morphology import disk, octagon, square,star,erosion, dilation

#Variables basicas
opcion = 3
tamaño = 10
img = imread('circunferencias.png')
noisy_image = rgb2gray(img)
binaria = 0.25 <= noisy_image
binaria = ~binaria

# Erosion y dilatación
if opcion == 0:
    erosionada = erosion(binaria, disk(tamaño))
    imagen_final = dilation(erosionada, disk(tamaño))
if opcion == 1:
    erosionada = erosion(binaria, octagon(tamaño,int(tamaño/2)))
    imagen_final = dilation(erosionada, octagon(tamaño,int(tamaño/2)))
if opcion == 2:
    erosionada = erosion(binaria, square(tamaño))
    imagen_final = dilation(erosionada, square(tamaño))
if opcion == 3:
    erosionada = erosion(binaria, star(tamaño))
    imagen_final = dilation(erosionada, star(tamaño))

#Gaurdado de imagenes    
plt.imshow(binaria,cmap='gray',vmin=0,vmax=1)
plt.title('Binaria')
plt.show()
plt.imshow(erosionada,cmap='gray',vmin=0,vmax=1)
plt.title('Tratada')
plt.show()
plt.imshow(imagen_final,cmap='gray',vmin=0,vmax=1)
plt.title('Tratada')
plt.show()
cv2.imwrite('imagen.png',imagen_final)