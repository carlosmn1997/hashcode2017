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
    matrixLatency = np.zeros((numEndpoints, (numCaches+1)))
    salir = False
    while (salir == False):

        linea = lineas[contadorLineas]
        partida = linea.split()
        latencyDatacenter = map(int, partida)
        if (len(latencyDatacenter) != 2):
            salir = True
        else:
            contadorLineas = contadorLineas + 1
            matrixLatency[x][y] = latencyDatacenter[0]
            for i in range(1, latencyDatacenter[1]+1):
                linea = map(int, lineas[contadorLineas].split())
                contadorLineas = contadorLineas + 1
                matrixLatency[x][linea[0]+1] = linea[1]
            x = x + 1

    matrixRequests = np.zeros((numEndpoints, numVideos))
    for i in range(contadorLineas, len(lineas)):
        linea = map(int, lineas[contadorLineas].split())
        contadorLineas = contadorLineas + 1
        # matrixRequests[endPoint][video]
        matrixRequests[linea[1]][linea[0]] = linea[2]

    config = Configuracion()
    config.setParametrosIniciales(numVideos, numEndpoints, numRequests, numCaches, sizeCache, sizeVideos, matrixLatency, matrixRequests)
    return config

lectura_problema('me_at_the_zoo.in')
