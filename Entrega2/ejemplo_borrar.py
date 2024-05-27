import ast
import pandas as pd
from rdflib import Graph, Namespace, RDF, RDFS, XSD, Literal
import json
import urllib
import owlrl


# Definir los prefijos de los espacios de nombres RDF/OWL
paper = Namespace("http://example.org/paper#")
persona = Namespace("http://example.org/persona#")
url_namespace = Namespace("http://example.org/semanticUrl#")
id_namespace = Namespace("http://example.org/id#")
abstract = Namespace("http://example.org/abstract#")
introduccion = Namespace("http://example.org/introduccion#")
keywords = Namespace("http://example.org/keywords#")
citation = Namespace("http://example.org/citation#")
doi = Namespace("http://example.org/doi#")
paperId = Namespace("http://example.org/paperId#")
venue = Namespace("http://example.org/venue#")
url = Namespace("http://example.org/url#")
year = Namespace("http://example.org/year#")
influentialCitationCount = Namespace("http://example.org/influentialCitationCount#")
isOpenAccess = Namespace("http://example.org/isOpenAccess#")
isPublisherLicensed = Namespace("http://example.org/isPublisherLicensed#")
conceptAnotation = Namespace("http://example.org/conceptAnotation#")

# Crear un grafo RDF
g = Graph()

# Leer el archivo CSV
df = pd.read_csv('C:\\Users\\juane\\OneDrive\\Documentos\\Universidad\\Semantic\\SemanticWeb\\Entrega2\\archivo_entidades.csv')


# Función para convertir la cadena en una lista de diccionarios y extraer el título de cada referencia
def extract_reference_titles(references_str):
    references_list = json.loads(references_str)  # Convertir la cadena en una lista de diccionarios
    titles = [ref['title'] for ref in references_list]  # Extraer los títulos de los diccionarios
    return titles

# Aplicar la función a cada fila de la columna 'references' y crear una nueva columna 'reference_titles'
df['reference_titles'] = df['references'].apply(extract_reference_titles)

# Función para convertir la cadena en una lista de diccionarios y extraer el nombre, el authorId y la URL de cada autor en la lista
def extract_author_info(authors_str):
    authors_list = ast.literal_eval(authors_str)  # Convertir la cadena en una lista de diccionarios
    author_info = [(author['name'], author['authorId'], author['url']) for author in authors_list]
    return author_info

# Aplicar la función a cada fila de la columna 'authors' y crear una nueva columna 'author_info'
df['author_info'] = df['authors'].apply(extract_author_info)

