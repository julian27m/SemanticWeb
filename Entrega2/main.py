import os
import json
import requests
import xml.etree.ElementTree as ET

grobid_url = "http://localhost:8070/api/processFulltextDocument"
pdfs_folder = 'Entrega1/PDFs'

def extract_info_from_pdf(pdf_path):
    try:
        print(f"Procesando archivo: {pdf_path}")
        with open(pdf_path, 'rb') as pdf_file:
            files = {'input': pdf_file}
            response = requests.post(grobid_url, files=files)

        if response.status_code == 200:
            print(f"Respuesta recibida para el archivo: {pdf_path}")
            root = ET.fromstring(response.content)
            keywords = [term.text for term in root.findall('.//{http://www.tei-c.org/ns/1.0}term')]
            abstract = '\n'.join(p.text.strip() for p in root.findall('.//{http://www.tei-c.org/ns/1.0}abstract//{http://www.tei-c.org/ns/1.0}p'))
            introduction = '\n'.join(p.text.strip() for p in root.findall('.//{http://www.tei-c.org/ns/1.0}div[@type="introduction"]//{http://www.tei-c.org/ns/1.0}p'))
            conclusions = '\n'.join(p.text.strip() for p in root.findall('.//{http://www.tei-c.org/ns/1.0}div[@type="conclusions"]//{http://www.tei-c.org/ns/1.0}p'))
            print(f"Información extraída del archivo {pdf_path}:")
            print(f"Keywords: {keywords}")
            print(f"Abstract: {abstract}")
            print(f"Introducción: {introduction}")
            print(f"Conclusiones: {conclusions}")
            return {
                'keywords': keywords,
                'abstract': abstract,
                'introduction': introduction,
                'conclusions': conclusions
            }
        else:
            print(f"Error al procesar {pdf_path}: Código de estado HTTP {response.status_code}")
            return {
                'keywords': [],
                'abstract': '',
                'introduction': '',
                'conclusions': ''
            }
    except Exception as e:
        print(f"Error al procesar {pdf_path}: {e}")
        return {
            'keywords': [],
            'abstract': '',
            'introduction': '',
            'conclusions': ''
        }


def main():
    pdf_info_list = []

    for filename in os.listdir(pdfs_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdfs_folder, filename)
            try:
                pdf_info = extract_info_from_pdf(pdf_path)
                pdf_info_list.append({filename: pdf_info})
            except Exception as e:
                print(f"Error al procesar {pdf_path}: {e}")

    with open('pdf_info.json', 'w') as json_file:
        json.dump(pdf_info_list, json_file, indent=4)

if __name__ == "__main__":
    main()
