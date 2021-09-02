#IMPORTS
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronologicamente los artistas")
    print("3- Listar cronologicamente las adquisiciones")
    print("4- clasificar las obras de un artista por técnica")
    print("5- clasificar las obras por la nacionalidad de sus creadores")
    print("6- transportar obras de un departamento")
    print("7- Reglas de transporte")
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
def printLastArtists(catalog):
    size = lt.size(catalog['artists'])
    parent = lt.getElement(catalog['artists'],size)
    firstChild = lt.getElement(catalog['artists'],size-1)
    secondChild = lt.getElement(catalog['artists'],size-2)
    print(parent,'\n')
    print(firstChild,'\n')
    print(secondChild,'\n')
def printLastArtworks(catalog):
    size = lt.size(catalog['artworks'])
    parent = lt.getElement(catalog['artworks'],size)
    firstChild = lt.getElement(catalog['artworks'],size-1)
    secondChild = lt.getElement(catalog['artworks'],size-2)
    print(parent,'\n')
    print(firstChild,'\n')
    print(secondChild,'\n')
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
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Artworks cargados: ' + str(lt.size(catalog['artworks'])))
        print('Ultimos 3 elementos del archivo de artistas:')
        printLastArtists(catalog)
        print('Ultimos 3 elementos del archivo de artworks:')
        printLastArtworks(catalog)
    else:
        sys.exit(0)
sys.exit(0)