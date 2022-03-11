#Pandas Nejercicios serie 1
#canal youtube john oritz ordoñez

import pandas as pd
import numpy as np

print('ejercicio 3: convertir un objeto series a una lista python')

datos = [2,3,5,7,11]

serie = pd.Series(datos)

print("serie:\n ", serie,'\n', type(serie))

lista = serie.tolist()
print("lista: ", lista, '\n',type(lista))

print('ejercicio 6: convertir un objeto diccionario a una lista python')

datos = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

print("datos: ", datos, type(datos))
serie = pd.Series(datos)

print("serie: ", serie, '\n', type(serie))

print('ejercicio 8: Cambiar el tipo de datos de un objeto Series.')

datos = pd.Series(['100','200','python'])
datos = pd.to_numeric(datos, errors='coerce')

print(datos, ', datos.hasnans :', datos.hasnans)

print('ejercicio 9: Obtener una columna de un objeto DataFrame como un objeto Series.')

datos = {'A': [1, 2, 3, 4, 5], 'B': [9, 8, 7, 6, 5], 'C': [2, 3, 5, 7, 11]}

df = pd.DataFrame(data=datos)

columns = df.iloc[:,1]

print("columna\n", columns)

fila = df.iloc[1,:]

print("fila\n", fila)

print("Ejercicio 11: Convertir un objeto Series con múltiples"
      " listas en un único objeto Series.")

datos = [['Colombia', 'Perú', 'Argentina'], ['Bolivia', 'Uruguay'], ['Chile']]

serie = pd.Series(datos)
serie = serie.apply(pd.Series).stack().reset_index(drop=True)

print(serie.sort_values()[::-1], ', serie.nbytes', serie.nbytes)

print("Ejercicio 25: Calcular el valor absoluto de los elementos de un objeto Series.")

datos = [-5, 3, 0, np.nan, 1]

serie = pd.Series(datos)
serie = pd.to_numeric(serie, errors='coerce')
serie = serie.dropna()
serie = serie.abs()

def cuadrado(x):
    return x*x

serie = serie.agg(cuadrado)

print(serie)

print("Ejercicio 30: Reemplazar por un valor arbitrario"
      " los valores de una serie que no satisfagan una condición.")

datos = list(range(1, 6))

serie = pd.Series(datos)

serie = serie.where(serie > 1, -1)

print(serie)

print("Ejercicio 31: Remover los valores que no cumplan una condición en un objeto Series.")

datos = list(range(1, 11))

serie = pd.Series(datos)

serie = serie.where(serie >= 5).dropna()

print(serie)

print("Ejercicio33: Generar representación JSON de un objeto Series.")

serie = pd.Series([1,2,3,4,5])

print(serie.to_json())

print("Ejercicio34: Obtener la representación de diccionario de un objeto Series")

capitales = ['Lima', 'Paris', 'Moscu', 'Berlin', 'Bogota']
paises = ['Peru', 'Francia', 'Rusia', 'Alemania', 'Colombia']

serie = pd.Series(capitales, index=paises)

print('serie.to_dict() :\n', serie.to_dict())
print('serie.to_frame() :\n', serie.to_frame())


print("Ejercicio 37: Aplicar una función sobre los elementos de un objeto Series")

serie = pd.Series([22, 18, 17], index=['Pitalito', 'Isnos', 'San Agustin'])

print(serie.apply(lambda x: x*x))

def adicionar_temperatura(x, delta):
    return x + delta

print(serie.apply(adicionar_temperatura, args=(7,)))

print("Ejercicio 38: Encontrar los elementos que están dentro de un rango.")

datos = [7, 2, 3, 5, 0, np.nan]

serie = pd.Series(datos)

print(serie.between(2, 5))

print("Ejercicio40: Remover los valores duplicados de un objeto Series con drop_duplicates.")

datos = ['Python', 'C#', 'Python', 'Java', 'Python', 'JavaScript']

serie = pd.Series(datos, name='lenguajes')

print(serie.drop_duplicates(keep='last'))
#nota: con keep='last' conserva el elemento con el último índice


print("Ejercicio44: Usar la función filter para extraer elementos por su índice.")

produccion = {'Enero': [1,2,3], 'Febrero': [4,5,6], 'Marzo': [7,8,9],
              'Abril': [10,11,12], 'Mayo': [13,14,15]}

serie = pd.DataFrame(produccion, index=['a', 'b', 'c'])

print(serie.filter(regex='^M'))
print(serie.filter(like='yo'))


print("columnas :\n", serie.columns)
print("filas :\n", serie.index)
print("tipo datos columnas :\n", serie.dtypes)

print("Ejercicio49: Mostrar un reporte con la información básica de un objeto DataFrame.")

lenguajes = ['Python', 'Java', 'C#', 'JavaScript', 'C++', 'PHP']
agnio_creacion = [1990, 1995, 2013, 1995, 1985, 1995]
interpretado = [True, False, False, True, False, True]
extension = ['.py', '.java', 'cs', 'js', 'cpp', 'php']
indices = ['a', 'b', 'c', 'd', 'e', 'f']

datos = {'lenguaje': lenguajes,
         'agnio_creacion': agnio_creacion,
         'interpretado': interpretado,
         'extension': extension}

df = pd.DataFrame(data=datos, index=indices)

print(df.info())

