#IMPORTS
import sys
from DISClib.ADT import list as lt
assert cf
import config as cf
import csv
from DISClib.Algorithms.Sorting import shellsort as sa

#MODEL

def newCatalog():
    catalog = {
        'artworks': None,
        'artists':None,
    }
    catalog['artwroks'] = lt.newList()
    catalog['artists'] = lt.newList()
    return catalog

def addArtwork_and_Artist_to_catalog(catalog,artist,artwork):
    artistas = catalog['artists']
    name = artist['name']
    if lt.isPresent(artistas,name) != 0:
        artist_info = newArtist()
        artwork_info = newArtwork()
        includeArtworks(artist_info,artwork_info)
        lt.addLast(catalog['artists'],artist_info)
        lt.addLast(catalog['artworks'],artwork_info)

def newArtwork(artwork):
    artwork_out = {'title':None,'fecha':None,'medio':None,'dimensiones':None,'artistID':None}
    artwork_out['title'] = artwork['Title']
    artwork_out['fecha'] = artwork['DateAcquired']
    artwork_out['medio'] = artwork['Medium']
    artwork_out['dimensiones'] = artwork['Dimensions']
    artwork_out['ID'] = artwork['ConstituentID']
    return artwork_out

def newArtist(artist):
    artist_out = {'name':None,'nationality':None,'gender':None,'birthday':None, 'artworks':None, 'ID':None}
    artist_out['name'] = artist['DisplayName']
    artist_out['nationality'] = artist['Nationality']
    artist_out['gender'] = artist['Gender']
    artist_out['birthday'] = artist['BeginDate']
    artist_out['ID'] = artist['ConstituentID']
    artist_out['artworks'] = lt.newList()
    return artist_out

def includeArtworks(artist_info,artwork_info):
    pass