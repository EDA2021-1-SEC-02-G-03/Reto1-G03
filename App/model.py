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
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas como mínimo, una para los videos, otra para las categorias de
los mismos.

Se agregan listas al catalogo para mejorar la eficiencia del programa.
"""
def newCatalog():
    catalog = {'videos':None,
               'categories':None}
    catalog['videos'] = lt.newList(datastructure='ARRAY_LIST') 
    catalog['categories'] = lt.newList(datastructure='ARRAY_LIST') 
    catalog['country_videos'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['country_location'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['category_videos'] = lt.newList(datastructure='ARRAY_LIST')
    return catalog

def indexdict(catalog):
    datos=lt.newList(datastructure='ARRAY_LIST')
    dicti={}
    print(catalog['videos'])
    '''
    for i in catalog['categories']:
        print(i)
        dicti[i]='ola'
        print(dicti)
    '''

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)

def VideosTrendingDaysCategory(catalog,category_id:str):
    lista=catalog['category_videos']
    trendingdays={}
    channels={}
    for i in range(lt.size(lista)):
        element=lt.getElement(lista,i)
        e=i
        while str(element['category_id'])==str(category_id):
            element=lt.getElement(lista,e)
            if element['title'] not in trendingdays:
                trendingdays[element['title']]=1
                channel=element['channel_title']
                title=element['title']
                channels[title]=channel
            elif element['title'] in trendingdays:
                trendingdays[element['title']]+=1
            e+=1
        if len(trendingdays)>0 or i>=lt.size(lista):
            break 
    numeromayor=0
    mayor=''
    for i in trendingdays:
        actual=trendingdays[i]
        if numeromayor==0:
            mayor=i
            numeromayor=trendingdays[i]
        elif actual>numeromayor:
            numeromayor=actual
    return [mayor,numeromayor,channels]   
            
def add_videosbycategory(catalog,video):
    lt.addLast(catalog['category_videos'],video)


def addCategories(catalog, category):
    #c = newCategory(category['id'], category['name'])
    lt.addLast(catalog['categories'], category)

def addCountryVideo(catalog):
    for country in range(lt.size(catalog['videos'])):
        element = lt.getElement(catalog['videos'], country)
        lt.addLast(catalog['country_videos'], element)

# Funciones para creacion de datos

# Funciones de consulta
def find_position_category(catalog, category):
    for runner in range(lt.size(catalog)):
        element = lt.getElement(catalog, runner)
        print(element['name'], category) 
        if element['name'].strip() == category.strip():
            return element['id']
    return False

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByViews(video1, video2):
    #Esta función devuelve True si "views" video1 < video2
    return (int(video1['views']) > int(video2['views']))

    #def comparSections()
def cmpVideosByCountry(country1, country2):
    return (country1['country'] > country2['country'])
# Funciones de ordenamiento    

def cmpVideosByCategory(category1, category2):
    return (category1['category_id'] > category2['category_id'])


def sort_countries(catalog):
    sorted_list = mgs.sort(catalog['country_videos'], cmpVideosByCountry)
    return sorted_list

def sort_categories(catalog):
    sorted_list = mgs.sort(catalog['country_videos'], cmpVideosByCategory)
    return sorted_list

def sort_videos_by_category(catalog):
    sorted_list=mgs.sort(catalog['category_videos'],cmpVideosByCategory)

def create_map_countries(catalog):
    for something in range(lt.size(catalog)):
        element = lt.getElement(catalog['country_videos'])
    pass

def sort_videos(catalog):
    #start_time = time.process_time()
    sorted_list = mgs.sort(catalog['videos'], cmpVideosByViews)
    sorted_list = mgs.sort(catalog['country_videos'], cmpVideosByViews)
    #stop_time = time.process_time()
    #elapsed_time_mseg = (stop_time - start_time)*1000
    return sorted_list

