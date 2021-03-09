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
Programa Principal
"""
while True:
    printMenu()
    opcion = int(input('Seleccione una opción para continuar\n'))
    if opcion==1:
        ejecutar_opcion1()
    elif opcion==2:
        ejecutar_opcion2()
    elif opcion==3:
        ejecutar_opcion3()
    elif opcion==4:
        ejecutar_opcion4()
    elif opcion==5:
        ejecutar_opcion5()
    elif opcion==0:
        sys.exit(0)



sys.exit(0)
