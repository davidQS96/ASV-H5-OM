
from skimage.io import imread, imshow
import matplotlib.pyplot as plt
import numpy as np

from Modulos.Functions import *
from Modulos.Morfologicos import *


img = imread('Imagenes/ruido.png')
#img = imread('Archivos temp - borrar/imgPrueba2.png')#'Imagenes/ruido.png')

#hist1 = crearHistograma(img, nombreArchivo = "antes", aBorrar = False)

#Aumento de contraste
for row in range(len(img)):
    for pix in range(len(img[row])):
        if img[row][pix] <= 127:
            img[row][pix] = 0

        else:
            img[row][pix] = 255

#hist2 = crearHistograma(img, nombreArchivo = "despues", aBorrar = False)

#Binarizacion 0 y 1
img = img / 255


#Metodo 1---------------------------------------------------------------------------------------------------
#Generacion de elemento estructural
elemStr = generateElemStr({"x": 7, "y": 7}, "diamante")

#Creacion de imagen erosionada
imgNew = erosionTotal(img, elemStr)
print("Erosion lista")

#Finalizacion de apertura
imgNew = dilatacionTotal(imgNew, elemStr)
print("Dilatacion lista")

#Creacion de dilatacion
imgNew = dilatacionTotal(imgNew, elemStr)
print("Dilatacion lista")

#Finalizacion de reduccion de ruido
imgNew = erosionTotal(imgNew, elemStr)
print("Erosion lista")




#print(img)

#plt.clear()

plt.imshow(imgNew,cmap='gray',vmin=0,vmax=1)
plt.title('Binaria')

plt.show()
