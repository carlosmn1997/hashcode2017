
class Endpoint(object):

    def __init_(self,id):
        self.id = id
        self.DCLat = 0
        self.cachesConectadas = []    #Latencia de cada cache conectada
        self.sizeVideos = []
        self.requests = []

    def setCachesConectadas(self, matrixLatency, DCLatency):
        self.cachesConectadas = matrixLatency[self.id]
        self.DCLat = DCLatency[self.id]

    def setVideos(self, matrixRequests, sizeVideos):
        self.sizeVideos = sizeVideos
        self.requests = matrixRequests[self.id]


    """
        Devuelve una lista con los costes de todos los videos del endpoint para la cache idCache --> [[beneficio, id_video, tam_video]]
    """
    def getVideos(self, idCache):

        for i in range(0, len(self.sizeVideos)):
            numReq = self.requests[self.id]
            resul = []      # devuelve [beneficio, id, tam]
            if (numReq>0):   #hay peticiones del video
                gastoNormal = numReq*self.DCLat
                gastoMejor = numReq*self.cachesConectadas[idCache]
                resul.append([gastoNormal-gastoMejor, i, self.sizeVideos[i]])
        return resul







