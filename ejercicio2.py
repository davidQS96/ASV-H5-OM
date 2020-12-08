
from skimage.io import imread, imshow
import matplotlib.pyplot as plt
import numpy as np

from Modulos.Functions import *


img = imread('Imagenes/ruido.png')
#img = imread('Archivos temp - borrar/imgPrueba2.png')#'Imagenes/ruido.png')

#hist1 = crearHistograma(img, nombreArchivo = "antes", aBorrar = False)


for row in range(len(img)):
    for pix in range(len(img[row])):
        if img[row][pix] <= 127:
            img[row][pix] = 0

        else:
            img[row][pix] = 255

#hist2 = crearHistograma(img, nombreArchivo = "despues", aBorrar = False)

#Binarizacion 0 y 1
img = img / 255

#Generacion de elemento estructural
elemStr = np.asarray([[1, 1, 1, 1],
                      [1, 1, 1, 1],
                      [1, 1, 1, 1]])


#Funcion para realizar una erosión completa de una imágen
#Retorna una copia de la imagen original, modificada con la op. de erosión
#img es una imágen de tipo ndarray 2d
#elemStr es el elemento estructural a utilizar en la operación, ndarray 2d, con dimensiones menores
#centro es el "centro" u "origen" del elem. estruct. Tipo tupla (x, y). Dejado en None, se toma el píxel central del mismo.
def erosionTotal(img, elemStr, centro  = None):
    cantMovs = {"x": len(img[0]) - len(elemStr[0]) + 1, "y": len(img) - len(elemStr) + 1}

    if centro == None:
        centro = {"x": (len(elemStr[0]) - 1) // 2, "y": (len(elemStr) - 1) // 2}

    imgNew = img.copy()

    for j in range(cantMovs["y"]):
        for i in range(cantMovs["x"]):
            res = erosionPaso(img, elemStr, (i, j))

            imgNew[centro["y"] + j][centro["x"] + i] = res

    return imgNew


#Funcion para realizar una erosión en un sólo punto en la imagen
#Retorna 1 o 0 si se dió erosionado o no, respectivamente
#img es una imágen de tipo ndarray 2d
#elemStr es el elemento estructural a utilizar en la operación, ndarray 2d, con dimensiones menores
#relPosElemStr es una tupla que indica
def erosionPaso(img, elemStr, relPosElemStr):
    posX = relPosElemStr[0]
    posY = relPosElemStr[1]

    pertenencia = True

    for row in range(len(elemStr)):
        for col in range(len(elemStr[0])):
            pixStr = elemStr[row][col]
            pixImg = img[row + posY][col + posX]

            if pixStr == 1:
                pertenencia = pertenencia and (pixStr and pixImg)

            if not pertenencia:
                return 0

    return 1


#Creacion de imagen erosionada
imgNew = erosionTotal(img, elemStr)


#print(img)

#plt.clear()

plt.imshow(imgNew,cmap='gray',vmin=0,vmax=1)
plt.title('Binaria')

plt.show()
