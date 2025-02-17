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
import datetime
import time

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
    print("10- Nueva exposicion en el museo")

######                         ######
######                         ######
######      PREVIOUS LABS      ######
######                         ######
######                         ######

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

######                 ######
######                 ######
######      LAB 4      ######
######                 ######
######                 ######

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

def sublist_creator(value: float, catalog, complete_catalog: bool,sorted: bool,d_structure):
    # SORT BEFORE DOING THIS
    evaluated = False
    pos = 1
    if catalog != None and complete_catalog and not sorted:
        sortingPrints(catalog, None)
        sorted = True
        evaluated = True
    elif catalog == None:
        catalog = create_catalog_complete(d_structure)
        complete_catalog = True
        sortingPrints(catalog, None)
        sorted = True
        evaluated = True
    elif catalog != None and not complete_catalog:
        del catalog
        catalog = create_catalog_complete(d_structure)
        complete_catalog = True
        sortingPrints(catalog, None)
        sorted = True
        evaluated = True
    if evaluated:
        catalog = controller.createSublist(catalog,pos,value)
    return catalog

def sorting(entrada,catalog, target):
    lista_organizada = None
    if int(entrada[0]) == 1:
        sortret = controller.insert(catalog['artworks'], target)
        time = sortret[1]
        lista_organizada = sortret[0]
        print(f'Se organizaron los archivos correctamente en {time}ms')
    elif int(entrada[0]) == 2:
        sortret = controller.merge(catalog['artworks'], target)
        time = sortret[1]
        lista_organizada = sortret[0]
        print(f'Se organizaron los archivos correctamente en {time}ms')
    elif int(entrada[0]) == 3:
        sortret = controller.quick(catalog['artworks'],target)
        time = sortret[1]
        lista_organizada = sortret[0]
        print(f'Se organizaron los archivos correctamente en {time}ms')
    elif int(entrada[0]) == 4:
        sortret = controller.shell(catalog['artworks'], target)
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
    catalog['artworks'] = sorting(entrada,temp, None)
    del temp
    print('¡Artworks organizados!')
    print_catalog_elements(catalog)

######                     ######
######                     ######
######   REQUISITO 1 y 2   ######
######                     ######
######                     ######

def inputsR1R2(R1,R2):
    yi = None
    yf = None
    mi = None
    mf = None
    di = None
    df = None
    digits = '0123456789'
    only_numbers = True
    datei = None
    datef = None
    req = None
    if R1:
        req = 1
    elif R2:
        req = 2
    while True:
        if R1:
            INi = input("Ingrese la Date inicial (YYYY): \n").strip()
            INf = input("Ingrese la Date final (YYYY): \n").strip()
            for i in INi:
                if i not in digits :
                    only_numbers = False
                    break
            for j in INf:
                if j not in digits:
                    only_numbers = False
                    break
            if not only_numbers:
                print('Introduce años validos pls :D')
                continue
            else:
                yi = int(INi) 
                yf = int(INf)
            if len(str(yi)) < 4 or len(str(yf)) < 4:
                print('Introduce años validos pls :D')
            elif yf < yi:
                print('Por favor ingresar el año menor como inicial y el mayor como final.')
            else:
                datef = yf
                datei = yi
                break
        elif R2:
            INiList = input("Ingrese la Date inicial (YYYY-MM-DD) : \n").strip().split('-')
            INfList = input("Ingrese la Date final (YYYY-MM-DD) : \n").strip().split('-')
            if len(INiList) == 3 and len(INfList) == 3:
                yi = INiList[0]
                mi = INiList[1]
                di = INiList[2]
                yf = INfList[0]
                mf = INfList[1]
                df = INfList[2]
                datei = f'{yi}-{mi}-{di}'
                datef = f'{yf}-{mf}-{df}'
                for i in INiList:
                    for j in i:
                        if j not in digits:
                            only_numbers = False
                for k in INfList:
                    for l in k:
                        if l not in digits:
                            only_numbers = False
                #check
                if not only_numbers:
                    print('Introduce años validos pls :D')
                    continue
                else:
                    datetimeDatei = datetime.date.fromisoformat(datei)
                    datetimeDatef = datetime.date.fromisoformat(datef)
                if datetimeDatei > datetimeDatef:
                    print('Por favor ingresar el año menor como inicial y el mayor como final.')
                    continue
                else:
                    break
            else:
                print('Introduce Dates validas pls :D')
    print(f'Se usara la Date {datei} como Date inicial y {datef} como Date final')
    return (datei,datef,req)
    
