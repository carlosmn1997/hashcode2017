# Lector de ficheros de descripcion de problema
# DoYouKnowDaWae?
# 27 Febrero 2018

import heapq

class montCaches:

    def __init__(self, lista_caches):
        self.caches = lista_caches
        self.heap = heapq()
        for i in range(0, len(self.caches)):
            id = self.caches[i].id()
            prioridad = self.caches[i]
            self.heap.heappush([prioridad, id])

    def get_best(self):
        best = self.heap.heappop()
        id_cache = best[1]
        cache = self.caches[id_cache]
        cache.save_video()

            
