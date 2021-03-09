"""
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
    #controller.sort_videos(catalog)

def ejecutar_opcion1():

    pass

def ejecutar_opcion2():

    pass

def ejecutar_opcion3():
    #Requerimiento 2 del laboratorio (estudiante A, individual)
    pass

def ejecutar_opcion4():
    #Requerimiento 3 del laboratorio (estudiante B, individual)
    pass

def ejecutar_opcion5():

    pass

def ejecutar_opcion0():

    pass

catalog = None #Ni idea por qué esto

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
            #sort_videos(catalog, 3)
            print('Videos cargados: '+str(lt.size(catalog['videos'])))
            informacion1 = lt.getElement(catalog['videos'], 1)
            print('title: ' + str(informacion1['title'])+'\n' +'Channel title: '+ str(informacion1['channel_title']+'\n') 
            +'trending date: '+ str(informacion1['trending_date'])+'\n' +'country: '+ str(informacion1['country'])+'\n' +
            'views: '+str(informacion1['views'])+'\n' +'likes:'+ str(informacion1['likes'])+'\n' +'dislikes: '+ str(informacion1['dislikes'])+'\n')
            #print(lt.getElement(catalog['videos'], 0))
            print('Categorias cargadas: ')
            #print(tipo_lista)
            #print(type(catalog['categories']))
            #print(tipo_lista)
            #print(str(lt.getElement(catalog['categories'], 2)))
            #print(catalog['categories'])
            #print(lt.getElement(catalog['categories'], 0))
            print('id ', 'name')
            for i in range(lt.size(catalog['categories'])):
                element = lt.getElement(catalog['categories'], i)
                print(element['id'], element['name'])
                #print(i['id'], i['name'])
            #print(i)
            #print(catalog['categories'])

    elif int(inputs[0]) == 2:
        tamano_datos_cargados = lt.size(catalog['videos'])+1
        #category_name = input('Ingrese una categoria')
        #country = input('Ingrese un país')
        tamano_lista = int(input('Ingrese el número de videos que quiere listar: '))
        if tamano_lista > tamano_datos_cargados:
            print("El número que ingresó excede la cantidad de videos cargados")
        tipo_ordenamiento = int(input('Ingrese el número del tipo de algoritmo de ordenamiento que desea\n 1- Quick Sort \n 2- Merge Sort \n'))
        result = controller.sort_videos(catalog, tipo_ordenamiento, tamano_lista)
        print("Para la muestra de ",tamano_lista,
        "elementos, el tiempo (mseg) es: ", str(result[0]))
        #videos = lt.subList(catalog['videos'], tamano_datos_cargados - tamano_lista, tamano_datos_cargados)
        #videos = lt.subList(catalog['videos'], 1, tamano_lista)
        #print('trending_date', 'title', 'channel_title', 'publish_time',
        #'views', 'likes', 'dislikes')
        """for video in range(1, tamano_lista+1): 
            element = lt.getElement(result[1], video)
            #Esto es para la parte del reto 1 completo
            #if (lt.getElement(catalog['country']) == country and 
            #lt.getElement(catalog['category_id'] == ) 
            print(element['trending_date'], element['title'],
             element['channel_title'], element['publish_time'],
          element['views'], element['likes'], element['dislikes'])
        """    
    else:
    
        sys.exit(0)
sys.exit(0)
