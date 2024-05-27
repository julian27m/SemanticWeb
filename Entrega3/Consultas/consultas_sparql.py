from rdflib import Graph

# Crear un grafo RDF
g = Graph()

# Cargar la ontología RDF desde un archivo
ontology_file = "Entrega2\\Ontología\\ontologia.rdf"
g.parse(ontology_file, format="n3")  # El formato depende del formato en el que esté tu archivo RDF

# Consulta SPARQL
query = """
    PREFIX ns: <http://example.org/ontology#>
    SELECT ?paper1 ?paper2
    WHERE {
        ?paper1 rdf:type ns:Paper .
        ?paper2 rdf:type ns:Paper .
        ?paper1 ns:conceptAnotation ?concept .
        ?paper2 ns:conceptAnotation ?concept .
        FILTER (?paper1 != ?paper2)
    }
"""
query2 = """
    PREFIX ns: <http://example.org/ontology#>
    SELECT ?paper1 ?paper2 ?citationCount1 ?citationCount2
    WHERE {
        ?paper1 rdf:type ns:Paper .
        ?paper2 rdf:type ns:Paper .
        ?paper1 ns:conceptAnotation ?concept .
        ?paper2 ns:conceptAnotation ?concept .
        FILTER (?paper1 != ?paper2)
        ?paper1 ns:citationCount ?citationCount1 .
        ?paper2 ns:citationCount ?citationCount2 .
        FILTER (?citationCount1 = ?citationCount2)
    }
"""


query3 = """
    PREFIX ns: <http://example.org/ontology#>
    SELECT ?paper1 ?paper2 ?author
    WHERE {
        ?paper1 rdf:type ns:Paper .
        ?paper2 rdf:type ns:Paper .
        ?paper1 ns:conceptAnotation ?concept .
        ?paper2 ns:conceptAnotation ?concept .
        FILTER (?paper1 != ?paper2)
        ?paper1 ns:autor ?author .
        ?paper2 ns:autor ?author .
    }
"""

query4 = """
    PREFIX ns: <http://example.org/ontology#>
    SELECT ?paper1 ?paper2 ?venue
    WHERE {
        ?paper1 rdf:type ns:Paper .
        ?paper2 rdf:type ns:Paper .
        ?paper1 ns:conceptAnotation ?concept .
        ?paper2 ns:conceptAnotation ?concept .
        FILTER (?paper1 != ?paper2)
        ?paper1 ns:venue ?venue .
        ?paper2 ns:venue ?venue .
    }
"""

query5 = """
    PREFIX ns: <http://example.org/ontology#>
    SELECT ?paper1 ?paper2 ?year1 ?year2
    WHERE {
        ?paper1 rdf:type ns:Paper .
        ?paper2 rdf:type ns:Paper .
        ?paper1 ns:conceptAnotation ?concept .
        ?paper2 ns:conceptAnotation ?concept .
        FILTER (?paper1 != ?paper2)
        ?paper1 ns:yearPublicacion ?year1 .
        ?paper2 ns:yearPublicacion ?year2 .
        FILTER (?year1 = ?year2)
    }
"""



# Ejecutar la consulta SPARQL sobre el grafo RDF
results = g.query(query)

# Imprimir los resultados
for row in results:
    paper1 = row['paper1']
    paper2 = row['paper2']
    print(f"Paper 1: {paper1}, Paper 2: {paper2}")
