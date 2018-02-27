# Lector de ficheros de descripcion de problema
# DoYouKnowDaWae?
# 27 Febrero 2018

class Indice():

    def __init__(self, matriz_adyacencia):
        self.matriz = matriz_adyacencia

    def get(self, indice):
        tup = self.matriz.shape
        resultado = []
        for i in range(0,tup[0]):
            if self.matriz[i, indice] > 0:
                resultado.append(i)

        return resultado