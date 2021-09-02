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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalogArts():
    catalog = {'ConstituentID': None,
               'DisplayName': None,
               'ArtistBio': None,
               'Nationality': None,
               'Gender': None,
               'BeginDate': None,
               'EndDate': None,
               'Wiki QID': None,
               'ULAN': None}
    catalog['ConstituentID'] = lt.newList()
    catalog['DisplayName'] = lt.newList()
    catalog['ArtistBio'] = lt.newList()
    catalog['Nationality'] = lt.newList()
    catalog['Gender'] = lt.newList()
    catalog['BeginDate'] = lt.newList()
    catalog['EndDate'] = lt.newList()
    catalog['Wiki QID'] = lt.newList()
    catalog['ULAN'] = lt.newList()

    return catalog

# Funciones para agregar informacion al catalogo
def addIdFile(catalog, id):
    # Se adiciona el id a la lista de ids
    lt.addLast(catalog['ConstituentID'], id[0])

def addDisplayFile(catalog, display):
    lt.addLast(catalog['DisplayName'], display[1])
    
def addBioFile(catalog, bio):
    lt.addLast(catalog['ArtistBio'], bio[2])

def addNationalityFile(catalog, Nationality):
    lt.addLast(catalog['Nationality'], Nationality[3])

def addGenderFile(catalog, gender):
    lt.addLast(catalog['Gender'], gender[4])

def addBeginDateFile(catalog, begin):
    lt.addLast(catalog['BeginDate'], begin[5])

def addEndDateFile(catalog, end):
    lt.addLast(catalog['EndDate', end[6]])

def addWikiFile(catalog, wiki):
    lt.addLast(catalog['Wiki QID'], wiki[7])

def addUlanFile(catalog, ulan):
    lt.addLast(catalog['ULAN'], ulan[8])

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def compareratings(artist1, artist2):
    return (float(artist1['ConstituentID']) > float(artist2['ConstituentID']))

# Funciones de ordenamiento
def sortArtist(catalog):
    sa.sort(catalog['DisplayName'], compareratings)