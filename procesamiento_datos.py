#procesamiento_datos.py
import pandas as pd
import numpy as np
#import os

data_cines = pd.read_csv('cines/2022-mayo/cines-26-05-2022.csv')
data_museos = pd.read_csv('museos/2022-mayo/museos-26-05-2022.csv')
data_bibliotecas = pd.read_csv('bibliotecas/2022-mayo/bibliotecas-26-05-2022.csv')

nombres_columnas = ['cod_localidad',
				 'id_provincia',
				 'id_departamento',
				 'categoría',
				 'provincia',
				 'localidad',
				 'nombre',
				 'domicilio',
				 'código postal',
				 'número de teléfono',
				 'mail',
				 'web']

data_cines.rename(columns = {'Cod_Loc': 'cod_localidad',
						 	 'IdProvincia': 'id_provincia',
						 	 'IdDepartamento': 'id_departamento',
						 	 'Categoría': 'categoría',
						 	 'Provincia': 'provincia',
						 	 'Localidad': 'localidad',
						 	 'Nombre': 'nombre',
						 	 'Dirección': 'domicilio',
							  'CP': 'código postal',
						 	 'Teléfono': 'número de teléfono',
						 	 'Mail': 'mail',
						 	 'Web': 'web'}, inplace = True)

data_cines['número de teléfono'] = np.where(data_cines.cod_area == 's/d',data_cines['número de teléfono'], data_cines.cod_area + data_cines['número de teléfono'])

data_cines.domicilio = np.where(data_cines.Piso == 's/d', data_cines.domicilio, data_cines.domicilio + ' ' + data_cines.Piso)

for column in data_cines.columns:
	if column not in nombres_columnas:
		del data_cines[column]



#Selecciono codigo de area y telefono
#data_cines_tel = data_cines[['cod_area', 'número de teléfono']]

#Selecciono las que tienen solo datos validos
#data_cines_tel = data_cines_tel[(data_cines_tel['cod_area'] != 's/d') &
#			                    (data_cines_tel['número de teléfono'] != 's/d')]
