import ast
import pandas as pd
from rdflib import Graph, Namespace, RDF, RDFS, XSD, Literal
import json
import urllib
import owlrl

# Definir un único espacio de nombres para todas las clases y propiedades
ns = Namespace("http://example.org/ontology#")

# Crear un grafo RDF
g = Graph()

# Definir las clases en el espacio de nombres
g.add((ns.Paper, RDF.type, RDFS.Class))
g.add((ns.Persona, RDF.type, RDFS.Class))
g.add((ns.Anotacion, RDF.type, RDFS.Class))

# Definir las propiedades en el espacio de nombres
g.add((ns.autor, RDF.type, RDF.Property))
g.add((ns.references, RDF.type, RDF.Property))
g.add((ns.authorId, RDF.type, RDF.Property))
g.add((ns.semanticUrl, RDF.type, RDF.Property))
g.add((ns.conceptAnotation, RDF.type, RDF.Property))
g.add((ns.tieneAbstract, RDF.type, RDF.Property))
g.add((ns.tieneIntroduccion, RDF.type, RDF.Property))
g.add((ns.tieneKeyWords, RDF.type, RDF.Property))
g.add((ns.tieneCitationVelocity, RDF.type, RDF.Property))
g.add((ns.tieneDOI, RDF.type, RDF.Property))
g.add((ns.tienePaperId, RDF.type, RDF.Property))
g.add((ns.tieneVenue, RDF.type, RDF.Property))
g.add((ns.tieneAñoPublicacion, RDF.type, RDF.Property))
g.add((ns.tieneInfluentialCitationCount, RDF.type, RDF.Property))
g.add((ns.tieneIsOpenAccess, RDF.type, RDF.Property))
g.add((ns.tieneIsPublisherLicensed, RDF.type, RDF.Property))

# Leer el archivo CSV
df = pd.read_csv('archivo_entidades.csv')

# Función para convertir la cadena en una lista de diccionarios y extraer el título de cada referencia
def extract_reference_titles(references_str):
    references_list = json.loads(references_str)  # Convertir la cadena en una lista de diccionarios
    titles = [ref['title'] for ref in references_list]  # Extraer los títulos de los diccionarios
    return titles

# Aplicar la función a cada fila de la columna 'references' y crear una nueva columna 'reference_titles'
df['reference_titles'] = df['references'].apply(extract_reference_titles)

# Función para convertir la cadena en una lista de diccionarios y extraer el nombre, el authorId y la URL de cada autor en la lista
def extract_author_info(authors_str):
    authors_list = json.loads(authors_str)  # Convertir la cadena en una lista de diccionarios
    author_info = [(author['name'], author['authorId'], author['url']) for author in authors_list]
    return author_info

# Aplicar la función a cada fila de la columna 'authors' y crear una nueva columna 'author_info'
df['author_info'] = df['authors'].apply(extract_author_info)

count = 0
# Iterar sobre cada fila del DataFrame
for index, row in df.iterrows():
    count += 1
    print(count)
    # Crear un URI para el paper basado en su título
    cleaned_title = urllib.parse.quote(row['title'].replace('"', ''))  # Remover las comillas dobles y codificar la cadena
    paper_uri = ns[cleaned_title.replace(" ", "_")]

    # Restricciones de dominio y rango
    g.add((ns.citationVelocity, RDFS.domain, ns.Paper))
    g.add((ns.citationVelocity, RDFS.range, XSD.integer))

    # Continuar con la definición de restricciones para las otras propiedades y clases

    # Para cada autor en la lista de autores de esta fila
    for author_name, author_id, url in row['author_info']:
        # Crear un URI para la persona basado en su nombre
        persona_uri = ns[author_name.replace(" ", "_")]

        # Agregar tripletas al grafo RDF
        g.add((paper_uri, RDF.type, ns.Paper))
        g.add((persona_uri, RDF.type, ns.Persona))
        g.add((paper_uri, ns.autor, persona_uri))
        
        # Agregar la tripleta para el ID de la persona como DataProperty
        g.add((persona_uri, ns.authorId, Literal(author_id)))
        g.add((ns.authorId, RDF.type, RDF.Property))
        g.add((ns.authorId, RDFS.domain, ns.Persona))
        g.add((ns.authorId, RDFS.range, XSD.string))
        
        # Agregar la tripleta para la URL semántica de la persona como DataProperty
        g.add((persona_uri, ns.semanticUrl, Literal(url)))
        g.add((ns.semanticUrl, RDF.type, RDF.Property))
        g.add((ns.semanticUrl, RDFS.domain, ns.Persona))
        g.add((ns.semanticUrl, RDFS.range, XSD.string))
    
    # Establecer relaciones entre el papel actual y cada título de referencia
    for ref_title in row['reference_titles']:
        cleaned_ref_title = urllib.parse.quote(ref_title.replace('"', ''))
        ref_paper_uri = ns[cleaned_ref_title.replace(" ", "_")]
        
        g.add((paper_uri, ns.references, ref_paper_uri))
    
    # Agregar las tripletas para las columnas restantes
    
    # Agregar las tripletas para los data properties
    paper_abstract = Literal(row['abstract'])
    g.add((paper_uri, ns.tieneAbstract, paper_abstract))
    
    paper_introduccion = Literal(row['introduction'])
    g.add((paper_uri, ns.tieneIntroduccion, paper_introduccion))
    
    paper_keywords = Literal(row['keywords'])
    g.add((paper_uri, ns.tieneKeyWords, paper_keywords))
    
    paper_citation_velocity = Literal(row['citationVelocity'])
    g.add((paper_uri, ns.tieneCitationVelocity, paper_citation_velocity))
    
    paper_doi = Literal(row['doi'])
    g.add((paper_uri, ns.tieneDOI, paper_doi))
    
    paper_paper_id = Literal(row['paperId'])
    g.add((paper_uri, ns.tienePaperId, paper_paper_id))
    
    paper_venue = Literal(row['venue'])
    g.add((paper_uri, ns.tieneVenue, paper_venue))
    
    paper_year = Literal(row['year'])
    g.add((paper_uri, ns.tieneAñoPublicacion, paper_year))
    
    paper_influential_citation_count = Literal(row['influentialCitationCount'])
    g.add((paper_uri, ns.tieneInfluentialCitationCount, paper_influential_citation_count))
    
    paper_is_open_access = Literal(row['isOpenAccess'])
    g.add((paper_uri, ns.tieneIsOpenAccess, paper_is_open_access))
    
    paper_is_publisher_licensed = Literal(row['isPublisherLicensed'])
    g.add((paper_uri, ns.tieneIsPublisherLicensed, paper_is_publisher_licensed))

    # Agregar las tripletas para las entidades encontradas con ConceptAnotation
    entities = ast.literal_eval(row['entities_found'])
    for entity in entities:
        entity_uri = ns[entity.replace(" ", "_")]
        g.add((entity_uri, RDF.type, ns.Anotacion))
        g.add((paper_uri, ns.conceptAnotation, entity_uri))

# Serializar y guardar el grafo RDF en un archivo en formato Turtle
g.serialize(destination='ontologia.rdf', format='n3')

print("Listo sin inferir")

# Inferir tuplas
owl_reasoner = owlrl.CombinedClosure.RDFS_OWLRL_Semantics(g, False, False, False)
owl_reasoner.closure()
owl_reasoner.flush_stored_triples()

with open("inference.ttl", "w", encoding="utf-8") as f:
    f.write(g.serialize(format='ttl'))

