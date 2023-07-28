import requests as requests
import json

def lista_nombre_paises(url):

    paises = requests.get(url)
    paises = paises.json()

    for pais in paises:

        #NOMBRE OFICIAL EN ESPAÑOL
        print(f"NOMBRE DEL PAIS: {pais['translations']['spa']['official']}")

        #Población
        print(f"CON UNA POBLACIÓN DE:{pais['population']}")

        #Area
        print(f"CON UNA ÁREA DE:{pais['area']}")

        # Cual es el país con mayor población
        poblacion_max = max(paises, key=lambda pais:pais['population'])
        print("EL PAÍS CON MAYOR POBLACIÓN ES:",poblacion_max['translations']['spa']['official'],",Con una poblacion de:",poblacion_max['population'])

        # Cual es el país con mayor area
        area_max = max(paises, key=lambda pais:pais['area'])
        print("EL PAÍS CON MAYOR ÁREA ES:", area_max['translations']['spa']['official'],",Su area es de:", area_max['area'])

        #Cual es la poblacion total
        total = sum(pais['population'] for pais in paises)
        print("LA POBLACIÓN TOTAL ES:",total)

        #Media de la poblacion
        media = total/ len(paises)
        print("LA MEDIA DE LA POBLACIÓN ES:",media)

        #Mediana de la poblacion
        mediana = paises[len(paises) //2] ['population']
        print("LA MEDIANA DE LA POBLACIÓN ES:",mediana)

        #Moda de la poblacion
        moda = max(pais['population'] for pais in paises)
        print("LA MODA DE LA POBLACIÓN ES:",moda)


url = 'https://restcountries.com/v3.1/all'
lista_nombre_paises(url)