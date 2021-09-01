#IMPORTS
import sys
from DISClib.ADT import list as lt
assert cf
import config as cf
import csv
from DISClib.Algorithms.Sorting import shellsort as sa
import model

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

