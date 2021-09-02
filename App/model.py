#IMPORTS
import config as cf
from DISClib.ADT import list as lt
assert cf

# Construccion de modelos
def newCatalog():
    catalog = {
        'artworks': None,
        'artists':None,
    }
    catalog['artworks'] = lt.newList("ARRAY_LIST")
    catalog['artists'] = lt.newList("ARRAY_LIST")
    return catalog
# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    artistnew = newArtist()
    addInfoArtist(artistnew,artist)
    lt.addLast(catalog['artists'],artistnew)
def addArtwork(catalog, artwork):
    artworknew = newArtwork()
    addInfoArtwork(artworknew,artwork)
    lt.addLast(catalog['artworks'],artworknew)
# Funciones para agregar informacion a los diccionarios de artistas y artworks
def addInfoArtist(artistnew,artist):
    artistnew['name'] = artist['DisplayName']
    artistnew['nationality'] = artist['Nationality']
    artistnew['gender'] = artist['Gender']
    artistnew['birthday'] = artist['BeginDate']
    artistnew['ID'] = artist['ConstituentID']
def addInfoArtwork(artworknew,artwork):
    artworknew['title'] = artwork['Title']
    artworknew['fecha'] = artwork['DateAcquired']
    artworknew['medio'] = artwork['Medium']
    artworknew['dimensiones'] = artwork['Dimensions']
    artworknew['AuthorID'] = artwork['ConstituentID']
# Funciones para creacion de datos
def newArtist():
    artistnew = {'name':None,'nationality':None,'gender':None,'birthday':None,'ID':None}
    return artistnew
def newArtwork():
    artworknew = {'title':None,'fecha':None,'medio':None,'dimensiones':None,'artistID':None}
    return artworknew