# Máster en Ciencia de Datos UOC - Tipología y ciclo de vida de los datos: Práctica 1: Web scraping.

## Miembros de la práctica.

La práctica ha sido desarrollada por **Daniel Carretero San José** y **Ivan Tecles Gassó**.

## Contexto.

Se ha escogido un portal que ofrece sus recetas para su utilización de forma gratuita para la realización de una aplicación de “web scraping” capaz de extraer la información básica de recetas que tienen un ingrediente en común como es el pollo. El portal escogido es www.recetasderechupete.com y el subconjunto de recetas escogidas para su extracción serían las que se pueden acceder desde el menú “Recetas de pollo”.

## Descripción del dataset.

El dataset elaborado contiene la información básica de un conjunto de recetas del portal “recetasderechupete.com”. En concreto se centra en la obtención de información básica de las recetas que tienen como ingrediente principal el pollo. 

Cada receta posee multitud de atributos que pueden ser de interés para la realización de estudios analíticos y de todos ellos se ha hecho una selección de un subconjunto para su extracción en un dataset.

Aparte del dataset de atributos de la receta, mediante el proceso de web scraping también se obtienen los ficheros de imágenes de todas las recetas y se almacenan en un directorio local de la máquina de ejecución de la aplicación.

## Representación gráfica.

La aplicación de web scraping sigue la siguiente lógica para llegar a obtener el dataset a partir de las librerías Selenium y BeautifulSoup (se ha remarcado especialmente en qué parte del flujo se ha usado BeautifulSoup y en cual Selenium):

![Representación Gráfica](WebScrapingRecetasCocina/info/diagram.png?raw=true "Representación Gráfica")

## Ficheros del código fuente.

Se han generado dos proyectos con los siguientes ficheros y directorios:
* **WebScrapingRecetasCocina**: directorio de aplicación de web scraping que solo hace uso de la librería BeautifulSoup.
  * **main.py**: Fichero principal de entrada del programa que inicia el proceso de web scraping.
  * **datasets**: Directorio donde se almacenan los datasets obtenidos despúes de completarse el proceso de web scraping.
  * **images**: Directorio donde se almacenan todas las imágenes obtenidas de las recetas.

* **WebScrapingRecetasCocinaSelenium**: directorio de aplicación de web scraping que combina el uso de las librerías BeautifulSoup y Selenium. La navegación inicial es gestionada con Selenium y la navegación posterior y obtención de atributos es gestionada con BeautifulSoup. 
  * **main.py**: Fichero principal de entrada del programa que inicia el proceso de web scraping.
  * **datasets**: Directorio donde se almacenan los datasets obtenidos despúes de completarse el proceso de web scraping.
  * **images**: Directorio donde se almacenan todas las imágenes obtenidas de las recetas.
  * **drivers**: Directorio donde se encuentran los chromedrivers necesarios para Selenium. Es importante que los drivers ubicados en esta carpeta sean los adecuados para el sistema operativo y la versión de chrome donde se ejecute la aplicación. Se puede encontrar mas información en la web https://chromedriver.chromium.org/

  
## Recursos.

1. Subirats, L., Calvo, M. (2018). Web Scraping. Editorial UOC.
2. Masip, D. (2019) El lenguaje Python. Editorial UOC.
3. Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2.
Scraping the Data.
4. Portal de Creative Commons - https://creativecommons.org/
5. Web oficial de ChromeDriver - https://chromedriver.chromium.org/