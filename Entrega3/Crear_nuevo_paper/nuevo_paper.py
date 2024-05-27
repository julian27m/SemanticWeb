from rdflib import Graph, Literal, Namespace, RDF, URIRef
from rdflib.namespace import XSD  # Importar el módulo XSD

# Definir el namespace de tu ontología
ns = Namespace("http://example.org/ontology#")

# Crear un grafo RDF y cargar la ontología desde el archivo OWL existente
g = Graph()
g.parse("Entrega2\\Ontología\\ontologia.rdf", format="n3")

# Definir el URI del nuevo paper
paper_uri = URIRef("http://example.org/papers/paper124")

# Agregar el tipo de paper
g.add((paper_uri, RDF.type, ns.Paper))

# Agregar los valores de las propiedades de datos del paper
g.add((paper_uri, ns.hasAbstract, Literal("Este es el abstract del nuevo paper")))
g.add((paper_uri, ns.hasIntroduccion, Literal("Introducción desssdsdsl nuevo paper")))
g.add((paper_uri, ns.hasKeyWords, Literal("keyword1, keyword2")))
g.add((paper_uri, ns.hasCitationVelocity, Literal("10", datatype=XSD.integer)))
g.add((paper_uri, ns.hasDOI, Literal("doi_del_nuevo_paper")))
g.add((paper_uri, ns.hasPaperId, Literal("paper123")))
g.add((paper_uri, ns.hasVenue, Literal("Venue del nuevo paper")))
g.add((paper_uri, ns.hasAñoPublicacion, Literal("2023", datatype=XSD.integer)))
g.add((paper_uri, ns.hasIsOpenAccess, Literal("true", datatype=XSD.boolean)))
g.add((paper_uri, ns.hasIsPublisherLicensed, Literal("false", datatype=XSD.boolean)))

# Guardar el grafo RDF actualizado en el mismo archivo OWL
g.serialize(destination="Entrega2\\Ontología\\ontologia.rdf", format="n3")
