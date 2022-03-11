#Pandas Nejercicios serie 2
#canal youtube john oritz ordoñez

import pandas as pd
import numpy as np

print("Ejercicio54: Seleccionar columnas de un objeto "
      "DataFrame usando notación de slicing.")


nombre = ['Oliva', 'Daniela', 'Juan', 'Germán', 'Edward', 'Alex', 'Julio',
          'Edgar', 'Angie', 'Irlesa']
puntaje = [11.5, 8, 15.5, np.nan, 8, 19, 13.5, np.nan, 8, 18]
intentos = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
califico = ['Sí', 'No', 'Sí', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'Sí']

indices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

jugadores = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos,
             'califico': califico}

df = pd.DataFrame(data=jugadores, index=indices)

print("df[['nombre', 'califico']]\n", df[['nombre', 'califico']])

print('df.axes\n', df.axes)
print("df.iloc[[1,4], [0,2]]\n", df.iloc[[1,4], [0,2]])
print("df.loc[['b','e'], ['nombre','intentos']]",
      df.loc[['b','e'], ['nombre','intentos']])
print('dimension :',df.ndim)
print('tamaño :',df.size)
print('forma :',df.shape)
print('memoria ocupada :',df.memory_usage())
print('comprobar vacio con df.empty :', df.empty)
print("df[df['puntaje'].isnull()]\n", df[df['puntaje'].isnull()])
print("df[df['puntaje'].between(14, 19)]\n", df[df['puntaje'].between(14, 19)])
print()
print(df.isna())
print()
print(df.notna())
print()
print("df.at['a', 'nombre']\n", df.at['a', 'nombre'])
print()
print("df.loc['a', 'nombre']\n", df.loc['a', 'nombre'])
print("df['puntaje'].sum()\n", df['puntaje'].sum())
print("df.iat[0, 0]\n", df.iat[0, 0])
#insertar columna
df.insert(1, 'pais', 0)
df['pais'] = ['colombia']*10
print(df)
#insertar fila
df.loc['k'] = ['Sebastian', 'colombia', 17.9, 2, 'si']
print(df)

datos = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1], 'Z': [2, 3, 5, 7, 11]}

indices = ['a', 'b', 'c', 'd', 'e']

df3 = pd.DataFrame(data=datos, index=indices)

for etiqueta, contenido in df3.items():
    print('nombre columna:', etiqueta)
    print('contenido:', contenido, sep='\n')
print("Iterar con la función itertuples un DataFrame"
      " por filas a modo de tuplas nombradas.")
for registro in df3.itertuples():
    print(registro)

df3.pop('Y')
print(df3)

print(df3.isin([10, 3]))

print(df3.mask(df3 > 3, 0))

print(df3.query('X < Z'))

df = df.drop('k')
print(df.sort_values(by=['nombre', 'puntaje'], ascending=[False, True]))

print("Reemplazar valores de una columna con la función map de un DataFrame.")

print(df['califico'].map({'Sí': True, 'No': False}))

df['nombre'] = df['nombre'].replace('Alex', 'Alexander')
print(df)

for indice, fila in df.iterrows():
    print(fila['nombre'], fila['califico'])

print("Ejercicio93 : Renombrar las columnas de un objeto DataFrame.")

datos = {'Columna1': [1, 2, 3, 4, 5], 'Columna2': [5, 4, 3, 2, 1],
         'Columna3': [2, 3, 5, 7, 11]}

indices = ['a', 'b', 'c', 'd', 'e']

df4 = pd.DataFrame(data=datos, index=indices)

renombrado_columnas = {'Columna1': 'X', 'Columna2': 'Y', 'Columna3': 'Z'}

df4 = df4.rename(columns=renombrado_columnas)
df4 = df4[['X','Z','Y']]
print(df4)

print(df.loc[df['califico']=='Sí'])

print("Ejercicio 99: Combinar dos DataFrame y dejar"
      " en cada columna el valor mínimo de la suma por columna.")

datos_1 = {'A': [1, 1], 'B': [5, 5]}
datos_2 = {'A': [3, 3], 'B': [2, 2]}

df_1 = pd.DataFrame(data=datos_1)
df_2 = pd.DataFrame(data=datos_2)

minimo_columna = lambda s1, s2: s1.sum() if s1.sum() < s2.sum() else s2.sum()

print("df_1\n", df_1)
print("df_2\n", df_2)
print("minimo_columna\n", minimo_columna)
print(df_1.combine(df_2, minimo_columna))


