import json
import csv

##Función para convertir json en csv

# Leer el archivo JSON
with open('articulos_combinados.json', 'r') as json_file:
    data = json.load(json_file)

# Definir las columnas que deseas extraer
columnas = ['abstract', 'arxivId', 'citationVelocity', 'citations', 'authors', 'doi', 'intent', 'isInfluential',
            'paperId', 'title', 'url', 'venue', 'year', 'corpusId', 'doi', 'fieldsOfStudy', 'influentialCitationCount',
            'isOpenAccess', 'isPublisherLicensed', 'is_open_access', 'is_publisher_licensed', 'numCitedBy', 'numCiting',
            'paperId', 'references', 's2FieldsOfStudy', 'title', 'topics', 'url', 'venue', 'year']

# Crear un archivo CSV y escribir las columnas
with open('articulos_completos.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=columnas)
    writer.writeheader()

    # Iterar sobre los datos y escribir en el archivo CSV
    for item in data:
        writer.writerow({
            'abstract': item.get('abstract', ''),
            'arxivId': item.get('arxivId', ''),
            'citationVelocity': item.get('citationVelocity', ''),
            'citations': json.dumps(item.get('citations', [])),
            'authors': json.dumps(item.get('authors', [])),
            'doi': item.get('doi', ''),
            'intent': json.dumps(item.get('intent', [])),
            'isInfluential': item.get('isInfluential', ''),
            'paperId': item.get('paperId', ''),
            'title': item.get('title', ''),
            'url': item.get('url', ''),
            'venue': item.get('venue', ''),
            'year': item.get('year', ''),
            'corpusId': item.get('corpusId', ''),
            'doi': item.get('doi', ''),
            'fieldsOfStudy': json.dumps(item.get('fieldsOfStudy', [])),
            'influentialCitationCount': item.get('influentialCitationCount', ''),
            'isOpenAccess': item.get('isOpenAccess', ''),
            'isPublisherLicensed': item.get('isPublisherLicensed', ''),
            'is_open_access': item.get('is_open_access', ''),
            'is_publisher_licensed': item.get('is_publisher_licensed', ''),
            'numCitedBy': item.get('numCitedBy', ''),
            'numCiting': item.get('numCiting', ''),
            'paperId': item.get('paperId', ''),
            'references': json.dumps(item.get('references', [])),
            's2FieldsOfStudy': json.dumps(item.get('s2FieldsOfStudy', [])),
            'title': item.get('title', ''),
            'topics': json.dumps(item.get('topics', [])),
            'url': item.get('url', ''),
            'venue': item.get('venue', ''),
            'year': item.get('year', '')
        })