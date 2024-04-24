import requests
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('Entrega2/CSVs/primeras_cinco_filas.csv')

# URL del servicio de DBpedia Spotlight en Docker
spotlight_url = "http://localhost:2222/rest/annotate"

# Lista para almacenar las entidades encontradas para cada columna
columns_to_process = ['introduction', 'keywords', 'conclusions', 'abstract']

# Lista para almacenar las entidades encontradas para cada fila
entities_found_per_row = []

# Iterar sobre las filas del DataFrame
for index, row in df.iterrows():
    # Mostrar un mensaje en la consola con el número de la fila actual
    print(f"Procesando fila {index + 1}/{len(df)}")

    # Lista para almacenar las entidades encontradas para esta fila
    entities_found_row = []

    # Iterar sobre las columnas a procesar
    for column in columns_to_process:
        # Obtener el texto de la columna actual
        text = row[column]

        # Setear los parámetros para la solicitud
        params = {
            "text": text,
            "confidence": 0.35
        }

        # Enviar la solicitud al contenedor de DBpedia Spotlight en Docker
        response = requests.post(spotlight_url, data=params, headers={"Accept": "application/json"})

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Parsear la respuesta JSON
            data = response.json()
            # Verificar si la clave 'Resources' está presente en la respuesta
            if 'Resources' in data:
                # Extraer las anotaciones de la respuesta
                annotations = data["Resources"]
                # Crear una lista de las entidades encontradas para esta fila
                entities = [annotation['@URI'] for annotation in annotations]
                # Agregar las entidades encontradas para esta fila a la lista
                entities_found_row.extend(entities)

    # Agregar la lista de entidades encontradas para esta fila a la lista general
    entities_found_per_row.append(entities_found_row)

# Agregar la lista de entidades encontradas como una nueva columna al DataFrame
df['entities_found'] = entities_found_per_row

# Guardar el DataFrame actualizado en un nuevo archivo CSV
df.to_csv('anotaciones.csv', index=False)

print(df.columns)
