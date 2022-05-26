'''
Challenge Data Analytics y Python de Alkemy
'''

import pandas as pd
import requests
import datetime
import os
import locale

locale.setlocale(locale.LC_TIME, 'es_ES')
fecha = datetime.date.today()
fecha_str = fecha.strftime('%d-%m-%Y')
mes = fecha.strftime('%Y-%B')


#Lista de URLs al 23/03/2022 19 hs--
url_cines = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
url_museos = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv'
url_bibliotecas = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'
lista_urls = [(url_cines, 'cines'), (url_museos, 'museos'), (url_bibliotecas, 'bibliotecas')]



#Uso os.makedirs() para crear varios directorios embebidos a la vez. si no da error
os.makedirs(f'museos/{mes}') #Uso comillas dobles en f"...('...')", porque da error si no
os.makedirs(f'bibliotecas/{mes}') 
os.makedirs(f'cines/{mes}') 

#Descarga los archivos con sus nombres
#def funcion?
for tupla in lista_urls:
    request = requests.get(tupla[0])
    url_content = request.content
    csv_file = open(f'{tupla[1]}/{mes}/{tupla[1]}-{fecha_str}.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()





