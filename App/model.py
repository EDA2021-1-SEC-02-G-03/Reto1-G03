"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ses
from DISClib.Algorithms.Sorting import mergesort as mgs
from DISClib.Algorithms.Sorting import quicksort as qus
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog():
    catalog = {'videos':None,
               'categories':None}
    catalog['videos'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['categories'] = lt.newList(datastructure='ARRAY_LIST')
    return catalog

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)

"""def newCategory(name, id):
    
    cats = cat.split()
    category = {'id':'', 'name':''}
    category['id'] = cats[0]
    category['category'] = cats[1]
    return category

    category = {'id': '', 'name': ''}
    category['name'] = name
    category['cat_id'] = id
    return category
"""
def addCategories(catalog, category):
    #c = newCategory(category['id'], category['name'])
    lt.addLast(catalog['categories'], category)
# Funciones para creacion de datos

# Funciones de consulta
def find_position_category(category_list, id, category_s, category):
    #for element in range(lt.size(category_list)):
        #if category
    pass

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByViews(video1, video2):
    #Esta función devuelve True si "views" video1 < video2
    return (int(video1['views']) > int(video2['views']))

    #def comparSections()
# Funciones de ordenamiento    
def sort_videos(catalog):
    #start_time = time.process_time()
    sorted_list = mgs.sort(catalog['videos'], cmpVideosByViews)
    #stop_time = time.process_time()
    #elapsed_time_mseg = (stop_time - start_time)*1000
    return sorted_list