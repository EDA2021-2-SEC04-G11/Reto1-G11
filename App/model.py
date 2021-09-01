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

def newCatalogArtist():
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

def newCatalogArtworks():
    catalog = {'ObjectID': None,
               'Title': None,
               'ConstituentID': None,
               'Date': None,
               'Medium': None,
               'Dimensions': None,
               'CreditLine': None,
               'AccessionNumber': None,
               'Classification': None,
               'Department': None,
               'DateAcquired': None,
               'Cataloged': None,
               'URL': None,
               'Circumference (cm)': None,
               'Depth (cm)': None,
               'Diameter (cm)': None,
               'Height (cm)': None,
               'Length (cm)': None,
               'Weight (kg)': None,
               'Width (cm)': None,
               'Seat Height (cm)': None,
               'Duration (sec.)': None,
               }
    catalog['ObjectID'] = lt.newList()
    catalog['Title'] = lt.newList()
    catalog['ConstituentID'] = lt.newList()
    catalog['Date'] = lt.newList()
    catalog['Medium'] = lt.newList()
    catalog['Dimensions'] = lt.newList()
    catalog['CreditLine'] = lt.newList()
    catalog['AccessionNumber'] = lt.newList()
    catalog['Classification'] = lt.newList()
    catalog['Department'] = lt.newList()
    catalog['DateAcquired'] = lt.newList()
    catalog['Cataloged'] = lt.newList()
    catalog['URL'] = lt.newList()
    catalog['Circumference (cm)'] = lt.newList()
    catalog['Depth (cm)'] = lt.newList()
    catalog['Diameter (cm)'] = lt.newList()
    catalog['Height (cm)'] = lt.newList()
    catalog['Length (cm)'] = lt.newList()
    catalog['Weight (kg)'] = lt.newList()
    catalog['Width (cm)'] = lt.newList()
    catalog['Seat Height (cm)'] = lt.newList()
    catalog['Duration (sec.)'] = lt.newList()

    return catalog

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento