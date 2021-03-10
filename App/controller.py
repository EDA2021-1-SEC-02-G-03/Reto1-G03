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
    loadVideos(catalog)
    loadCategories(catalog)
    loadCountriesVideos(catalog)
    sort_videos(catalog)
    sort_categories(catalog)
    sort_countries(catalog)
    

def loadVideos(catalog):
    videos_file = cf.data_dir + 'videos/videos-small.csv'
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

def sort_videos(catalog):
    return model.sort_videos(catalog)

def sort_countries(catalog):
    return model.sort_countries(catalog)

def sort_categories(catalog):
    return model.sort_categories(catalog)

def find_position_category(catalog, category):
    return model.find_position_category(catalog, category)
# Funciones de consulta sobre el catálogo
