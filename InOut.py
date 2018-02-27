# Lector de ficheros de descripcion de problema
# DoYouKnowDaWae?
# 27 Febrero 2018

import numpy as np


class Configuracion:
    n_videos = 0
    n_epoints = 0
    n_reqs = 0
    n_caches = 0
    videos = []  # i = id video, videos(i) = tamaño
    datacenters = []  # i = id endpoint, datacenters(i) = latencia
    caches_endpoints = []
    videos_endpoints = []

    def __init__(self, fichero):
        with open(fichero) as f:
            # Leer cabecera (videos, endpoints, RDs, caches, tamaño caches)
            self.n_videos, self.n_epoints, self.n_reqs, self.n_caches = [int(x) for x in f.readline().split(' ')]
            self.videos = [int(x) for x in f.readline().split(' ')]
            self.caches_endpoints = np.zeros(self.n_epoints, self.n_caches)
            self.videos_endpoints = np.zeros(self.n_epoints, self.n_videos)

            id_ep = 0
            linea = f.readline().split(' ')
            while len(linea) == 2:
                self.__read_block_ep(f, linea, id_ep)
                linea = f.readline().split(' ')
                id_ep += 1
            while len(linea) == 3:
                id_vid, id_ep, lat_vid = [int(x) for x in linea]
                self.videos_endpoints[id_vid, id_ep] = lat_vid
                linea = f.readline().split(' ')
        f.close()

    def __read_block_ep(self, f, linea, id_ep):
        lat_ep, num_lineas = [int(x) for x in linea]
        self.datacenters.append(lat_ep)
        for i in range(0, num_lineas):
            id_cache, lat_cache = [int(x) for x in f.readline().split(' ')]
            self.caches_endpoints[id_cache, id_ep] = lat_cache

