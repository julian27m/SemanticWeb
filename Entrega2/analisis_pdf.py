import os
import json
import pandas as pd
import requests
import xml.etree.ElementTree as ET

grobid_url = "http://localhost:8070/api/processFulltextDocument"

def extract_info_from_pdf(pdf_path):
    try:
        print(f"Procesando archivo: {pdf_path}")
        with open(pdf_path, 'rb') as pdf_file:
            files = {'input': pdf_file}
            response = requests.post(grobid_url, files=files)

        if response.status_code == 200:
            print(f"Respuesta recibida para el archivo: {pdf_path}")
            root = ET.fromstring(response.content)
            
            # Buscar introduction usando palabras clave
            introduction = find_section_by_keywords(root, "introduction")
            
            # Buscar keywords en las etiquetas <keywords>
            keywords = find_keywords(root)
            
            # Buscar conclusiones usando palabras clave
            conclusions = find_section_by_keywords(root, "conclusions")

            print(f"Información extraída del archivo {pdf_path}:")
            #print(f"Introduction: {introduction}")
            #print(f"Keywords: {keywords}")
            #print(f"Conclusions: {conclusions}")
            return {
                'keywords': keywords,
                'introduction': introduction,
                'conclusions': conclusions
            }
        else:
            print(f"Error al procesar {pdf_path}: Código de estado HTTP {response.status_code}")
            return {
                'keywords': '',
                'introduction': '',
                'conclusions': ''
            }
    except Exception as e:
        print(f"Error al procesar {pdf_path}: {e}")
        return {
            'keywords': '',
            'introduction': '',
            'conclusions': ''
        }

def find_section_by_keywords(root, section_name):
    """
    Busca la sección específica en el XML devuelto por GROBID utilizando palabras clave
    """
    section_text = ''
    section_found = False
    section_name = section_name.lower()

    # Palabras clave relacionadas a la sección
    section_keywords = {
        'introduction': ['introduction', 'background', 'context'],
        'conclusions': ['conclusions', 'concluding', 'summary', 'summary of findings'"conclusions", "conclusion", "concluding remarks", "remarkable conclusions"]
    }

    # Buscar sección por palabras clave relacionadas
    for elem in root.iter():
        if elem.text and any(keyword in elem.text.lower() for keyword in section_keywords[section_name]):
            section_found = True
        elif section_found and elem.tag.endswith('p'):
            section_text += elem.text.strip() + '\n'
        elif section_found and elem.text and not any(keyword in elem.text.lower() for keyword in section_keywords[section_name]):
            break

    return section_text.strip()

def find_keywords(root):
    """
    Busca y extrae las palabras clave del XML devuelto por GROBID
    """
    keywords_text = ''
    keywords_elements = root.findall('.//{http://www.tei-c.org/ns/1.0}keywords')
    for keywords_element in keywords_elements:
        keywords_text += ''.join(term.text.strip() + ', ' for term in keywords_element.findall('.//{http://www.tei-c.org/ns/1.0}term'))
    return keywords_text.strip(', ')

def main():
    # Leer el archivo CSV
    csv_path = 'articulos_limpios.csv'
    df = pd.read_csv(csv_path)

    # Contador de progreso
    total_rows = len(df)
    processed_rows = 0

    # Recorrer el DataFrame
    for index, row in df.iterrows():
        pdf_path = row['pdf_path']  # Obtener la ruta del PDF desde la columna 'pdf_path'
        try:
            pdf_info = extract_info_from_pdf(pdf_path)
            # Asignar los valores a las nuevas columnas
            df.at[index, 'introduction'] = pdf_info['introduction']
            df.at[index, 'keywords'] = pdf_info['keywords']
            df.at[index, 'conclusions'] = pdf_info['conclusions']
            processed_rows += 1
            print(f"Procesando fila {processed_rows} de {total_rows}")
        except Exception as e:
            print(f"Error al procesar {pdf_path}: {e}")

    # Guardar el DataFrame actualizado en un nuevo CSV
    df.to_csv('metadatos.csv', index=False)

if __name__ == "__main__":
    main()
