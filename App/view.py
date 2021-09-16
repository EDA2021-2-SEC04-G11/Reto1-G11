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
    print("1- Tipo de representacion")
    print("2- Cargar 100% de la información en el catálogo")
    print("3- Cargar sublista con tamaño personalizado") 
    print("4- Listar cronologicamente los artistas")
    print("5- Listar cronologicamente las adquisiciones")
    print("6- clasificar las obras de un artista por técnica")
    print("7- clasificar las obras por la nacionalidad de sus creadores")
    print("8- transportar obras de un departamento")
    print("9- Reglas de transporte")


def initCatalog(d_structure,pos,numelem_artworks,numelem_artists, prev_catalog):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(d_structure,pos,numelem_artworks,numelem_artists, prev_catalog)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


def printLastArtists(catalog):
    """
    Imprime los 3 ultimos elementos de artists en el catalogo
    """
    size = lt.size(catalog['artists'])
    parent = lt.getElement(catalog['artists'],size)
    firstChild = lt.getElement(catalog['artists'],size-1)
    secondChild = lt.getElement(catalog['artists'],size-2)
    print(parent,'\n')
    print(firstChild,'\n')
    print(secondChild,'\n')


def printLastArtworks(catalog):
    """
    Imprime los 3 ultimos elementos de artworks en el catalogo
    """
    size = lt.size(catalog['artworks'])
    parent = lt.getElement(catalog['artworks'],size)
    firstChild = lt.getElement(catalog['artworks'],size-1)
    secondChild = lt.getElement(catalog['artworks'],size-2)
    print(parent,'\n')
    print(firstChild,'\n')
    print(secondChild,'\n')


catalog = None
d_structure = "LINKED_LIST"

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print('Escribir al para ARRAY_LIST o ll para LINKED_LIST')
        input_1 = input()
        if input_1[:2] == 'al':
            d_structure = "ARRAY_LIST"
        elif input_1[:2] == 'll':
            d_structure = "LINKED_LIST"
        else:
            print('Proporcione un dato correcto.')

    elif int(inputs[0]) == 2:
        pos = 0
        numelem_artworks = None
        numelem_artists = None
        prev_catalog = None
        print("Cargando información de los archivos ....")
        catalog = initCatalog(d_structure,pos,numelem_artworks,numelem_artists, prev_catalog)
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Artworks cargados: ' + str(lt.size(catalog['artworks'])))
        print('Ultimos 3 elementos del archivo de artistas:')
        printLastArtists(catalog)
        print('Ultimos 3 elementos del archivo de artworks:')
        printLastArtworks(catalog)

    elif int(inputs[0]) == 3:
        size_subl = None
        condition_subl = True
        count = 0
        while condition_subl:
            input_subl = input(('Ingrese el tamaño de la muestra a cargar en porcentaje (1 - 100):\n')).strip()
            for i in input_subl:
                if i != ' ' and count == 0 and int(i) in range(10):
                    count += 1
                    size_subl = f'{i}'
                elif i != ' ' and count == 1 and int(i) in range(10):
                    if size_subl[0] != '1':
                        count += 1
                        size_subl += f'{i}'
                        size_subl = int(size_subl)
                        condition_subl = False
                        break
                    else:
                        count += 1
                        size_subl += f'{i}'  
                elif i != ' ' and count == 2 and int(i) in range(10) :
                    count += 1
                    size_subl += f'{i}'
                    size_subl = int(size_subl)
                    condition_subl = False
                    break
            if input_subl == None:
                print('Ingrese un porcentaje valido.')

        if size_subl != None and catalog != None:
            prev_catalog = catalog
            print(f"Cargando {size_subl}% de información de los archivos ....")
            catalog = initCatalog(d_structure,0,lt.size(catalog['artworks'])*(size_subl/100),lt.size(catalog['artists'])*(size_subl/100), prev_catalog)
            loadData(catalog)
            print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
            print('Artworks cargados: ' + str(lt.size(catalog['artworks'])))
            print('Ultimos 3 elementos del archivo de artistas:')
            printLastArtists(catalog)
            print('Ultimos 3 elementos del archivo de artworks:')
            printLastArtworks(catalog)
        elif catalog == None:
            print('Primero debes de cargar los archivos para crear una sublista')
    else:
        sys.exit(0)
sys.exit(0)