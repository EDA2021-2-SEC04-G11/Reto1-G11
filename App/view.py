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
    print("4- Hacer sort")
    print("5- Listar cronologicamente los artistas")
    print("6- Listar cronologicamente las adquisiciones")
    print("7- clasificar las obras de un artista por técnica")
    print("8- clasificar las obras por la nacionalidad de sus creadores")
    print("9- transportar obras de un departamento")
    print("10- Reglas de transporte")

def initCatalog(d_structure):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(d_structure)

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

def sorting(entrada,catalog):
    lista_organizada = None
    if int(entrada[0]) == 1:
        sortret = controller.insert(catalog['artworks'])
        time = sortret[1]
        lista_organizada = sortret[0]
        print(f'Se organizaron los archivos correctamente en {time}ms')
    elif int(entrada[0]) == 2:
        sortret = controller.merge(catalog['artworks'])
        time = sortret[1]
        lista_organizada = sortret[0]
        print(f'Se organizaron los archivos correctamente en {time}ms')
    elif int(entrada[0]) == 3:
        sortret = controller.quick(catalog['artworks'])
        time = sortret[1]
        lista_organizada = sortret[0]
        print(f'Se organizaron los archivos correctamente en {time}ms')
    elif int(entrada[0]) == 4:
        sortret = controller.shell(catalog['artworks'])
        time = sortret[1]
        lista_organizada = sortret[0]
        print(f'Se organizaron los archivos correctamente en {time}ms')
    return lista_organizada

def sublist(input: str):
    digits = '0123456789'
    prev_was_number = None
    value = ''
    type = 'n'
    for n in input:
        print(value)
        if prev_was_number == None or prev_was_number and n in digits:
            prev_was_number = True
            value+=n
        if n == '%':
            type = 'p'
            break
    if value != '':
        value = int(value)
    print(f'Se cargaran {value} datos', type)

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
        catalog = initCatalog(d_structure)
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Artworks cargados: ' + str(lt.size(catalog['artworks'])))
        print('Ultimos 3 elementos del archivo de artistas:')
        printLastArtists(catalog)
        print('Ultimos 3 elementos del archivo de artworks:')
        printLastArtworks(catalog)

    elif int(inputs[0]) == 3:
        input3 = input("Ingrese el porcentaje('xx%' con el signo) o numero ('xxxx')\n")
        if catalog != None:
            del catalog
            catalog = None
            print('catalog ded')
        catalog = sublist(input3)

    elif int(inputs[0]) == 4:
        entrada = input("""Seleccione el algoritmo de ordenamiento
             1 - Insertionsort
             2 - Mergesort
             3 - Quicksort
             4 - Shellsort\n""")
        if catalog == None:
            print('Oops, primero carga la informacion.')
            continue
        else:
            print('Copiando y eliminando catalogo antiguo...')
            temp = catalog.copy()
            del catalog
            print('Creando nuevo catalogo personalizado...')
            catalog = sorting(entrada,temp)
            del temp
            print('¡Nuevo catalogo personalizado creado correctamente!')
        
    else:
        sys.exit(0)
sys.exit(0)