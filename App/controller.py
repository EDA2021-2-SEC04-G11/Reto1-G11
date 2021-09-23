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
"""

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

import config as cf
import model
import csv
import datetime

def initCatalog(d_structure):
    """
    Llama la funcion de inicializacion del catalogo del modelo con parametro el tipo de lista para representar los datos.
    """
    catalog = model.newCatalog(d_structure)
    return catalog


######                     ######
######                     ######
######   REQUISITO 1 y 2   ######
######                     ######
######                     ######

def createListR1R2(key,target, d_structure):
    targetList = model.createVoidListR1R2(key,target,d_structure)
    return targetList

def loadTargetR1R2(targetList,target,datei,datef):
    count = None
    if target == 'artists':
        loadArtistsR1R2(targetList,datei,datef)
    elif target == 'artworks':
        count = loadArtworksR1R2(targetList,datei,datef)
    return count

def loadArtistsR1R2(targetList,datei,datef):
    """
    Carga el archivo de artistas y lo agrega al catalogo de artistas.
    """
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    artistsFile = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in artistsFile:
        dartist = int(artist['BeginDate'])
        if int(datei) <= dartist and int(datef) >= dartist:
            model.addArtistR1R2(targetList,artist)
    
def loadArtworksR1R2(targetList,datei,datef):
    """
    Carga el archivo de obras y lo agrega al catalogo de obras.
    """
    count = 0
    di = datetime.date.fromisoformat(datei)
    df = datetime.date.fromisoformat(datef)
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    artworksFile = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in artworksFile:
        if 'Purchase' in artwork['CreditLine']:
            count+=1
        dartwork = artwork['DateAcquired']
        if dartwork != '':
            dartwork = datetime.date.fromisoformat(dartwork)
            if di <= dartwork and df >= dartwork:
                model.addArtworkR1R2(targetList,artwork,None)
    return count

######                 ######
######                 ######
######   REQUISITO 3   ######
######                 ######
######                 ######

def runFunctionsR3(author,d_structure):
    id = getAuthorIdR3(author)
    if id == None:
        return None
    collection = get_artworksListByIdR3(id,d_structure)
    artworksListById = collection[0]
    totalObras = model.get_size_artworksListByIdR3(artworksListById)
    dictTecnicas = collection[1]
    totalTecnicas = len(dictTecnicas.keys())
    bestTecnica = model.get_bestTecnicaR3(dictTecnicas)
    artworksListByBestTechnique = artworksListByBestTechniqueR3(artworksListById,bestTecnica,d_structure)
    return artworksListByBestTechnique, totalObras, dictTecnicas,bestTecnica,totalTecnicas

def getAuthorIdR3(author)->str:
    id = None
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    artistsFile = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in artistsFile:
        if author in artist['DisplayName']:
            id = artist['ConstituentID']
            break
    return id

def get_artworksListByIdR3(id: str,d_structure):
    dictTecnicas = {}
    artworksListById = model.create_artworksListR3(d_structure)
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    artworksFile = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in artworksFile:
        if id in artwork['ConstituentID'].strip('[]').replace(' ','').split(','):
            model.add_dictTecnicasR3(dictTecnicas,artwork)
            model.add_artworksListR3(artworksListById,artwork)
    return artworksListById, dictTecnicas

def artworksListByBestTechniqueR3(artworksListById,bestTecnica,d_structure):
    return model.create_artworksListByBestTechniqueR3(artworksListById,bestTecnica,d_structure)

######                 ######
######                 ######
######   REQUISITO 5   ######
######                 ######
######                 ######

def loadArtworksR5(targetList,department):
    """
    Carga el archivo de obras y lo agrega al catalogo de obras.
    """
    top5 = []  # lista de 5 elementos donde cada uno se vera asi: (ipos,price)
    ipos = 0
    pricef = 0
    weightf = 0
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    artworksFile = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in artworksFile:
        if artwork['Department'] == department:
            ipos += 1
            collection = model.getPriceR5(artwork,top5,ipos)
            price = collection[0]
            top5 = collection[1]
            model.addArtworkR1R2(targetList,artwork,price)
            pricef += price
            if artwork['Weight (kg)'] != '':
                weightf += float(artwork['Weight (kg)'])
    return pricef,weightf,top5

######                  ######
######                  ######
######   SUBFUNCTIONS   ######
######                  ######
######                  ######


def createSublist(catalog,pos,value):
    return model.createSublist(catalog,pos,value)
    
def loadData(catalog):
    """
    Carga los datos de los archivos y carga los datos en la
    estructura de datos.
    """
    loadArtists(catalog)
    loadArtworks(catalog)

def loadArtists(catalog):
    """
    Carga el archivo de artistas y lo agrega al catalogo de artistas.
    """
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    artistsFile = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in artistsFile:
        model.addArtist(catalog,artist)

def loadArtworks(catalog):
    """
    Carga el archivo de obras y lo agrega al catalogo de obras.
    """
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    artworksFile = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in artworksFile:
        model.addArtwork(catalog,artwork)
    
def insert(catalog,target):
    return model.insertionsorting(catalog, target)

def merge(catalog,target):
    return model.mergesorting(catalog, target)

def quick(catalog,target):
    return model.quicksorting(catalog, target)

def shell(catalog,target):
    return model.shellsorting(catalog,target)
