import requests
import pandas as pd

# Función para procesar las entidades y actualizar el DataFrame
def process_entities(df):
    # Define la URL del servicio de DBpedia Spotlight en Docker
    spotlight_url = "http://localhost:2222/rest/annotate"

    # Lista para almacenar las entidades encontradas para cada columna
    columns_to_process = ['introduction', 'keywords', 'conclusions', 'abstract']

    # Lista para almacenar las entidades encontradas para cada fila
    entities_found_per_row = []

    # Iterar sobre las filas del DataFrame
    for index, row in df.iterrows():
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

        # Mostrar el progreso del proceso
        print(f"Procesando fila {index+1} de {len(df)}")

    # Agregar la lista de entidades encontradas como una nueva columna al DataFrame
    df['entities_found'] = entities_found_per_row

    # Guardar el DataFrame actualizado en un nuevo archivo CSV
    df.to_csv('archivo_entidades.csv', index=False)

try:
    # Leer el archivo CSV
    df = pd.read_csv('metadatos.csv')

    # Procesar las entidades y actualizar el DataFrame
    process_entities(df)

    print("Proceso completado exitosamente.")
except Exception as e:
    # Capturar cualquier excepción que ocurra y mostrar un mensaje de error
    print("Se produjo un error durante el procesamiento:", str(e))
    print("Guardando el DataFrame actual antes de salir...")

    # Guardar el DataFrame actualizado en un nuevo archivo CSV antes de salir
    if 'df' in locals():
        df.to_csv('archivo_entidades.csv', index=False)

    # Salir del programa con un código de error
    exit(1)