def sortR1R2(targetList,target):
    IN = input("""Seleccione el algoritmo de ordenamiento
             1 - Insertionsort
             2 - Mergesort
             3 - Quicksort
             4 - Shellsort\n""")
    targetListSorted = None
    if int(IN[0]) == 1:
        sortret = controller.insert(targetList, target)
        time = sortret[1]
        targetListSorted = sortret[0]
        print(f'Se organizaron los archivos correctamente en {time}ms\n')
    elif int(IN[0]) == 2:
        sortret = controller.merge(targetList, target)
        time = sortret[1]
        targetListSorted = sortret[0]
        print(f'Se organizaron los archivos correctamente en {time}ms\n')
    elif int(IN[0]) == 3:
        sortret = controller.quick(targetList, target)
        time = sortret[1]
        targetListSorted = sortret[0]
        print(f'Se organizaron los archivos correctamente en {time}ms\n')
    elif int(IN[0]) == 4:
        sortret = controller.shell(targetList, target)
        time = sortret[1]
        targetListSorted = sortret[0]
        print(f'Se organizaron los archivos correctamente en {time}ms\n')
    return targetListSorted

def controllerR1R2(key,target,datei,datef, d_structure):
    print("Cargando información de los archivos ....")
    targetList = controller.createListR1R2(key,target, d_structure)
    pucharseCount = controller.loadTargetR1R2(targetList,target,datei,datef)
    targetListSorted = sortR1R2(targetList,target)
    return targetListSorted, pucharseCount
    
def visualizationR1R2(targetListSorted,target,datei,datef,pucharseCount):
    #date for artwork: 1944-06-06   1989-09-09
    first = lt.getElement(targetListSorted,1)
    second = lt.getElement(targetListSorted,2)
    third = lt.getElement(targetListSorted,3)
    size = lt.size(targetListSorted)
    secondToLast = lt.getElement(targetListSorted,size-2)
    nextToLast = lt.getElement(targetListSorted,size-1)
    last = lt.getElement(targetListSorted,size)
    preview = [first,second,third,secondToLast,nextToLast,last]
    if target == 'artists':
        print(f'\n\nHay {lt.size(targetListSorted)} artistas nacidos entre {datei} y {datef}.\n\n')
        print(f'A continuacion se imprimiran los primeros 3 y ultimos 3 artistas en el rango cronologico ->\n\n')
        for i in preview:
            print(f"NAME: {i['name']} | BIRTHDAY: {i['birthday']} | R.I.P {i['deathday']} | NATIONALITY: {i['nationality']} | GENERO: {i['gender']}\n\n")
    elif target == 'artworks':
        print(f'\n\nHay {lt.size(targetListSorted)} artworks entre {datei} y {datef}, donde {pucharseCount} fueron comparadas (pucharse).\n\n')
        print(f'A continuacion se imprimiran los primeros 3 y ultimos 3 artworks en el rango cronologico ->\n\n')
        for i in preview:
            print(f"Title: {i['Title']} | ConstituentID: {i['ConstituentID']} | DATE {i['DateAcquired']} | Medium: {i['Medium']} | Dimensions: {i['Dimensions']}\n\n")

######                 ######
######                 ######
######   REQUISITO 5   ######
######                 ######
######                 ######

def inputR5():
    department = input('Ingrese el departamento el cual desea investigar: \n')
    return department

