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

def initCatalog(d_structure,pos,numelem_artworks,numelem_artists, prev_catalog):
    """
    Llama la funcion de inicializacion del catalogo del modelo con parametro el tipo de lista para representar los datos.
    """
    catalog = model.newCatalog(d_structure,pos,numelem_artworks,numelem_artists, prev_catalog)
    return catalog
    
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
    
def insert(catalog):
    model.insertionsorting(catalog)

def merge(catalog):
    model.mergesorting(catalog)

def quick(catalog):
    model.quicksorting(catalog)

def shell(catalog):
    model.shellsorting(catalog)
