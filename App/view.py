﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar los videos con más views que son tendencia en un país dada una categoría específica.")
    print("3- Consultar el video que más días ha sido trending dado un país específico.")
    print("4- Consultar el video que más días ha sido trending para una categoría específica.")
    print("5- Consultar cuales son los videos diferentes con más likes en un país con un tag específico.")
    print("0- Salir")


def initCatalog(option):
    return controller.initCatalog(option)

def loadData(catalog):
    controller.loadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        opciones = ['1', '2']
        print("Cargando información de los archivos ....")
        tipo_lista = input("\n" + "A continuación los tipos de representación de lista que puede escoger \n" 
        +"1- ARRAY_LIST \n" + "2- LINKED_LIST\n")
        
        if tipo_lista not in opciones:
            print("Escoja una opción valida de lista")
        else:
            catalog = initCatalog(tipo_lista)
            loadData(catalog)
            print('Videos cargados: '+str(lt.size(catalog['videos'])))
            informacion1 = lt.getElement(catalog['videos'], 0)
            print('title: ' + str(informacion1['title'])+'\n' +'Channel title: '+ str(informacion1['channel_title']+'\n') 
            +'trending date: '+ str(informacion1['trending_date'])+'\n' +'country: '+ str(informacion1['country'])+'\n' +
            'views: '+str(informacion1['views'])+'\n' +'likes:'+ str(informacion1['likes'])+'\n' +'dislikes: '+ str(informacion1['dislikes'])+'\n')
            print('Categorias cargadas: ')
            #print(tipo_lista)
            #print(type(catalog['categories']))
            #print(tipo_lista)
            #print(str(lt.getElement(catalog['categories'], 2)))
            print(catalog['categories'])
            print('id ', 'name')
            for i in catalog['categories']['elements']:
                print(i['id'], i['name'])
            #print(i)
            #print(catalog['categories'])

    elif int(inputs[0]) == 2:
    
        pass

    else:
    
        sys.exit(0)
sys.exit(0)