def controllerR5(key,target,d_structure,department)-> tuple:
    print("Cargando información de los archivos ....")
    targetList = controller.createListR1R2(key,target, d_structure)
    targetListSorted = sortR1R2(targetList,'artists')
    collection = controller.loadArtworksR5(targetListSorted,department)
    pricef = collection[0]
    weightf = collection[1]
    top5 = collection[2]
    return targetListSorted, pricef, weightf, top5

def visualizationR5(targetListSorted,pricef,weightf,top5):
    #         Drawings & Prints
    print(f'Estimated cargo weight (kg): {weightf}')
    print(f'Estimated cargo cost (USD): {pricef}')
    print(f'Estimated number of elements in the cargo: {lt.size(targetListSorted)}') 
    #####
    print('\nTOP 5 OLDEST ARTWORKS ->\n\n')
    for i in range(1,6):
        element = lt.getElement(targetListSorted,i)
        titulo = element['Title']
        artistas = element['CreditLine']
        Classification = element['Classification']
        Date = element['Date']
        Medium = element['Medium']
        Dimensions = element['Dimensions']
        costo = element['costo transporte']
        print(f'TITULO: {titulo} | ARTISTA(S): {artistas} | Classification: {Classification} | Date DE LA OBRA: {Date} | Medium: {Medium} | Dimensions: {Dimensions} | COSTO DE TRANSPORTE: {costo}\n')
    #####
    print('\nTOP 5 BY COST ->\n\n')
    for i in top5:
        element = lt.getElement(targetListSorted,i[0])
        titulo = element['Title']
        artistas = element['CreditLine']
        Classification = element['Classification']
        Date = element['Date']
        Medium = element['Medium']
        Dimensions = element['Dimensions']
        costo = element['costo transporte']
        print(f'TITULO: {titulo} | ARTISTA(S): {artistas} | Classification: {Classification} | Date DE LA OBRA: {Date} | Medium: {Medium} | Dimensions: {Dimensions} | COSTO DE TRANSPORTE: {costo}\n')

######                 ######
######                 ######
######   REQUISITO 3   ######
######                 ######
######                 ######

"""
ARTIST FOR TEST = Louise Bourgeois

1. obtener el id del artista (checkear que sea diferente a None)
2. con el id del artistas crear una lista de obras hechas por ese autor
3. en el mismo loop de (2) obtener la lista de tecnicas con el numero de veces que aparecen
4. totalObras con lt.size(artworksListById)
5. dictTecnicas con (3)
6. bestTecnica con el artwork con mayor valor, loopear el diccionario (3) y 
guardar el curret high y su llave en variables y retornarlos
7. artworksListByBestTechnique con bestTecnica (6) se creara una nueva lista que sera 

TODO:
1. get id DONE
2. get artworksListById DONE
4. retornar size de artworksListById DONE 
5. get dictTecnicas en el loop de la funcion del controller de (2) para reducir complejidad DONE
6. get bestTecnica DONE
7. create nueva artworksListByBestTechnique a partir de iterar artworksListById (2) filtrando por tecnica para reducir complejidad DONE
"""

def controllerR3(author,d_structure):
    collection = controller.runFunctionsR3(author,d_structure)
    if collection == None:
        return None
    return collection

