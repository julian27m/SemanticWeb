import pandas as pd

"""
Proceso de Limpieza de Datos

"""

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('articulos_completos_pdf.csv')

#tamanio del dataframe
print(df.shape)

# Imprimimos el head del dataframe
print(df.head())

# Eliminar las filas duplicadas
df_sin_duplicados = df.drop_duplicates()

#Eliminar columnas repetidas
# Obtener los nombres de las columnas que terminan en '.1'
columnas_a_eliminar = [col for col in df.columns if col.endswith('.1')]

# Eliminar las columnas que terminan en '.1'
df = df.drop(columns=columnas_a_eliminar)

# Imprimimos los tipos de datos
print(df.dtypes)

## Arreglamos el tipo de datos

# Eliminar todas las filas con NaN en la columna 'year' antes de la conversión
df = df.dropna(subset=['year'])

# Convertir la columna 'year' a enteros
df['year'] = df['year'].astype(int)

# Eliminar los registros cuyo valor en 'year' sea menor a 1800 o mayor a 2025
df = df[(df['year'] >= 1800) & (df['year'] <= 2025)]

# Borramos la columna isInfluential porque no aporta mucho valor
df.drop('isInfluential', axis=1, inplace=True)

# Borramos la columna arxivId porque no aporta mucho valor
df.drop('arxivId', axis=1, inplace=True)

# Borramos la columna arxivId porque no aporta mucho valor
df.drop('intent', axis=1, inplace=True)

# Eliminar todas las filas con NaN en la columna 'pdf_path' (Registros sin PDF)
df = df.dropna(subset=['pdf_path'])

# Eliminar todas las filas con NaN en la columna 'pdf_path' (Registros sin PDF)
df = df.dropna(subset=['isOpenAccess'])

# Filtrar las filas donde pdf_path no comienza con 'DescargasPDFs'
df = df[df['pdf_path'].str.startswith('DescargasPDFs')]

# Eliminar cadenas vacías en la columna 'pdf_path'
df = df[df['pdf_path'].str.strip() != '']


#tamanio del dataframe
print(df.shape)


# Guardar el DataFrame de vuelta al archivo CSV si es necesario
df.to_csv('articulos_limpios.csv', index=False)

