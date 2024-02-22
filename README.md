# SemanticWeb

## OBJETIVO DEL PROYECTO
El proyecto pretende aplicar los conceptos y tecnologías de la WEB semántica para modelar, integrar y
publicar información proveniente de fuentes de datos semi estructurados. Como producto final, se
desarrollará una aplicación WEB que despliegue la información sobre artículos de investigación y citas
provenientes de estos a partir de un set de datos vinculado (linked data set) construido y capaz de inferir
información sobre citas y contextos de cita. El proyecto se divide en 3 Etapas (Figura 1). Al final de
cada una, los estudiantes deberán entregar un conjunto de productos y realizar una sustentación oral.

![image](https://github.com/julian27m/SemanticWeb/assets/69479452/3d2a0c14-60ca-4427-a956-b09de4cafc0d)


En la primera etapa del proyecto, los estudiantes deberán extraer información relacionada con los
artículos de investigación y sus respectivas referencias. Cada grupo deberá extraer metadatos de
artículos de investigación (por ejemplo, título, resumen, año, etc.). De ser posible, también deben
descargar el PDF completo de cada artículo, utilizando diferentes APIs y, de ser posible, extrayendo
información relevante de los PDFs (por ejemplo, palabras clave, referencias, etc.). En esta etapa, los
estudiantes deberán realizar un proceso de extracción de información, limpieza y posterior unificación
de las fuentes. En la segunda fase, los estudiantes utilizarán los conocimientos adquiridos en ingeniería
Ontológica para modelar el dominio asignado y realizar un mapeo entre la información capturada en la
etapa 1 y la ontología construida. La etapa 2 finaliza con la instalación de una base de datos basada en
grafos (como neo4j o AllegroGraph) donde se debe cargar la ontología con la información capturada
en la etapa 1. En la etapa 3, los estudiantes crearán un dataset vinculado (linked dataset) donde se espera
que puedan inferir información relevante sobre las relaciones entre las diferentes entidades. Primero
vincularán instancias de su dataset con Dbpedia y posteriormente harán uso de un endpoint SPARQL
para el consumo del mismo. Cada grupo deberá crear una aplicación WEB que presente la información
de las citas de los artículos. Además, la aplicación debe permitir realizar análisis sobre las conexiones
existentes entre los artículos y las citas realizadas en estos.

### GRUPOS: 4 personas
### ETAPA 1: Captura de datos no estructurados

Cada grupo tendrá asignado un dataset, el cual contiene información acerca de los metadatos de un
grupo de artículos. Su tarea consiste en analizar el PDF asociado a cada artículo con el fin de extraer
información adicional del artículo, como secciones, palabras clave, autores (en caso de ser necesario) y
lo más importante, las referencias que este usa. Con dichas fuentes, deben realizar una búsqueda en los
diferentes APIs para extraer los metadatos asociados al artículo (por ejemplo, título, resumen, año,
revista, etc.) y, de ser posible, la descarga correspondiente del artículo en formato PDF. Una vez
identificadas las fuentes a trabajar, el grupo de estudiantes deberá realizar las siguientes tareas:
1. Identificar la información disponible en cada una de las fuentes. Deberán responder las
siguientes preguntas: ¿Qué información está disponible? ¿Hay relaciones explícitas entre la
información (vínculos que amplían o contienen información relacionada)? ¿La información
desplegada tiene algún tipo de organización? ¿Existe homogeneidad en la información que se
despliega (por ejemplo, ¿el nombre de las diferentes revistas es homogéneo o puede tener
variaciones de escritura)?
2. Construir una estructura básica en tablas que les permita capturar de forma organizada la
información de cada fuente y les permita estructurar los archivos csv que van a generar de cada
fuente. No es necesario que sigan un modelamiento relacional de Base de Datos. Dado que cada
fuente contiene diferente información, se espera que realicen este proceso para cada una. Para
el caso de los PDFs, deberán almacenarlos en una carpeta y en el formato CSV especificar la
ruta necesaria para llegar a ellos.
3. Construir un programa en el lenguaje que deseen que les permita extraer la información de cada
fuente. Al final de este proceso para cada fuente debe existir un conjunto de archivos csv con
la información capturada (la primera fila de este archivo debe desplegar los nombres de
columnas definidos en el punto anterior). Bajo ningún motivo su proceso debe afectar la
disponibilidad de las fuentes.
4. Limpieza de la información: Muy seguramente la información capturada no está limpia o carece
de formato estándar (por ejemplo, fechas en diferentes formatos, nombres separados por
caracteres, espacios, caracteres especiales, etc.). Realicen un proceso de limpieza y
estandarización de valores de datos y documenten.
Consideraciones:
- Para el análisis de los documentos PDF se recomienda el uso de alguna de las siguientes
herramientas:
  - CERMINE: http://cermine.ceon.pl/index.html (DEMO)
  - GROBID: https://github.com/kermitt2/grobid
  - ParsCit: https://github.com/WING-NUS/Neural-ParsCit
- Algunas de estas herramientas generan archivos XML para su análisis se recomienda el uso de
librerías como beautifulsoup (https://pypi.org/project/beautifulsoup4/)
3
• Para la extracción de los metadatos y los artículos de investigación puede usar las siguientes
APIs:
  - https://info.arxiv.org/help/bulk_data.html
  - https://core.ac.uk/services

## Entregables ETAPA 1:
- Documento de máximo 4 páginas con descripción de las fuentes y el proceso de extracción y
limpieza de los datos, tecnologías usadas, retos y problemas del proceso.
- Código fuente de proceso de extracción y limpieza desarrollado.
- CSV con la información de cada uno de los artículos (especifique para cada artículo el API que
utilizo para conseguir y extraer su información)
- Carpeta con los archivos PDF de los artículos extraídos (recuerde que debe existir una relación
entre el nombre del archivo con su respectivo artículo en el CSV)
Nota: Se espera que cada grupo logre un total de 5 mil artículos como mínimo, en caso de que le falte
información deberá usar los APIs para extraer información relacionada a artículos de investigación
en el área de procesamiento de lenguaje natural
