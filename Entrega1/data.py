# %%
# Imports
import requests
from requests.exceptions import RequestException, SSLError
import json
import csv
import pandas as pd
import os
import time
#import sys

# %%
# Define the API endpoint URL
url = 'https://api.semanticscholar.org/graph/v1/paper/search'

# Directly define the API key (Reminder: Securely handle API keys in production environments)
api_key = 'zRjnP89HI697jM02sRqJjX9LgSItJSta3PDJUVN2'  

ruta_archivos_pdf = []


# %%
# Sacar los titles de los articulos desde el json

# Abrir el archivo JSON
with open('dict_split_1.json') as f:
    data = json.load(f)

# Lista para almacenar los títulos de los artículos
titulos = []

# Iterar sobre cada entrada en el JSON
for key, value in data.items():
    # Obtener el título del artículo de cada entrada y agregarlo a la lista de títulos
    titulo = value.get('title')
    if titulo:
        titulos.append(titulo)

# Imprimir los títulos de los artículos
count = 0
for titulo in titulos:
    count += 1
    #print(titulo)

print("Numero de articulos: "+ str(count))

# %%
## Sacar Ids de los articulos

# Arreglo donde se almacenarán los ids de los artículos
arregloIds = [] 

# More specific query parameter
for i in range(1000):
    query_params = {'query': titulos[i],
                    'limit': 1}
    paperDataQueryParams = {'fields': 'title'}

    # Define headers with API key
    headers = {'x-api-key': api_key}

    # Send the API request
    response = requests.get(url, query_params, headers=headers)

    # Check response status
    if response.status_code == 200:
        try:
            response_data = response.json()
            # Process and print the response data as needed
            arregloIds.append(response_data['data'][0]['paperId'])
        except KeyError:
            print(f"Key 'data' not found in response JSON: {response.json()}")
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
    # Agregar un retraso de un segundo entre las consultas
    time.sleep(1)



# %%
print(len(arregloIds))

# %%
def descargar_articulo(id):

  # URL de la API de Semantic Scholar
  url = f"https://api.semanticscholar.org/v1/paper/{id}"
 
  # Enviar la solicitud GET
  try:
    response = requests.get(url,headers=headers)
   
    response.raise_for_status()  # Raise an exception for non-200 status codes
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    return None

  # Devolver el contenido del artículo en formato PDF
 # print(response.content)
  return response.content



# %%
## Descargar los articulos principales (formato JSON)

contadorJSONs= 0
for i in range(len(arregloIds)):

  id = arregloIds[i]

  articulo_pdf = descargar_articulo(id)

  if articulo_pdf:
    # Guardar el artículo en un archivo
    with open("articulo"+str(i)+".json", "wb") as f:
      f.write(articulo_pdf)
      

    print("Artículo descargado correctamente.")
    contadorJSONs += 1
    print("Se han descargado JSONs: " + str(contadorJSONs) )

  else:
    print(f"No se pudo descargar el artículo con el ID '{id}'.")
  time.sleep(1)


# %%
## Obtener los ids de los articulos de referencia (Max 5)

idsReferencias = []
ultimoArticulo = 0

# Iterar sobre los archivos JSON descargados
for i in range(contadorJSONs):
    # Nombre del archivo JSON
    nombre_archivo = "articulo" + str(i) + ".json"

    # Leer el archivo JSON
    with open(nombre_archivo, "r") as f:
        data = json.load(f)

        # Obtener el título del artículo y agregarlo a la lista de títulos
        referencias = data.get('references', 'Título no encontrado')
        
        contadorreferencias = 0
        for j in range(len(referencias)):
           idPaper = referencias[j]['paperId']
           idsReferencias.append(idPaper)
           contadorreferencias += 1
           if contadorreferencias == 5:
               break
    ultimoArticulo = i

# Imprimir los títulos de los artículos
print("Títulos de los artículos:")
print(idsReferencias)

