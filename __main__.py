# Lector de ficheros de descripcion de problema
# DoYouKnowDaWae?
# 27 Febrero 2018

from InOut import lectura_problema
from InOut import Configuracion
from montCaches import mont_caches
from Cache import Cache
from Indice import Indice

while True:
    nombre_fichero = input("Introduce fichero de entrada: ")

    configuracion = lectura_problema(nombre_fichero)

    tamanyo_cache = configuracion.sizeCache()
    num_caches = configuracion.num_caches()
    num_end_points = configuracion.num_endpoints()

    lista_end_points = []

    for i in range(0, num_end_points):
        end_point = Endpoint()
        lista_end_points.append(end_point)

    lista_caches = []

    indice_invertido = Indice(configuracion.get_caches_endopoints())

    for i in range(0,num_caches):
        lista_id_end_points = indice_invertido.get(i)
        lista_end_points_para_cache = []
        for j in lista_id_end_points:
            lista_end_points_para_cache.append(lista_end_points[j])
        cache = Cache(i, tamanyo_cache, lista_end_points_para_cache)
        lista_caches.append(cache)

    monticulo = mont_caches(lista_caches)

    fin = 1
    while fin != None :
        fin = monticulo.get_best()

    solucion = []
    for i in range(0,num_caches):
        soluciones_locales = lista_caches[i].get_solucion()
        solucion.apend(soluciones_locales)




    almacenar_solucion(solucion)