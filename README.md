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
- 
### Notas importantes:
- Cada consulta de un articulo tiene un time out para evitar que el API rechaze las peticiones por superar el timerate.
- El tiempo de espera para la descarga de un archivo PDF es de 5 sengundos, si en este tiempo no se ha logrado descargar el archivo se pasará al siguiente artículo.
- Los Pdfs se almacenarán en la carpeta PDFs, y en el dataframe al final habrá una casilla con una ruta relativa a esta carpeta.
- Al finalizar la ejecución de las  consultas se creará un Json con la Metadata de todos los artículos. Este archivo Json se convertirá a un Datframe de Pandas, PERO el tamaño de RAM de la maquina debe ser doblemente proporcional al tamanio del archivo.

## Entrega 2 ##
### Instrucciones de ejecución:
- Para ejecutar el código, primero debe instalar las bibliotecas necesarias. Puede hacer esto ejecutando el siguiente comando:
   
   ```pip install -r requirements.py```
- Para extraer metadatos de los PDFs será necesario utilizar GROBID.
  Para iniciar el servidor GROBID hay que ejecutar los siguientes comandos:
  
  ```cd Entrega2```
  
  ```docker-compose up -d```

## Integrantes ##
- <a href="https://github.com/Juanes1516" target="_blank">Juan Esteban Rodríguez Ospino</a>
- <a href="https://github.com/julian27m/" target="_blank">Julián Camilo Mora Valbuena</a>
- <a href="https://github.com/andreapapadron/" target="_blank">Andrea Vega</a>


