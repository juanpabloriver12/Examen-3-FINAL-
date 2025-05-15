# EXAMEN 3 FINAL (DOCKER)
### AUTOR: JUAN PABLO RIVERA RAMIREZ ID:000554193
---
##  Descripción
Este proyecto consiste en una aplicación web ligera y escalable desarrollada con **Python** y **Flask**, empaquetada dentro de un contenedor **Docker**.  
La finalidad de este proyecto es demostrar de forma práctica los conocimientos adquiridos en el curso de **Telemática** con caz 8am (el mejor curso), haciendo énfasis en el uso de contenedores para facilitar el despliegue de servicios web modernos.
---
##  Tecnologías Utilizadas
- **Lenguaje:** Python 3.12
- **Framework:** Flask  
- **Contenerización:** Docker  
- **Control de Versiones:** Git & GitHub
- **Infraestructura Usada:** Local desde la terminal y AWS EC2 mediante instancia 
- **Sistema Operativo:** Linux Mint (VirtualBox)
---
  ## Instrucciones Paso a Paso para Ejecutar el Proyecto
- 1. Hacemos primero esto
```bash
sudo apt update
```
- 2. Luego instalamos docker
```bash
sudo apt install docker-compose
```
- 3. Clonamos este o creamos uno desde cero (Yo voy a poner el link del mio)
```bash
git clone https://github.com/juanpabloriver12/Examen-3-FINAL.git
```
- 4. Entramos a este
```bash
cd Examen-3-FINAL
```
- 5. Contruye la imagen
```bash
sudo docker build -t appExamen:v01 //Le ponemos el nombre que queramos y donde esta 01 tambien
```
- 6.  Iniciar el contenedor(Docker)
```bash
sudo docker run -d -p 80:80 appExamen:v01 //En 80:80 es el puerto entonces podemos tambien usar otro puerto como 8005
```
- 7. Verificamos el contenedor
```bash
sudo docker ps
```
-8 Comprobamos la pagina
```bash
http://(IP publica) // y al final segun el puerto le ponemos si le pusimos el 8005 lo terminas en :8005
```
---
## Para Modificar
```bash
- nano main.py
```
---
## Para Detener el contenedor
```bash
- sudo docker stop ID CONTENEDOR
```
---
## Para Eliminar el contenedor
```bash
- sudo docker rm ID CONTENEDOR
```

## Nota
- Si vamos a cambiar o modificar tenemos que parar el contenedor eliminarlo y volverlo a iniciar con los anteriores comandos 
