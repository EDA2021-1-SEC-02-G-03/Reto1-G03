
import config as cf
import controller
from DISClib.ADT import list as lt
assert cf

def prueba(tamano_lista:int,tipo_lista:int,tipo_ordenamiento:int)->float:
    tipo_lista=str(tipo_lista)
    catalog = controller.initCatalog(tipo_lista)
    controller.loadData(catalog)
    tamano_datos_cargados = lt.size(catalog['videos'])+1
    result = controller.sort_videos(catalog, tipo_ordenamiento, tamano_lista)
    return float(result[0])

def ejecutar_prueba()->None:
    nombre_csv=input("Teclee el nombre del csv donde quiere guardar los datos: ")
    tamano_maximo=int(input('Teclee el tamaño máximo de datos a analizar: '))
    archivo=open(nombre_csv,'w')
    archivo.write('Tamaño,QuickSort-Array,MergeSort-Array,QuickSort-Linked,MergeSort-Linked\n')
    size=1000
    cadena=str(size)+','
    i=0
    while size <= tamano_maximo:
        if i==0:
            #Se calcula el quickarray
            tiempo1=prueba(size,2,1)
            tiempo2=prueba(size,2,1)
            tiempo3=prueba(size,2,1)
            promedio=(tiempo1+tiempo2+tiempo3)/3
            cadena+=str(promedio)+'\n'
        """elif i==1:
            #Se calcula el mergearray
            tiempo1=prueba(size,2,2)
            tiempo2=prueba(size,2,2)
            tiempo3=prueba(size,2,2)
            promedio=(tiempo1+tiempo2+tiempo3)/3
            cadena+=str(promedio)+'\n'
        elif i==2:
            #Se calcula el quicklinked
            tiempo1=prueba(size,2,1)
            tiempo2=prueba(size,2,1)
            tiempo3=prueba(size,2,1)
            promedio=(tiempo1+tiempo2+tiempo3)/3
            cadena+=str(promedio)+','
        elif i==3:
            #Se calcula el mergelinked
            tiempo1=prueba(size,2,2)
            tiempo2=prueba(size,2,2)
            tiempo3=prueba(size,2,2)
            promedio=(tiempo1+tiempo2+tiempo3)/3
            cadena+=str(promedio)+'\n' """ 
        i+=1
        if size==tamano_maximo and i>0:
            archivo.write(cadena)
            size+=1
        elif i>0:
            archivo.write(cadena)
            size*=2
            cadena=str(size)+','
            i=0
    archivo.close()

def ejecutar_ultima():
    nombre_csv=input("Teclee el nombre del csv donde quiere guardar los datos: ")
    tamano_maximo=int(input('Teclee el tamaño máximo de datos a analizar: '))
    archivo=open(nombre_csv,'w')
    #archivo.write('Tamaño,QuickSort-Array,MergeSort-Array,QuickSort-Linked,MergeSort-Linked\n')
    size = 375942
    cadena=str(size)+','
    tiempo1=prueba(size,1,1)
    tiempo2=prueba(size,1,1)
    tiempo3=prueba(size,1,1)
    promedio=(tiempo1+tiempo2+tiempo3)/3
    cadena+=str(promedio)+','
    tiempo1=prueba(size,1,2)
    tiempo2=prueba(size,1,2)
    tiempo3=prueba(size,1,2)
    promedio=(tiempo1+tiempo2+tiempo3)/3
    cadena+=str(promedio)+'\n'
    archivo.write(cadena)
    archivo.close()


def iniciar()->None:
    ejecucion=True
    while ejecucion:
        print('1. Ejecutar Prueba \n2. Prueba final \n3. Salir')
        opcion=int(input('Seleccione 1 o 2 o 3: '))
        if opcion==1:
            ejecutar_prueba()
        elif opcion == 2:
            ejecutar_ultima()
        elif opcion==3:
            ejecucion=False

#Principal
iniciar()







      