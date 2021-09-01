import config as cf
import model
import csv
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
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

def loadArtists(catalogArtist):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalogArtist, artist)
        #print(artist)

def loadArtworks(catalogArtworks):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalogArtworks, artwork)
        #print(artwork)

def test():
    A = newCatalogArtist
    W = newCatalogArtworks
    loadArtists(A)
    loadArtworks(W)
#test()