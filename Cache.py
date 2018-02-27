from heapq import *


class Cache:
    # VIDEO ENTRADA = BENEFICIO, ID, TAMAÑO
    # VIDEO SALIDA = BENEFICIO, ID
    id = 0
    tamdisp = 0
    mont = []
    saved = []
    min_tam_video = 100000

    def __init__(self, _id, _tam, _endpoints):
        self.id = _id
        self.tamdisp = _tam
        for ep in _endpoints:
            # Para cada endpoint
            for video in ep.getVideos(self.id):
                # Para cada video de cada endpoint
                heappush(self.mont, video)
                # Actualizar el valor del video mínimo
                if video[2] < self.min_tam_video:
                    self.min_tam_video = video[2]

    def get_best(self):
        try:
            return self.mont[0][:1]
        except IndexError:
            return None

    def save_video(self):
        video = None
        # Intenta obtener el mejor video
        try:
            video = heappop(self.mont)
        except IndexError:
            return video[:1]
        # Añade el video a la lista de guardados si lo ha encontrado
        self.saved.append(video)
        if self.min_tam_video > self.tamdisp:
            # Ya no caben videos, vacia el monticulo y devuelve siempre None
            self.mont = []
            return None
        else:
            # Mientras el vídeo no quepa, va buscando vídeo más pequeño eliminando los que no caben
            while (self.tamdisp - self.mont[0][2]) <= 0:
                heappop(self.mont)