def visualizationR3(collection, author):
    artworksListByBestTechnique = collection[0]
    totalObras = collection[1]
    dictTecnicas = collection[2]
    bestTecnica = collection[3]
    timesUsedBestTecnica = dictTecnicas[bestTecnica]
    totalTecnicas = collection[4]
    print(f'\n\n\nEXAMINANDO LOS TRABAJOS DE {author} ->\n\n\n')
    print(f'Numero total de obras hechas por este artista: {totalObras}')
    print(f'Numero de tecnicas diferentes usadas por este artista: {totalTecnicas}')
    print(f'\nLa tecnica mas usada por {author} fue {bestTecnica}, usada {timesUsedBestTecnica} veces.')
    print(f'\n\nLas tecnicas usadas por {author} fueron: \n\n')
    for i in dictTecnicas.keys():
        times = dictTecnicas[i]
        print(f"TECNICA:  {i}   |   NUMERO DE VECES USADA:  {times}\n")
    print(f'\nUn ejemplo de 3 obras creadas por este artista con la tecnica {bestTecnica} son ->\n\n')
    count = 0
    for i in lt.iterator(artworksListByBestTechnique):
        if count == 3:
            break
        else:
            count+=1
        titulo = i['Title']
        Date = i['Date']
        Medium = i['Medium']
        dimensiones = i['Dimensions']
        print(f'TITULO: {titulo}\nFECHA DE LA OBRA: {Date}| MEDIO: {Medium}| DIMENSIONES: {dimensiones}\n\n')

######                 ######
######                 ######
######   REQUISITO 6   ######
######                 ######
######                 ######

"""
1. obtener inputs de area disponible en m^2 para objetos planos, año inicial y año final de las obras
2. cargar las obras que tengan la llave Date dentro de ese rango de años
3. obtener la sumatoria de m^2 de la lista (2) y asegurarse de seguir agregando hasta que no se pueda agregar mas

EFICIENCIA:
1. obtener inputs de area disponible en m^2 para objetos planos, año inicial y año final de las obras DONE
2. CONTROLLER:
    a. inicializar sumatoria de areas = 0 - CONTROLLER DONE
    i. crear una lista vacia para las obras que sean incluidas - MODEL DONE
    b. crear un loop de artworksfile en el controller - CONTROLLER DONE
    c. dentro del loop llamar a una funcion del model para obtener el area de una obra por parametro (si es un objeto plano) - MODEL
    d. calcular diferencia inputArea - (a) - CONTROLLER DONE
    e. checkear que (d) - (c) > 0, if True, then: (h), else (f) - CONTROLLER DONE
    h. agregar (c) a (a) y (j) - CONTROLLER DONE
    j. agregar elemento actual del loop (b) a (i) - MODEL DONE
    f. pass - CONTROLLER DONE 
    g. return (a) - CONTROLLER DONE
"""

def inputR6():
    datei = int(input('Introduce el año inicial: \n').strip())
    datef = int(input('Introduce el año final: \n').strip())
    inputArea = float(input('Introduce el area en m^2 disponible para los cuadros y fotos: \n').strip())
    return datei,datef,inputArea

def controllerR6(datei: int,datef: int,inputArea: int,d_structure):
    collection = controller.runFunctionsR6(datei,datef,inputArea,d_structure)
    return collection

def visualizacionR6(collection):
    artworkslist = collection[0]
    areaSum = collection[1]
    size = lt.size(artworkslist)
    print(f'Numero de obras: {size}')
    print(f'Area a utilizar: {areaSum}')
    print('\n\nPrimeras 5 y ultimas 5 obras ->\n\n')
    for i in range(1,6):
        e = lt.getElement(artworkslist,i)
        titulo = e['Title']
        Date = e['Date']
        Medium = e['Medium']
        dimensiones = e['Dimensions']
        artistas = e['CreditLine']
        clasificacion = e['Classification']
        print(f'TITULO: {titulo}\nFECHA DE LA OBRA: {Date}| MEDIO: {Medium}| DIMENSIONES: {dimensiones} | ARTISTAS: {artistas} | CLASIFICACION: {clasificacion}\n\n')
    for i in range(size-5,size+1):
        e = lt.getElement(artworkslist,i)
        titulo = e['Title']
        Date = e['Date']
        Medium = e['Medium']
        dimensiones = e['Dimensions']
        artistas = e['CreditLine']
        clasificacion = e['Classification']
        print(f'TITULO: {titulo}\nFECHA DE LA OBRA: {Date}| MEDIO: {Medium}| DIMENSIONES: {dimensiones} | ARTISTAS: {artistas} | CLASIFICACION: {clasificacion}\n\n')
