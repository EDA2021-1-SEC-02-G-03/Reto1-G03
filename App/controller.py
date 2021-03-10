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
 """

import config as cf
import model
import csv
from DISClib.ADT import list as lt 

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
#Aqui el option lo que va a hacer es permitirnos escoger entre
#las opcoines de ARRY_LIST y LINKED_LIST
def initCatalog():
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    #Loading
    loadVideos(catalog)
    loadCategories(catalog)
    loadCountriesVideos(catalog)
    loadVideosbyCategory(catalog)
    # sort_videos(catalog)
    # sort_categories(catalog)
    # sort_countries(catalog)
    sort_videos_by_category(catalog)
    loadCategoryTrendingVideo(catalog)
    loadCountriesLikes(catalog)
    #Sorting
    sort_videos(catalog)
    sort_categories(catalog)
    sort_countries(catalog)
    sort_id_videos(catalog)
    sort_countriesR2D2(catalog)
    sort_videos_likes(catalog)
    sort_countries3PO(catalog)
    sort_id_videos_RT(catalog)
    sort_categories4TPO(catalog)
    create_map_country(catalog)
    create_map_category(catalog)
    

def loadVideos(catalog):
    videos_file = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(videos_file, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategories(catalog):
    videos_file = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(videos_file, encoding='utf-8'), delimiter='\t')
    for category in input_file:
        #ix_category = {category['name']:category['id']}
        model.addCategories(catalog, category)
        #print(category)

def loadCountriesVideos(catalog):
    return model.addCountryVideo(catalog)

def loadVideosbyCategory(catalog):
    centinela=True
    for i in range(lt.size(catalog['videos'])):
        element=lt.getElement(catalog['videos'],i)
        model.add_videosbycategory(catalog,element)
    #model.addCountryVideo(catalog)

def loadCategoryTrendingVideo(catalog):
    model.addTrendingCategoryVideo(catalog)

def loadCountriesLikes(catalog):
    model.addLikedVideo(catalog)

def create_map_country(catalog):
    model.create_map_countries(catalog)

def create_map_category(catalog):
    model.create_map_categories(catalog)

def sort_videos(catalog):
    return model.sort_videos(catalog)

def sort_countries(catalog):
    return model.sort_countries(catalog)

def sort_categories(catalog):
    return model.sort_categories(catalog)

def sort_videos_by_category(catalog):
    return model.sort_videos_by_category(catalog)

def find_position_category(catalog, category):
    return model.find_position_category(catalog, category)

def most_trending_by_category(catalog,category_name:str):
    if category_name=='Film & Animation':
        category_name=='  Film & Animation'
    else:
        category_name=' '+category_name

    categoryid=''
    centinela=True
    i=1
    while centinela:
        element=lt.getElement(catalog['categories'],i)
        if element['name']==category_name:
            categoryid=element['id']
            centinela=False
        i+=1
    resultado=model.VideosTrendingDaysCategory(catalog,categoryid)
    resultado.append(categoryid)
    return resultado



def sort_id_videos(catalog):
    return model.sort_id_videos(catalog)
    #pass
def sort_id_videos_RT(catalog):
    return model.sort_id_videosV2(catalog)
    #pass
def sort_countriesR2D2(catalog):
    return model.sort_countries_R2D2(catalog)
    #return model.sort_countries(catalog)[1]
    #pass
def sort_countries3PO(catalog):
    return model.sort_countries_R4(catalog)
    #pass
def sort_categories(catalog):
    return model.sort_categories(catalog)

def sort_categories4TPO(catalog):
    return model.sort_categoriesV2(catalog)
    #pass
def sort_videos_likes(catalog):
    return model.sort_liked_videos(catalog)

def find_position_category(catalog, category):
    return model.find_position_category(catalog, category)
# Funciones de consulta sobre el catálogo
