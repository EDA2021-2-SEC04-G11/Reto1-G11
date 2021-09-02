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

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalogArts():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalogArts()
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadConstituentID(catalog)
    loadDisplayName(catalog)
    loadArtistBio(catalog)
    loadNationality(catalog)
    loadGender(catalog)
    loadBeginDate(catalog)
    loadEndDate(catalog)
    loadWiki_QID(catalog)
    loadULAN(catalog)

def loadConstituentID(catalog):
    file = cf.data_dir + 'MoMa/artists-utf8-small.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for id in input_file:
        model.addIdFile(catalog, id)

def loadDisplayName(catalog):
    file = cf.data_dir + 'MoMa/artists-utf8-small.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for display in input_file:
        model.addDisplayFile(catalog, display)

def loadArtistBio(catalog):
    file = cf.data_dir + 'MoMa/artists-utf8-small.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for bio in input_file:
        model.addBioFile(catalog, bio)

def loadNationality(catalog):
    file = cf.data_dir + 'MoMa/artists-utf8-small.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for Nationality in input_file:
        model.addNationalityFile(catalog, Nationality)

def loadGender(catalog):
    file = cf.data_dir + 'MoMa/artists-utf8-small.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for gender in input_file:
        model.addGenderFile(catalog, gender)

def loadBeginDate(catalog):
    file = cf.data_dir + 'MoMa/artists-utf8-small.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for begin in input_file:
        model.addBeginDateFile(catalog, begin)

def loadEndDate(catalog):
    file = cf.data_dir + 'MoMa/artists-utf8-small.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for end in input_file:
        model.addEndDateFile(catalog, end)

def loadWiki_QID(catalog):
    file = cf.data_dir + 'MoMa/artists-utf8-small.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for wiki in input_file:
        model.addWikiFile(catalog, wiki)

def loadULAN(catalog):
    file = cf.data_dir + 'MoMa/artists-utf8-small.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for ulan in input_file:
        model.addUlanFile(catalog, ulan)

# Funciones de ordenamiento
def sortArtists(catalog):
    
    model.sortArtist(catalog)

# Funciones de consulta sobre el catálogo
def getArtistsByNationality(catalog):
    
