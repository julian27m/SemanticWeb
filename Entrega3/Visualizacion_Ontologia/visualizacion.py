import networkx as nx
import matplotlib.pyplot as plt
import rdflib

# Crear un grafo dirigido para representar la red de conceptos
G = nx.DiGraph()

# Cargar los datos RDF desde un archivo
archivo_rdf = "Entrega2\\Ontología\\inference.ttl"
g = rdflib.Graph()
g.parse(archivo_rdf, format="n3")  # Ajusta el formato según el formato de tu archivo RDF

# Extraer los conceptos y conexiones de tu grafo RDF
conceptos = set()
conexiones = set()

for sujeto, predicado, objeto in g:
    if predicado == rdflib.term.URIRef("http://example.org/ontology#tieneConexiónCon"):  # Ajusta el predicado según tu ontología RDF
        concepto1 = str(sujeto)
        concepto2 = str(objeto)
        conexiones.add((concepto1, concepto2))
        conceptos.add(concepto1)
        conceptos.add(concepto2)

# Agregar nodos (conceptos)
G.add_nodes_from(conceptos)

# Agregar bordes (conexiones entre conceptos)
G.add_edges_from(conexiones)

# Calcular la densidad de conexión
densidad = nx.density(G)
print("Densidad de conexión:", densidad)

# Identificar clusters utilizando el algoritmo de Louvain
communities = nx.algorithms.community.greedy_modularity_communities(G)

# Dibujar la red con nodos y bordes
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)  # Layout para la visualización
nx.draw_networkx_nodes(G, pos, node_size=200)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

# Resaltar los clusters identificados
for i, community in enumerate(communities):
    nx.draw_networkx_nodes(G, pos, nodelist=community, node_color=f"C{i}", node_size=200)

plt.title("Visualización de la red de conceptos con clusters resaltados")
plt.axis("off")
plt.show()
