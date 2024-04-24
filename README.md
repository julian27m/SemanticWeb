<h1 align="center">
  Semantic Web
  <br>
</h1>
<p align="center">
  <a href="#entrega-1">Entrega 1</a> &#xa0; | &#xa0; 
  <a href="#entrega-2">Entrega 2</a> &#xa0; | &#xa0;
  <a href="#integrantes">Integrantes</a> &#xa0; | &#xa0;
</p>


## Entrega 1 ##
### Instrucciones de ejecución:
- Para ejecutar el código, primero debe instalar las bibliotecas necesarias. Puede hacer esto ejecutando el siguiente comando:
   
   ```pip install -r requirements.py```
- Asegúrese de tener el archivo `dict_split_1.json` dentro del mismo directorio que `data.py`.
- Ejecute el script `data.py` para extraer información de artículos científicos a través del API de Semantic Scholar.
- Ejecute el script `convertir_json_csv.py` para convertir la información previamente extraida a formato csv.
- Por último, ejecuta el script `limpieza_datos.py` para realizar la limpieza de los datos.

### Notas importantes:
- Cada consulta de un articulo tiene un time out para evitar que el API rechaze las peticiones por superar el timerate.
- El tiempo de espera para la descarga de un archivo PDF es de 5 sengundos, si en este tiempo no se ha logrado descargar el archivo se pasará al siguiente artículo.
- Los Pdfs se almacenarán en la carpeta PDFs, y en el dataframe al final habrá una casilla con una ruta relativa a esta carpeta.
- Al finalizar la ejecución de las  consultas se creará un Json con la Metadata de todos los artículos. Este archivo Json se convertirá a un Datframe de Pandas, PERO el tamaño de RAM de la maquina debe ser doblemente proporcional al tamanio del archivo.

## Entrega 2 ##
### Instrucciones de ejecución:
- Para ejecutar el código, primero debe instalar las bibliotecas necesarias. Puede hacer esto ejecutando el siguiente comando:
   
   ```pip install -r requirements.py```

Ahora, para realizar adecuadamente esta entrega tuvimos que completar algunos requerimientos de la entrega anterior. Por lo tanto, dentro de la carpeta `/Entrega2/` se encuentran el archivo `docker-compose.yml` y `spotlight-compose.yml` los cuales son contenedores de Docker con las imágenes de Grobid y DBpedia Spotlight, respectivamente. 

Usos:
- Grobid: Utilizado para extraer más metadatos de los PDFs, como abstract, introducción, palabras clave y conclusiones.
- DBpedia Spotlight: Utilizado para anotar las menciones de recursos de DBpedia, dentro de nuestros artículos.

Ejecución de los contenedores:
Los scripts que requieren la ejecución de los contenedores son: `analisis_pdf.py` y `busqueda_anotaciones.py`.

- Para iniciar ambos contenedores hay que ejecutar los siguientes comandos:
  
  1. Navegar a la ruta donde se encuentran los contenedores: ```cd Entrega2```

  2. Instalar Docker Compose en caso de no tenerlo: ```sudo apt install docker-compose``` 

  3. Iniciar el contenedor de Grobid para ejecutar analisis_pdf.py: ```sudo docker-compose up -d```
  4. Detener el contenedor de Grobid: ```docker-compose down```
  5. Iniciar el contenedor de DBpedia Spotlight para ejecutar busqueda_anotaciones.py: ```docker-compose -f spotlight-compose.yml up -d```
  6. Detener el contenedor de Grobid: ```docker-compose -f spotlight-compose.yml stop```

### Ejecución de los scripts:
Para la ejecución de esta entrega se siguieron los pasos descritos a continuación, en orden:
1. El script `analisis_pdf.py` es utilizado para analizar el CSV de la entrega pasada. Este script utiliza Grobid para extraer metadatos de los PDFs almacenados en la ruta `/DescargasPDFs/`, con el fin de agregarlos como columnas a un nuevo CSV. Los datos extraídos son: Abstract, Introducción, Palabras Clave y Conclusiones. Este script crea el archivo `metadatos.csv` con los nuevos datos extraídos y la información de la entrega pasada.
2. El script `busqueda_anotaciones.py` recorre el CSV creado en el punto pasado (`metadatos.csv`) y, utilizando DBpedia Spotlight, recopila las entidades relacionadas a los datos de cada artículo. Finalmente, las anotaciones (entidades) recolectadas se agregan como columnas de un nuevo archivo CSV llamado `archivo_entidades.csv`.
3. El script `crear_ontologia.py` recorre el CSV creado en el punto pasado (`archivo_entidades.csv`) y con base a este, crea la ontología. Al final de este script se serializa y guarda el grafo RDF (`ontologia.rdf`), además, también se crea y se guarda el archivo RDF con la ontología y las inferencias (`inference.rdf`).
4. Descargar la imagen de neo4j utilizando ```docker pull neo4j```.
5. Ejecutar el comando ```sudo docker run -it --rm   --publish=7474:7474 --publish=7687:7687 --volume=$HOME/neo4j/data:/data --volume=$HOME/neo4j/logs:/logs --user="$(id -u):$(id -g)"   -e NEO4J_AUTH=none   --env NEO4J_PLUGINS='["apoc","n10s"]'   neo4j:5.5.0```.
6. Agregar el archivo `inference.rdf` dentro del directorio `/neo4j/data/`.
7. Acceder a Neo4j a través de http://<ip_maquina>:7474/browser/.
8. Realizar las consultas en Neo4j.

Notas:
Los directorios `/DescargasPDFs/` y `/CSVs/` fueron agregados al .gitignore debido a que los archivos dentro de ellos son muy pesados para subir al repositorio. 

- Dentro de `/DescargasPDFs/` almacenamos los artículos descargados en formato PDF.
- En el directorio `/CSVs/` guardamos todos los archivos .csv en los que trabajamos y modificamos la base de datos final (`archivo_entidades.csv`).
- `archivo_entidades.csv` es el CSV final con los metadatos y las anotaciones de todos los artículos. Debido a su tamaño no lo incluimos en el repositorio pero pueden acceder a este en el siguiente enlace: 


## Integrantes ##
- <a href="https://github.com/Juanes1516" target="_blank">Juan Esteban Rodríguez Ospino</a>
- <a href="https://github.com/julian27m/" target="_blank">Julián Camilo Mora Valbuena</a>
- <a href="https://github.com/andreapapadron/" target="_blank">Andrea Vega</a>


