#IMPORTS
import config as cf
import model
import csv

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)
def loadArtists(catalog):
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    artistsFile = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in artistsFile:
        model.addArtist(catalog,artist)
def loadArtworks(catalog):
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    artworksFile = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in artworksFile:
        model.addArtwork(catalog,artwork)