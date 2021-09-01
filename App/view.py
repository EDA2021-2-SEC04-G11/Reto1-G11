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