# %%
len(idsReferencias)

# %%
## Descargar los artículos de referencia

cReferencias= 0
c = contadorJSONs
for i in range(len(idsReferencias)):

  id = idsReferencias[i]
 
  articulo_pdf = descargar_articulo(id)

  if articulo_pdf:
    # Guardar el artículo en un archivo
    with open("articulo"+str(ultimoArticulo)+".json", "wb") as f:
      f.write(articulo_pdf)
      

    print("Artículo descargado correctamente.")
    c += 1
    print("Se han descargado JSONs: " + str(c) )
    cReferencias += 1
    ultimoArticulo += 1

  else:
    print(f"No se pudo descargar el artículo con el ID '{id}'.")
  time.sleep(1)


# %%
## Descargar PDF

ruta_archivos_pdf = []

def descargar_articulo_pdf(id):

    # URL de la API de Semantic Scholar
    url = "https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,isOpenAccess,openAccessPdf"
    
    # Cuerpo de la solicitud JSON
    data = {
        "ids": [id]
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
    except RequestException as e:
        print(f"Error en la solicitud HTTP: {e}")
        ruta_archivos_pdf.append("No tiene")
        return None

    # Convertir la respuesta a JSON
    articles_data = response.json()

    # Iterar sobre cada artículo en la respuesta
    for article_data in articles_data:
        # Obtener los datos del artículo
        article_title = article_data.get('title', None)
        open_access_pdf = article_data.get('openAccessPdf', None)

        if article_title and open_access_pdf:
            article_pdf_access = open_access_pdf.get('url', None)
            if article_pdf_access:
                try:
                    print(f"Descargando PDF para el artículo '{article_title}'...")
                    # Descargar el PDF
                    pdf = requests.get(article_pdf_access)
                    pdf.raise_for_status()

                    # Guardar el PDF
                    folder_path = os.path.join(os.getcwd(), "DescargasPDFs")
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    
                    pdf_file_path = os.path.join(folder_path, f"{article_title}.pdf")

                    with open(pdf_file_path, "wb") as f:
                        f.write(pdf.content)

                    print(f"El archivo PDF para '{article_title}' se descargó correctamente.")
                    
                    # Agregar la ruta de la carpeta donde se guardó el PDF al JSON
                    pdf_file_relative_path = os.path.join("DescargasPDFs", f"{article_title}.pdf")
                    ruta_archivos_pdf.append(pdf_file_relative_path)
                except RequestException as e:
                    print(f"No se pudo descargar el PDF para '{article_title}': {e}")
                    ruta_archivos_pdf.append("No tiene")
            else:
                print(f"No se encontró el enlace de acceso al PDF para el artículo '{article_title}'.")
                ruta_archivos_pdf.append("No tiene")
        else:
            print(f"No se encontró el título o el enlace de acceso al PDF para el artículo '{article_title}'.")
            ruta_archivos_pdf.append("No tiene")

    return 


# %%
## Unificación de todos los json en uno solo

lista_combinada = []

for i in range(ultimoArticulo):
    print(str(i))
    # Lee el contenido de los archivos JSON
    articuloNameFile = "articulo"+ str(i) + ".json" 
    with open(articuloNameFile, 'r') as file1:
        data = json.load(file1)
        lista_combinada.append(data)



# Crea una lista que contenga ambos diccionarios


# Escribe la lista combinada en un nuevo archivo JSON
with open('articulos_combinados.json', 'w') as outfile:
    json.dump(lista_combinada, outfile, indent=4)


# %%
print(len(ruta_archivos_pdf))

# %%
## Llamado de funcion para descargar todos los PDFs

for i in range(len(arregloIds)):
    id = arregloIds[i]
    articulo_pdf = descargar_articulo_pdf(id)
time.sleep(1)

for i in range(len(idsReferencias)):
    id = idsReferencias[i]
    articulo_pdf = descargar_articulo_pdf(id)
time.sleep(1)

    

