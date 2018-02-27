# Lector de ficheros de descripcion de problema
# DoYouKnowDaWae?
# 27 Febrero 2018

import numpy as np

class Configuracion(object):
    def setParametrosIniciales(self, numVideos, numEndpoints, numRequests, numCaches, sizeCache, sizeVideos, matrixLatency, matrixRequests):
        self.numVideos = numVideos
        self.numEndpoints = numEndpoints
        self.numRequests = numRequests
        self.numCaches = numCaches
        self.sizeCache = sizeCache
        self.sizeVideos = sizeVideos
        self.matrixLatency = matrixLatency
        self.matrixRequests = matrixRequests



def lectura_problema(nombreFichero):
    fichero_objeto = open(nombreFichero, "r")
    lineas = fichero_objeto.readlines()
    numVideos, numEndpoints, numRequests, numCaches, sizeCache = [int(i) for i in lineas[0].split(' ')]
    sizeVideos = lineas[1].split()

    contadorLineas = 2
    x, y = 0, 0 # x son los numEndpoints, y son los caches
    matrixLatency = np.zeros((numEndpoints, (numCaches+1)), dtype=np.uint8)
    salir = False
    while (salir == False):
        linea = lineas[contadorLineas]
        if (len(linea.split()) != 2):
            salir = True
        else:
            matrixLatency[x][y] = 

#     config.setParametrosIniciales(filas, columnas, min, max)
#     for i in range(0,config.getDimensionx()):
#         for j in range(0,config.getDimensiony()):
#             config.setAtributo(i, j, lineas[i+1][j])
# return config
    print numVideos, numEndpoints, numRequests, numCaches, sizeCache, sizeVideos
lectura_problema('me_at_the_zoo.in')
