import statistics
import requests

from statistics import median

def obtener_datos_paises(url):
    paises = requests.get(url)
    paises = paises.json()
    return paises

def encontrar_pais_con_mayor_poblacion(paises):
    pais_mayor_poblacion = max(paises, key=lambda x: x['population'])
    return pais_mayor_poblacion

def encontrar_pais_con_mayor_area(paises):
    pais_mayor_area = max(paises, key=lambda x: x['area'])
    return pais_mayor_area

def calcular_poblacion_total(paises):
    poblacion_total = sum(pais['population'] for pais in paises)
    return poblacion_total

def calcular_media_poblacion(paises):
    poblacion_lista = [pais['population'] for pais in paises]
    media_poblacion = sum(poblacion_lista) / len(poblacion_lista)
    return media_poblacion

def calcular_mediana_poblacion(paises):
    poblacion_lista = [pais['population'] for pais in paises]
    mediana_poblacion = median(poblacion_lista)
    return mediana_poblacion

def calcular_moda_poblacion(paises):
    poblacion_lista = [pais['population'] for pais in paises]
    # Nota: Si hay varias modas, statistics.mode() arrojará la primera moda encontrada en la lista.
    moda_poblacion = statistics.mode(poblacion_lista)
    return moda_poblacion

def listar_nombre_paises(url):
    paises = obtener_datos_paises(url)
    pais_mayor_poblacion = encontrar_pais_con_mayor_poblacion(paises)
    pais_mayor_area = encontrar_pais_con_mayor_area(paises)

    for pais in paises:
        print(f"Nombre Oficial en Español: {pais['translations']['spa']['official']}")
        print(f"Su población es de: {pais['population']} habitantes.")
        print(f"Con un área de: {pais['area']} km²")
        print("-----")

    poblacion_total = calcular_poblacion_total(paises)
    media_poblacion = calcular_media_poblacion(paises)
    mediana_poblacion = calcular_mediana_poblacion(paises)
    moda_poblacion = calcular_moda_poblacion(paises)

    print(f"El país de mayor población es {pais_mayor_poblacion['translations']['spa']['official']} "
          f"con una población de {pais_mayor_poblacion['population']} habitantes.")
    print(f"El país de mayor área es {pais_mayor_area['translations']['spa']['official']} "
          f"con un área de {pais_mayor_area['area']} km².")
    print(f"La población total de todos los países es de {poblacion_total} habitantes.")
    print(f"La media de población de todos los países es de {media_poblacion} habitantes.")
    print(f"La mediana de población de todos los países es de {mediana_poblacion} habitantes.")
    print(f"La moda de población de todos los países es de {moda_poblacion} habitantes.")

url = 'https://restcountries.com/v3.1/independent?status=true&fields=translations,population,area'
listar_nombre_paises(url)