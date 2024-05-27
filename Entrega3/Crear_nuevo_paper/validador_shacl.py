from pyshacl import validate
from rdflib import Graph

# Cargar tu ontología RDF y las restricciones SHACL
data_graph = Graph()
data_graph.parse("Entrega2\\Ontología\\ontologia.rdf", format="n3")

shacl_graph = Graph()
shacl_graph.parse("Entrega3\\Crear_nuevo_paper\\restricciones_shacl.ttl", format="ttl")

# Validar la ontología RDF con respecto a las restricciones SHACL
conforms, _, _ = validate(data_graph, shacl_graph)

if conforms:
    print("La ontología cumple con las restricciones SHACL.")
else:
    print("La ontología NO cumple con las restricciones SHACL.")
