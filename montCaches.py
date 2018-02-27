# Lector de ficheros de descripcion de problema
# DoYouKnowDaWae?
# 27 Febrero 2018

import heapq

class montCaches:

    def __init__(self, lista_caches):
        self.caches = lista_caches
        self.heap = heapq()
        for i in range(0, len(self.caches)):
            nodo_mejor = self.caches[i].get_best()
            self.heap.heappush(nodo_mejor)

    def get_best(self):
        best = self.heap.heappop()
        id_cache = best[1]
        cache = self.caches[id_cache]
        new  = cache.save_video()
        self.heap.heappush(new)

            
