#IMPORTS
import sys
from DISClib.ADT import list as lt
assert cf
import config as cf
import csv
from DISClib.Algorithms.Sorting import shellsort as sa

#VIEW

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- ")

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Libros cargados: ' + str(lt.size(catalog['books'])))
        print('Autores cargados: ' + str(lt.size(catalog['authors'])))
        print('Géneros cargados: ' + str(lt.size(catalog['tags'])))
        print('Asociación de Géneros a Libros cargados: ' + str(lt.size(catalog['book_tags'])))

    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)

#CONTROLLER

def initCatalog():
    pass


def loadArtist_and_Artworks(catalogArtist):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file_artists = csv.DictReader(open(artistsfile, encoding='utf-8'))
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file_artworks = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artist, artwork in input_file_artists,input_file_artworks:
        model.addArtwork_and_Artist_to_catalog(catalogArtist, artist, artwork)
        #print(artist)

def loadData():
    pass

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
    if artwork_info['ID'] == artist_info['artistID']:
        lt.addLast(artist_info['artworks'],artwork_info['title'])