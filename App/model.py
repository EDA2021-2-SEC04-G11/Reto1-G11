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
    
def addInfoArtwork(artworknew,artwork):
    """
    Añade la información de una determinada obra.
    """
    artworknew['title'] = artwork['Title']
    artworknew['fecha'] = artwork['DateAcquired']
    artworknew['medio'] = artwork['Medium']
    artworknew['dimensiones'] = artwork['Dimensions']
    artworknew['AuthorID'] = artwork['ConstituentID']

# Funciones para creacion de datos
def newArtist():
    """
    Crea un nuevo artista.
    Retorna el artista.
    """
    artistnew = {'name':None,'nationality':None,'gender':None,'birthday':None,'ID':None}
    return artistnew

def newArtwork():
    """
    Crea una nueva obra.
    Retorna la obra.
    """

    artworknew = {'title':None,'fecha':None,'medio':None,'dimensiones':None,'artistID':None}
    return artworknew