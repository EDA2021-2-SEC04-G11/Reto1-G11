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
    print("1- Tipo de representacion (LINKED_LIST por default)")
    print("2- Cargar 100% de la información en el catálogo")
    print("3- Cargar sublista con tamaño personalizado") 
    print("4- Hacer sort de los Artworks")
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

def printFirstArtworks(catalog):
    """
    Imprime los 3 primeros elementos de artworks en el catalogo
    """
    parent = lt.getElement(catalog['artworks'],1)
    firstChild = lt.getElement(catalog['artworks'],2)
    secondChild = lt.getElement(catalog['artworks'],3)
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

def sortingPrints(catalog):
    entrada = input("""Seleccione el algoritmo de ordenamiento
             1 - Insertionsort
             2 - Mergesort
             3 - Quicksort
             4 - Shellsort\n""")
    print('Copiando temporalmente el catalogo antiguo...')
    temp = catalog.copy()
    print('Proceso de sorting iniciado...')
    del catalog['artworks'] 
    catalog['artworks'] = sorting(entrada,temp)
    del temp
    print('¡Artworks organizados!')
    print_catalog_elements(catalog)

def sublist_input(input: str)->tuple:
    digits = '0123456789'
    prev_was_number = None
    value = ''
    for n in input:
        if n == '.' or n == ',':
            print('Ingresar numeros del 1 al 100')
            return None
        if len(value) == 3:
            break
        if prev_was_number == None or prev_was_number and n in digits:
            prev_was_number = True
            value+=n
    if value != '':
        value = int(value)
        if value > 100 or value == 0:
            print('Ingresar un porcentaje valido.')
            return None
        print(f'Se cargaran {value}% de los datos')
    return value/100 #False for complete_catalog

def create_catalog_complete(d_structure):
    print("Cargando información de los archivos ....")
    catalog = initCatalog(d_structure)
    loadData(catalog)
    print_catalog_elements(catalog)
    return catalog

def print_catalog_elements(catalog):
    print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
    print('Artworks cargados: ' + str(lt.size(catalog['artworks'])))
    print('Ultimos 3 elementos del archivo de artistas:')
    printLastArtists(catalog)
    print('Ultimos 3 elementos del archivo de artworks:')
    printLastArtworks(catalog)
    print('Primeros 3 elementos del archivo de artworks:')
    printFirstArtworks(catalog)

def sublist_creator(value: float, catalog, complete_catalog: bool,sorted: bool,d_structure):
    # SORT BEFORE DOING THIS
    max_artists = 0
    max_artworks = 0
    amount_artists = None
    amount_artworks = None
    evaluated = False
    pos = 1
    if catalog != None and complete_catalog and not sorted:
        sortingPrints(catalog)
        sorted = True
        evaluated = True
    elif catalog == None:
        catalog = create_catalog_complete(d_structure)
        complete_catalog = True
        sortingPrints(catalog)
        sorted = True
        evaluated = True
    elif catalog != None and not complete_catalog:
        del catalog
        catalog = create_catalog_complete(d_structure)
        complete_catalog = True
        sortingPrints(catalog)
        sorted = True
        evaluated = True
    if evaluated:
        max_artists = lt.size(catalog['artists'])
        max_artworks = lt.size(catalog['artworks'])
        amount_artists = int(max_artists*value)
        amount_artworks = int(max_artworks*value)
        print(amount_artists,amount_artworks)
        temp = catalog.copy()
        del catalog['artists']
        del catalog['artworks']
        catalog['artists'] = lt.subList(temp['artists'],pos,amount_artists)
        catalog['artworks'] = lt.subList(temp['artworks'],pos,amount_artworks)
        del temp
    return catalog
    
def listar_cronologicamente_artists(catalog,yeari: int,yearf: int): #REQUERIMIENTO 1
    pass

def listar_cronologicamente_artistsPrint():
    yi = None
    yf = None
    IN = input("Ingrese el año inicial y el año final:\nex. '2014 2021'\n")
    digits = '0123456789'
    prev_was_number = None
    value = ''
    value_count = 0
    while True:
        for i in IN:
            if i in digits:
                if prev_was_number == None or prev_was_number and i in digits and len(value) < 4:
                    value+=i
                    prev_was_number = True
                elif i not in digits:
                    prev_was_number = False
                    value = ''
                if len(value) == 4:
                    if value_count == 0:
                        yi = value
                        value = ''
                        value_count+=1
                    elif value_count == 1:
                        yf = value
                        value = ''
                        value_count+=1  
        #check values
        if value_count == 2:
            if len(str(yi)) < 4 or len(str(yf)) < 4:
                print('Introduce años validos pls :D')
            elif yf < yi:
                print('Por favor ingresar el año menor como inicial y el mayor como final.')
            else:
                break
    print(f'Se usaran los años {yi} como inicial y {yf} como final.')
    return yi,yf

sorted = False
sublist_input_runs = 0
catalog = None
d_structure = "LINKED_LIST"
complete_catalog = False

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
        catalog = create_catalog_complete(d_structure)
        complete_catalog = True
        sorted = False

    elif int(inputs[0]) == 3:
        value = None
        while value == None:
            input3 = input("Ingrese el porcentaje('xx%')\n")
            value = sublist_input(input3)
        if catalog == None:
            print('No se encontro catalogo antiguo, asi que se creara el primer catalogo...')
        print('Creando sublista...')
        catalog = sublist_creator(value,catalog,complete_catalog,sorted,d_structure)
        complete_catalog = False
        sorted = True
        print('\n\n\n\nSUBLISTAS CREADAS CORRECTAMENTE ->\n\n\n\n')
        print_catalog_elements(catalog)

    elif int(inputs[0]) == 4:
        if catalog == None:
            print('Oops, primero carga la informacion.')
            continue
        elif sorted:
            print('Ya ordenaste este catalogo.')
        else:
            sortingPrints(catalog)
            sorted = True
    elif int(inputs[0]) == 5: #LISTAR CRONOLOGICAMENTE LOS ARTISTAS
        yi, yf = listar_cronologicamente_artistsPrint()
    else:
        sys.exit(0)
sys.exit(0)