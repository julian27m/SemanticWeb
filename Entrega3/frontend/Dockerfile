# Dockerfile para el frontend
FROM node:18

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . /app

# Instalar las dependencias
RUN npm install
RUN npm install -g @angular/cli

# Construir la aplicación Angular
RUN ng build --configuration production

# Instalar un servidor HTTP simple para servir los archivos estáticos
RUN npm install -g http-server

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8080

# Comando para correr la aplicación
CMD ["http-server", "dist/proyecto-frontend", "-p", "8080"]
