#procesamiento_datos.py
import pandas as pd
import numpy as np

df_cines = pd.read_csv('cines/2022-mayo/cines-28-05-2022.csv')
df_museos = pd.read_csv('museos/2022-mayo/museos-28-05-2022.csv')
df_bibliotecas = pd.read_csv('bibliotecas/2022-mayo/bibliotecas-28-05-2022.csv')

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

df_cines.rename(columns = {'Cod_Loc': 'cod_localidad',
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

df_cines['número de teléfono'] = np.where(df_cines.cod_area == 's/d',
										  df_cines['número de teléfono'],
										  df_cines.cod_area + ' ' + df_cines['número de teléfono'])

df_cines.domicilio = np.where(df_cines.Piso == 's/d',
							  df_cines.domicilio, 
							  df_cines.domicilio + ' ' + df_cines.Piso)

for column in df_cines.columns:
	if column not in nombres_columnas:
		del df_cines[column]


df_museos.rename(columns = {'Cod_Loc': 'cod_localidad',
						 	 'IdProvincia': 'id_provincia',
						 	 'IdDepartamento': 'id_departamento',
						 	 'categoria': 'categoría', 
						 	 'direccion': 'domicilio',
							  'CP': 'código postal',
						 	 'telefono': 'número de teléfono',
						 	 'Mail': 'mail',
						 	 'Web': 'web'}, inplace = True)

df_museos['número de teléfono'] = np.where(df_museos.cod_area.notnull() & df_museos['número de teléfono'].notnull(),
										   df_museos.cod_area.astype('Int64').astype(str) + ' ' + df_museos['número de teléfono'],
										   df_museos['número de teléfono'])

for column in df_museos.columns:
	if column not in nombres_columnas:
		del df_museos[column]

df_bibliotecas.rename(columns = {'Cod_Loc': 'cod_localidad',
						 	 	 'IdProvincia': 'id_provincia',
						 	 	 'IdDepartamento': 'id_departamento',
						 		 'Categoría': 'categoría',
						 	 	 'Provincia': 'provincia',
						 	 	 'Localidad': 'localidad',
						 	 	 'Nombre': 'nombre',
						 	 	 'Domicilio': 'domicilio',
							  	 'CP': 'código postal',
						 	 	 'Teléfono': 'número de teléfono',
						 	 	 'Mail': 'mail',
						 	 	 'Web': 'web'}, inplace = True)

df_bibliotecas['número de teléfono'] = np.where(df_bibliotecas.Cod_tel == 's/d',
										 		df_bibliotecas['número de teléfono'],
												df_bibliotecas.Cod_tel + ' ' + df_bibliotecas['número de teléfono'])

for column in df_bibliotecas.columns:
	if column not in nombres_columnas:
		del df_bibliotecas[column]


#UNIR DFs de TODAS LAS CATEGORIAS