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


def initCatalog():
    return controller.initCatalog()

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
        print("Cargando información de los archivos ....")
        #Cargamos los datos
        catalog = initCatalog()
        loadData(catalog)
        #catalog_by_countries = controller.sort_countries(catalog)
        #Se hace print de la información de videos cargados
        print('Videos cargados: '+str(lt.size(catalog['videos'])))
        informacion1 = lt.getElement(catalog['videos'], 1)
        print('title: ' + str(informacion1['title'])+'\n' +'Channel title: '+ str(informacion1['channel_title']+'\n') 
        +'trending date: '+ str(informacion1['trending_date'])+'\n' +'country: '+ str(informacion1['country'])+'\n' +
        'views: '+str(informacion1['views'])+'\n' +'likes:'+ str(informacion1['likes'])+'\n' +'dislikes: '+ str(informacion1['dislikes'])+'\n')
        print('Categorias cargadas: ')

        print('id ', 'name')
        #print(catalog['categories'])
        for i in range(lt.size(catalog['categories'])):
            element = lt.getElement(catalog['categories'], i)
            print(element['id'], element['name'])
            #print(element)
        print(catalog['category_map'])
        # for i in range(1, 1000):
        #     element = lt.getElement(catalog['category_trending_video'], i)
        #     print(element['category_id'],element['video_id'], element['title'], element['country'])

    elif int(inputs[0]) == 2:

        tamano_datos_cargados = lt.size(catalog['videos'])+1
        category_name = input('Ingrese una categoria: ')
        id_number = controller.find_position_category(catalog['categories'], category_name)
        country = input('Ingrese un país: ')
        tamano_lista = int(input('Ingrese el número de videos que quiere listar: '))
        if tamano_lista > tamano_datos_cargados:
            print("El número que ingresó excede la cantidad de videos cargados")
        
        country_map = lt.getElement(catalog['country_map'], 1)

        counter_data = 0
        # for i in range(1, 1000):
        #     element = lt.getElement(catalog['country_videos'], i)
        #     print(element['video_id'], element['country'], element['category_id'], element['views'])
        for element in range(country_map[country][0]+1, country_map[country][1]):
            data = lt.getElement(catalog['country_videos'], element)
            if data['category_id'] == id_number:
                counter_data += 1
                if counter_data > tamano_lista:
                    break
                print(data['title'], data['trending_date'], data['channel_title'],
                data['publish_time'], data['views'], data['likes'], data['dislikes'])

    elif int(inputs[0]) == 3:
        country = input('Ingrese un país: ')
        country_map = lt.getElement(catalog['country_map'], 1)
        bigger_moment = 0
        actual_video = ''
        actual_winner = 0
        #video_winner = ''
        for element in range(country_map[country][0]+1, country_map[country][1]):
            data = lt.getElement(catalog['videos'], element)
            if data['video_id'] != actual_video:
                actual_video = data['video_id']
                bigger_moment = 0
            bigger_moment += 1
            if bigger_moment >= actual_winner:
                actual_winner = bigger_moment
                video_winner = element
        winner = lt.getElement(catalog['videos'], video_winner)
        print(winner['title'], winner['channel_title'], winner['country'], actual_winner)
            #print(data['country'], data['video_id'], data['views'])
    elif int(inputs[0]) == 4:
        category_name = input('Ingrese una categoria: ')
        id_number = str(controller.find_position_category(catalog['categories'], category_name))
        category_map = lt.getElement(catalog['category_map'], 1)
        bigger_moment = 0
        actual_video = ''
        actual_winner = 0
        comprobador_sad = 0
        #video_winner = ''
        for element in range(category_map[id_number][0]+1, category_map[id_number][1]):
            data = lt.getElement(catalog['category_trending_video'], element)
            if data['channel_title'] == 'Жаны':
                comprobador_sad += 1
            if data['video_id'] != actual_video:
                actual_video = data['video_id']
                bigger_moment = 0
            bigger_moment += 1
            if bigger_moment > actual_winner:
                actual_winner = bigger_moment
                video_winner = element
        winner = lt.getElement(catalog['category_trending_video'], winner['video_id'],video_winner)
        print(winner['title'], winner['channel_title'], actual_winner)
        print(comprobador_sad)
        #print(catalog[])
    elif int(inputs[0]) == 5:
        country = input('Ingrese un país: ')
        tamano_lista = int(input('Ingrese el número de videos que quiere listar: '))
        tag = input('Ingrese el tag del video: ')
        country_map = lt.getElement(catalog['country_map'], 1)
        counter_data = 0
        for element in range(country_map[country][0]+1, country_map[country][1]):
            data = lt.getElement(catalog['liked_videos'], element)
            if tag in data['tags']:
                counter_data +=1
                if counter_data > tamano_lista:
                    break
                print(data['title'], data['channel_title'], data['views'], 
                data['likes'])
        # for i in range(1, 1000):
        #     data = lt.getElement(catalog['liked_videos'], i)
        #     print(data['country'], data['likes'])
    else:
        sys.exit(0)
sys.exit(0)
