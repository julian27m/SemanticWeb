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
            #print(response.content.decode('utf-8'))  # Imprimir el XML devuelto por GROBID

        if response.status_code == 200:
            print(f"Respuesta recibida para el archivo: {pdf_path}")
            root = ET.fromstring(response.content)
            
            # Extraer abstract
            abstract = '\n'.join(p.text.strip() for p in root.findall('.//{http://www.tei-c.org/ns/1.0}abstract//{http://www.tei-c.org/ns/1.0}p'))
            
            # Buscar introduction usando palabras clave
            introduction = find_section_by_keywords(root, "introduction")
            
            # Buscar keywords en las etiquetas <keywords>
            keywords = find_keywords(root)
            
            # Buscar conclusiones usando palabras clave
            conclusions = find_section_by_keywords(root, "conclusions")

            print(f"Información extraída del archivo {pdf_path}:")
            print(f"Abstract: {abstract}")
            print(f"Keywords: {keywords}")
            print(f"Introduction: {introduction}")
            print(f"Conclusions: {conclusions}")
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
        'conclusions': ['conclusions', 'concluding', 'summary', 'summary of findings'"conclusions", "conclusion", "concluding remarks", "remarkable conclusions"],
        'keywords': ['keywords', 'key words', 'index terms', 'terms']
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
    pdf_info_list = []
    abstract_count = 0
    keywords_count = 0
    introduction_count = 0
    conclusions_count = 0

    for filename in os.listdir(pdfs_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdfs_folder, filename)
            try:
                pdf_info = extract_info_from_pdf(pdf_path)
                pdf_info_list.append({filename: pdf_info})
                if pdf_info['abstract']:
                    abstract_count += 1
                if pdf_info['keywords']:
                    keywords_count += 1
                if pdf_info['introduction']:
                    introduction_count += 1
                if pdf_info['conclusions']:
                    conclusions_count += 1
            except Exception as e:
                print(f"Error al procesar {pdf_path}: {e}")

    print(f"\nResumen de análisis:")
    print(f"{len(pdf_info_list)} PDFs analizados:")
    print(f"{abstract_count} con abstract")
    print(f"{keywords_count} con keywords")
    print(f"{introduction_count} con introduction")
    print(f"{conclusions_count} con conclusions")

    with open('pdf_info.json', 'w') as json_file:
        json.dump(pdf_info_list, json_file, indent=4)

if __name__ == "__main__":
    main()