######                             ######
######                             ######
######   VALORES PREDETERMINADOS   ######
######                             ######
######                             ######

sorted = False
sublist_input_runs = 0
catalog = None
d_structure = "LINKED_LIST"
complete_catalog = False
statusR1 = False
statusR2 = False

######                        ######
######                        ######
######     MENU PRINCIPAL     ######
######                        ######
######                        ######

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1 and '10' not in inputs:
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
            print('\n\n\n\nNO SE ENCONTRO CATALOGO ANTIGUO, ASI QUE SE CREARA EL PRIMER CATALOGO ->\n\n\n\n')
        print('\n\n\n\nCREANDO SUBLISTAS ->\n\n\n\n')
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
            print('Este catalogo ya esta organizado.')
        else:
            sortingPrints(catalog, None)
            sorted = True
    elif int(inputs[0]) == 5 or int(inputs[0]) == 6: #LISTAR CRONOLOGICAMENTE LOS ARTISTAS O ARTWORKS
        R1,R2 = False, False
        if int(inputs[0]) == 5:
            R1 = True
        elif int(inputs[0]) == 6:
            R2 = True
        if R1:
            if statusR1:
                print('Ya creaste usaste esta funcionalidad anteriormente, te visualizare los datos.')
                visualizationR1R2(targetListSorted,target,datei,datef,pucharseCount)
                continue
        elif R2:
            if statusR2:
                print('Ya creaste usaste esta funcionalidad anteriormente, te visualizare los datos.')
                visualizationR1R2(targetListSorted,target,datei,datef,pucharseCount)
                continue
        inputsR12 = inputsR1R2(R1,R2)
        datei = inputsR12[0]
        datef = inputsR12[1]
        req = inputsR12[2]
        #check if ran before
        if req == 1:
            target = 'artists'
            key = 'BeginDate'
        elif req == 2:
            target = 'artworks'
            key = 'DateAcquired'
        if datei == None or datef == None or req == None:
            print('Hay inputs incorrectos, por favor iniciar nuevamente.')
            continue
        else:
            start_time = time.process_time()
            collection = controllerR1R2(key,target,datei,datef, d_structure)
            targetListSorted = collection[0]
            pucharseCount = collection[1]
            visualizationR1R2(targetListSorted,target,datei,datef,pucharseCount)
            stop_time = time.process_time()
            elapsed_time_mseg = (stop_time - start_time)*1000
            print(f'TIEMPO {elapsed_time_mseg}')
            if req == 1:
                statusR1 = True
            elif req == 2:
                statusR2 = True
    elif  int(inputs[0]) == 9:
        department = inputR5()
        start_time = time.process_time()
        OUT = controllerR5(None,'artworks',d_structure,department)
        artworksListSorted = OUT[0]
        pricef = OUT[1]
        weightf = OUT[2]
        top5 = OUT[3]
        visualizationR5(artworksListSorted,pricef,weightf,top5)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(f'TIEMPO {elapsed_time_mseg}')
    elif int(inputs[0]) == 7:
        while True:
            author = input('Ingrese el nombre del autor que desea buscar: \n').strip()
            start_time = time.process_time()
            collection = controllerR3(author,d_structure)
            if collection == None:
                print('Por favor ingresar un nombre valido.')
                continue
            else:
                visualizationR3(collection,author)
                stop_time = time.process_time()
                elapsed_time_mseg = (stop_time - start_time)*1000
                print(f'TIEMPO {elapsed_time_mseg}')
                break
    elif int(inputs[:2]) == 10:
        collectionInputs = inputR6()
        start_time = time.process_time()
        datei = collectionInputs[0]
        datef = collectionInputs[1]
        inputArea = collectionInputs[2]
        collection = controllerR6(datei,datef,inputArea,d_structure)
        visualizacionR6(collection)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(f'TIEMPO {elapsed_time_mseg}')
    else:
        sys.exit(0)
sys.exit(0)