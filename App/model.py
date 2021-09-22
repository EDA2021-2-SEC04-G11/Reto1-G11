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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
"""


import config as cf
from DISClib.ADT import list as lt
assert cf
import datetime
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
from DISClib.Algorithms.Sorting import shellsort as shell
import time

# Construccion de modelos
def newCatalog(d_structure):
    """
    Crea un diccionario de listas llamado "catalogo".
    """
    catalog = {
            'artworks': None,
            'artists':None,
        }
    
    catalog['artworks'] = lt.newList(d_structure)
    catalog['artists'] = lt.newList(d_structure)
    return catalog


######                     ######
######                     ######
######   REQUISITO 1 y 2   ######
######                     ######
######                     ######

def createVoidListR1R2(key,target,d_structure):
    cmpfunction = None
    if target == 'artists':
        cmpfunction = cmpArtistsByYear
    elif target == 'artworks':
        cmpfunction = cmpArtworkByDateAcquired
    targetListVoid = lt.newList(d_structure,cmpfunction,key)
    return targetListVoid
        
def addArtistR1R2(targetList, artist):
    artistnew = newArtist()
    addInfoArtist(artistnew,artist)
    lt.addLast(targetList,artistnew)

def addArtworkR1R2(targetList, artwork, price):
    artworknew = newArtwork()
    addInfoArtwork(artworknew,artwork,price)
    lt.addLast(targetList,artworknew)

def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
        artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
        artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    ret = False
    if artwork1['fecha de adquisicion'] != '' :
        date1 = datetime.date.fromisoformat(artwork1['fecha de adquisicion'])
    else:
        date1 = datetime.date.today()
    if artwork2['fecha de adquisicion'] != '':
        date2 = datetime.date.fromisoformat(artwork2['fecha de adquisicion'])
    else:
        date2 = datetime.date.today()
    if date1 < date2:
        ret = True
    return ret

def cmpArtistsByYear(artist1: int, artist2: int):
    year1 = artist1['birthday']
    year2 = artist2['birthday']
    ret = False
    if year1 < year2:
        ret = True
    return ret

######                 ######
######                 ######
######   REQUISITO 5   ######
######                 ######
######                 ######

def getPriceR5(artwork,top5,ipos)->float:
    """
    Obtiene el precio de cada obra y lo retorna
    """
    #ipos is the position of current artwork in the lt.list
    # height, lenght, depth, width
    methods = []
    rate = 72
    pi = 3.141592
    priceStandard = 48
    highest = 0
    top5c = top5
    h =  artwork['Height (cm)']
    l =  artwork['Length (cm)']
    d =  artwork['Depth (cm)']
    w =  artwork['Width (cm)']
    area = 0
    volumen = 0
    hbool,lbool,dbool,wbool = False,False,False,False
    if h != '':
        h = float(h)/100
        hbool = True
    elif l != '':
        l = float(h)/100
        lbool = True
    if d != '':
        d = float(h)/100
        dbool = True
    if w != '':
        w = float(h)/100
        wbool = True
    ######
    areal = []
    print(hbool,lbool,dbool,wbool)
    if hbool and dbool:
        areal.append(h*d)
    if lbool and dbool:
        areal.append(l*d)
    if hbool and wbool:
        areal.append(h*w)
    if lbool and wbool:
        areal.append(l*w)
    if wbool and dbool:
        areal.append(w*d)
    if len(areal) > 1:
        area = max(areal)
    elif len(areal) < 1 and len(areal) != 0:
        area = areal[0]
    if hbool and dbool and wbool:
        volumen = h*d*w
    elif lbool and dbool and wbool:
        volumen = l*d*w
    ######
    if area != 0:
        methods.append(area*rate)
    if volumen != 0:
        methods.append(volumen*rate)
    ################
    if len(methods) == 0:
        highest = priceStandard
    else:
        for i in methods:
            pricei = rate*i
            if pricei > highest:
                highest = pricei
    if top5c == [] or len(top5c) < 5:
        top5.append((ipos,highest))
    else:
        for i in range(len(top5c)):
            if highest > top5c[i][1]:
                top5c[i] = (ipos,highest)
    print(methods)
    return highest,top5c

######                  ######
######                  ######
######   SUBFUNCTIONS   ######
######                  ######
######                  ######


def createSublist(catalog,pos,value):
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

# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    """
    Anñade un nuevo artista al catalogo.
    """
    artistnew = newArtist()
    addInfoArtist(artistnew,artist)
    lt.addLast(catalog['artists'],artistnew)

def addArtwork(catalog, artwork):
    """
    Añade una nueva obra al catalogo.
    """
    artworknew = newArtwork()
    addInfoArtwork(artworknew,artwork)
    lt.addLast(catalog['artworks'],artworknew)

# Funciones para agregar informacion a los diccionarios de artistas y artworks
def addInfoArtist(artistnew,artist):
    """
    Añade la información de un determinado artista.
    """
    artistnew['name'] = artist['DisplayName']
    artistnew['nationality'] = artist['Nationality']
    artistnew['gender'] = artist['Gender']
    artistnew['birthday'] = artist['BeginDate']
    artistnew['ID'] = artist['ConstituentID']
    
def addInfoArtwork(artworknew,artwork,price):
    """
    Añade la información de una determinada obra.
    """
    artworknew['title'] = artwork['Title']
    artworknew['fecha de adquisicion'] = artwork['DateAcquired']
    artworknew['medio'] = artwork['Medium']
    artworknew['dimensiones'] = artwork['Dimensions']
    artworknew['AuthorID'] = artwork['ConstituentID']
    artworknew['weight'] = artwork['Weight (kg)']
    artworknew['height'] = artwork['Height (cm)']
    artworknew['length'] = artwork['Length (cm)']
    artworknew['width'] = artwork['Width (cm)']
    artworknew['department'] = artwork['Department']
    artworknew['clasificacion'] = artwork['Classification']
    artworknew['fecha'] = artwork['Date']
    artworknew['autores'] = artwork['CreditLine']
    artworknew['costo transporte'] = price

# Funciones para creacion de datos
def newArtist():
    """
    Crea un nuevo artista.
    Retorna el artista.
    """
    artistnew = {'name':None,'nationality':None,'gender':None,'birthday':None,'ID':None,'deathday':None,}
    return artistnew

def newArtwork():
    """
    Crea una nueva obra.
    Retorna la obra.
    """
    artworknew = {'title':None,'fecha de adquisicion':None,'medio':None,'dimensiones':None,'artistID':None,
    'weight':None,'height':None,'length':None,'width':None, 'department':None,'costo transporte':None,
     'clasificacion':None, 'fecha':None, 'autores':None}
    return artworknew

# SORTING

def insertionsorting(lst, target):
    cmpfunction = cmpArtworkByDateAcquired
    if target == 'artists':
        cmpfunction = cmpArtistsByYear
    start_time = time.process_time()
    ordenada = insertion.sort(lst,cmpfunction)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return (ordenada, f'time: {elapsed_time_mseg}')

def mergesorting(lst, target):
    cmpfunction = cmpArtworkByDateAcquired
    if target == 'artists':
        cmpfunction = cmpArtistsByYear
    start_time = time.process_time()
    ordenada = merge.sort(lst, cmpfunction)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return (ordenada, f'time: {elapsed_time_mseg}')
     
def quicksorting(lst, target):
    cmpfunction = cmpArtworkByDateAcquired
    if target == 'artists':
        cmpfunction = cmpArtistsByYear
    start_time = time.process_time()
    ordenada = quick.sort(lst, cmpfunction)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return (ordenada, f'time: {elapsed_time_mseg}')
    
def shellsorting(lst, target):
    cmpfunction = cmpArtworkByDateAcquired
    if target == 'artists':
        cmpfunction = cmpArtistsByYear
    start_time = time.process_time()
    ordenada = shell.sort(lst, cmpfunction)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return (ordenada, f'time: {elapsed_time_mseg}')
