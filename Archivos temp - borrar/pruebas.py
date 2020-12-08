import numpy as np

def generateElemStr(tamano, tipo):
    #https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros

    l, h = tamano["x"], tamano["y"]
    elemStr = np.zeros((h, l))

    #https://www.mathworks.com/help/images/ref/strel.html
    #https://www.guru99.com/python-lambda-function.html#:~:text=Just%20like%20a%20normal%20function,def%20to%20define%20normal%20functions).
    formas = {"diamante":       lambda x, y: (y + 1 / 2) >= -h / l * (x + 1 / 2) + h / 2,
              "disco":          lambda x, y: (y + 1 / 2) >= h / 2 * (1 - 2 / l * ((x + 1 / 2) * l - (x + 1 / 2) ** 2) ** (1 / 2)),
              "rectangulo":     lambda x, y: (y + 1 / 2) >= -1}


    for j in range(h):
        for i in range(l):
            if j < (h + 1) // 2:
                if i < (l + 1) // 2:
                    elemStr[j][i] = formas[tipo](i, j) * 1

                else:
                    elemStr[j][i] = elemStr[j][l - i - 1]

            else:
                elemStr[j][i] = elemStr[h - j - 1][l - i - 1]

    print(elemStr)
    return elemStr


a = generateElemStr({"x": 8, "y": 8}, "diamante")





