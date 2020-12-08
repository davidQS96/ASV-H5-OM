import numpy as np


#Funcion que genera el elemento estructural, hay 3 formas
#Devuelve el ndarray correspondiente al mismo
#tamano es un diccionario {"x":x, "y":y}
#tipo puede ser "diamante", "disco", "rectangulo"
def generateElemStr(tamano, tipo):
    #https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros

    l, h = tamano["x"], tamano["y"]
    elemStr = np.zeros((h, l))

    #https://www.mathworks.com/help/images/ref/strel.html
    #https://www.guru99.com/python-lambda-function.html#:~:text=Just%20like%20a%20normal%20function,def%20to%20define%20normal%20functions).
    #Diccionario con comparaciones para rellenar array
    formas = {"diamante":       lambda x, y: (y + 1 / 2) >= -h / l * (x + 1 / 2) + h / 2,
              "disco":          lambda x, y: (y + 1 / 2) >= h / 2 * (1 - 2 / l * ((x + 1 / 2) * l - (x + 1 / 2) ** 2) ** (1 / 2)),
              "rectangulo":     lambda x, y: (y + 1 / 2) >= -1}


    for j in range(h):
        for i in range(l):
            if j < (h + 1) // 2:
                if i < (l + 1) // 2:
                    #Primer cuadrante
                    elemStr[j][i] = formas[tipo](i, j) * 1

                else:
                    #Espejo del primer cuadrante
                    elemStr[j][i] = elemStr[j][l - i - 1]

            else:
                #Espejo de la seccion superior
                elemStr[j][i] = elemStr[h - j - 1][l - i - 1]

    return elemStr


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

    #Movimiento del elem estruct. por la imagen
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

    #Variable indica si el elemento estruct. se encuentra incluido en la imagen, en la posicion actual
    pertenencia = True

    #Revision de pertenencia por cada pixel del elem. str., pertenencia es falso si al menos un pixel no pertenece
    for row in range(len(elemStr)):
        for col in range(len(elemStr[0])):
            pixStr = elemStr[row][col]
            pixImg = img[row + posY][col + posX]

            if pixStr == 1:
                pertenencia = pertenencia and (pixStr and pixImg)

            if not pertenencia:
                return 0

    return 1


#Funcion para realizar una dilatacion completa de una imágen
#Retorna una copia de la imagen original, modificada con la op. de dilatacion
#img es una imágen de tipo ndarray 2d
#elemStr es el elemento estructural a utilizar en la operación, ndarray 2d, con dimensiones menores
#centro es el "centro" u "origen" del elem. estruct. Tipo tupla (x, y). Dejado en None, se toma el píxel central del mismo.
def dilatacionTotal(img, elemStr, centro  = None):
    cantMovs = {"x": len(img[0]) - len(elemStr[0]) + 1, "y": len(img) - len(elemStr) + 1}

    if centro == None:
        centro = {"x": (len(elemStr[0]) - 1) // 2, "y": (len(elemStr) - 1) // 2}

    imgNew = img.copy()

    #Movimiento del elem estruct. por la imagen
    for j in range(cantMovs["y"]):
        for i in range(cantMovs["x"]):
            res = dilatacionPaso(img, elemStr, (i, j))
            imgNew[centro["y"] + j][centro["x"] + i] = res

    return imgNew


#Funcion para realizar una dilatacion en un sólo punto en la imagen
#Retorna 1 o 0 si se dió dilatacion o no, respectivamente
#img es una imágen de tipo ndarray 2d
#elemStr es el elemento estructural a utilizar en la operación, ndarray 2d, con dimensiones menores
#relPosElemStr es una tupla que indica
def dilatacionPaso(img, elemStr, relPosElemStr):
    posX = relPosElemStr[0]
    posY = relPosElemStr[1]

    #Variable indica si el elemento estruct. se encuentra incluido en la imagen, en la posicion actual
    cruce = False

    #Revision de pertenencia por cada pixel del elem. str., pertenencia es falso si al menos un pixel no pertenece
    for row in range(len(elemStr)):
        for col in range(len(elemStr[0])):
            pixStr = elemStr[row][col]
            pixImg = img[row + posY][col + posX]

            if pixStr == 1:
                cruce = cruce or (pixStr and pixImg)

            if cruce:
                return 1

    return 0