# Iterar sobre cada fila del DataFrame
for index, row in df.iterrows():
    # Crear un URI para el paper basado en su título
    cleaned_title = urllib.parse.quote(row['title'].replace('"', ''))  # Remover las comillas dobles y codificar la cadena
    paper_uri = paper[cleaned_title.replace(" ", "_")]

    # Restricciones de dominio y rango
    g.add((paper.citationVelocity, RDFS.domain, paper.Paper))
    g.add((paper.citationVelocity, RDFS.range, XSD.integer))

    g.add((paper.doi, RDFS.domain, paper.Paper))
    g.add((paper.doi, RDFS.range, XSD.string))

    g.add((paper.paperId, RDFS.domain, paper.Paper))
    g.add((paper.paperId, RDFS.range, XSD.string))

    g.add((paper.venue, RDFS.domain, paper.Paper))
    g.add((paper.venue, RDFS.range, XSD.string))

    g.add((paper.year, RDFS.domain, paper.Paper))
    g.add((paper.year, RDFS.range, XSD.integer))

    g.add((paper.influentialCitationCount, RDFS.domain, paper.Paper))
    g.add((paper.influentialCitationCount, RDFS.range, XSD.integer))

    g.add((paper.isOpenAccess, RDFS.domain, paper.Paper))
    g.add((paper.isOpenAccess, RDFS.range, XSD.boolean))

    g.add((paper.isPublisherLicensed, RDFS.domain, paper.Paper))
    g.add((paper.isPublisherLicensed, RDFS.range, XSD.boolean))

    g.add((paper.semanticUrl, RDFS.domain, paper.Paper))
    g.add((paper.semanticUrl, RDFS.range, XSD.string))

    g.add((paper.yearPublicacion, RDFS.domain, paper.Paper))
    g.add((paper.yearPublicacion, RDFS.range, XSD.integer))

    # Para cada autor en la lista de autores de esta fila
    for author_name, author_id, url in row['author_info']:
        # Crear un URI para la persona basado en su nombre
        persona_uri = persona[author_name.replace(" ", "_")]

        # Agregar tripletas al grafo RDF
        g.add((paper_uri, RDF.type, paper.Paper))
        g.add((persona_uri, RDF.type, persona.Persona))
        g.add((paper_uri, paper.autor, persona_uri))
        
        # Agregar la tripleta para el ID de la persona como DataProperty
        g.add((persona_uri, id_namespace['authorId'], Literal(author_id)))
        g.add((id_namespace['authorId'], RDF.type, RDF.Property))
        g.add((id_namespace['authorId'], RDFS.domain, persona.Persona))
        g.add((id_namespace['authorId'], RDFS.range, XSD.string))
        
        # Agregar la tripleta para la URL semántica de la persona como DataProperty
        g.add((persona_uri, url_namespace['semanticUrl'], Literal(url)))
        g.add((url_namespace['semanticUrl'], RDF.type, RDF.Property))
        g.add((url_namespace['semanticUrl'], RDFS.domain, persona.Persona))
        g.add((url_namespace['semanticUrl'], RDFS.range, XSD.string))
    
    # Establecer relaciones entre el papel actual y cada título de referencia
    for ref_title in row['reference_titles']:
        cleaned_ref_title = urllib.parse.quote(ref_title.replace('"', ''))
        ref_paper_uri = paper[cleaned_ref_title.replace(" ", "_")]
        
        g.add((paper_uri, paper.references, ref_paper_uri))
    
    # Agregar la tripleta Paper-tieneAbstract-Abstract
    paper_abstract = Literal(row['abstract'])
    g.add((paper_uri, abstract.tieneAbstract, paper_abstract))
    
    # Agregar la tripleta Paper-tieneIntroduccion-Introduccion
    paper_introduccion = Literal(row['introduction'])
    g.add((paper_uri, introduccion.tieneIntroduccion, paper_introduccion))
    
    # Agregar la tripleta Paper-tieneKeyWords-KeyWords
    paper_keywords = Literal(row['keywords'])
    g.add((paper_uri, keywords.tieneKeyWords, paper_keywords))
    
    # Agregar la tripleta Paper-tieneCitationVelocity-CitationVelocity
    paper_citation_velocity = Literal(row['citationVelocity'])
    g.add((paper_uri, citation.tieneCitationVelocity, paper_citation_velocity))
    
    # Agregar la tripleta Paper-tieneDOI-DOI
    paper_doi = Literal(row['doi'])
    g.add((paper_uri, doi.tieneDOI, paper_doi))
    
    # Agregar la tripleta Paper-tienePaperId-PaperId
    paper_paper_id = Literal(row['paperId'])
    g.add((paper_uri, paperId.tienePaperId, paper_paper_id))
    
    # Agregar la tripleta Paper-tieneVenue-Venue
    paper_venue = Literal(row['venue'])
    g.add((paper_uri, venue.tieneVenue, paper_venue))
    
    # Agregar la tripleta Paper-tieneAñoPublicacion-AñoPublicacion
    paper_year = Literal(row['year'])
    g.add((paper_uri, year.tieneAñoPublicacion, paper_year))
    
    # Agregar la tripleta Paper-tieneInfluentialCitationCount-InfluentialCitationCount
    paper_influential_citation_count = Literal(row['influentialCitationCount'])
    g.add((paper_uri, influentialCitationCount.tieneInfluentialCitationCount, paper_influential_citation_count))
    
    # Agregar la tripleta Paper-tieneIsOpenAccess-IsOpenAccess
    paper_is_open_access = Literal(row['isOpenAccess'])
    g.add((paper_uri, isOpenAccess.tieneIsOpenAccess, paper_is_open_access))
    
    # Agregar la tripleta Paper-tieneIsPublisherLicensed-IsPublisherLicensed
    paper_is_publisher_licensed = Literal(row['isPublisherLicensed'])
    g.add((paper_uri, isPublisherLicensed.tieneIsPublisherLicensed, paper_is_publisher_licensed))
    
    # Agregar las tripletas para la columna 'entities_found'
    entities = ast.literal_eval(row['entities_found'])
    for entity in entities:
        g.add((paper_uri, conceptAnotation.conceptAnotation, Literal(entity)))
    

# Serializar y guardar el grafo RDF en un archivo en formato Turtle
g.serialize(destination='ontologia.rdf', format='n3')

print("Listo sin inferir")

#Inferir tuplas
owl_reasoner = owlrl.CombinedClosure.RDFS_OWLRL_Semantics(g, False, False, False)
owl_reasoner.closure()
owl_reasoner.flush_stored_triples()

with open("inference.rdf", "w") as f:
    f.write(g.serialize(format='n3'))
