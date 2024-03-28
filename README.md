# WEBSCRAPPING APP (Docker - MariaDB - PHPMyAdmin - StreamLit)

## Descripción: 
LinkScribe es una aplicación web/mobile/desktop que utiliza NLP para permitir a los usuarios crear y organizar listas de enlaces de forma fácil y eficiente. Con LinkScribe, los usuarios pueden simplemente copiar y pegar un enlace web, y la aplicación lo procesará automáticamente, extrayendo información sobre el contenido de la página y clasificándolos de acuerdo a la información obtenida, por ejemplo, AI, Machine Learning, Educación, Travel etc.
Los usuarios pueden crear categorías personalizadas para sus listas y buscar entre ellas utilizando términos clave y palabras clave.

### Funcionalidades:
Crear y guardar listas de enlaces: Los usuarios pueden crear listas de enlaces y guardarlas en su cuenta. Cada lista puede tener una categoría y una descripción personalizada. (Opcional)
Extracción automática de información(ML Componente): LinkScribe utiliza NLP para extraer automáticamente información relevante de los enlaces, incluyendo el título, la descripción y la imagen de vista previa.
Búsqueda y filtrado avanzados: Los usuarios pueden buscar entre sus listas utilizando términos clave y palabras clave. También pueden filtrar las listas por categoría, fecha de creación y fecha de modificación.(Opcional)
Compartir listas: Los usuarios pueden compartir sus listas con amigos y colegas a través de un enlace público o una opción de invitación privada. (Opcional)

## Prouesta
a. Descripción de la empresa y sus necesidades:
La empresa SearchInt, quien ofrece servicios de desarrollo de software dirigido a centros de investigación y universidades, requiere desarrollar una aplicación web de nombre LinkScribe, que utilice NLP para permitir a los usuarios crear y organizar listas de enlaces de forma fácil y eficiente, agilizando los procesos de investigación al categorizar y resumir el contenido de páginas web que podrán servir de referencia para las diferentes necesidades de los equipos.

### Requerimientos:
Fácil uso: Los usuarios pueden simplemente copiar y pegar un enlace web, y la aplicación lo procesará automáticamente, extrayendo información sobre el contenido de la página y clasificándolos de acuerdo a la información obtenida, por ejemplo, AI, Machine Learning, Educación, Travel etc.
Crear y guardar listas de enlaces: Los usuarios pueden crear listas de enlaces y guardarlas en su cuenta. Cada lista puede tener una categoría y una descripción personalizada. (Opcional)
Extracción automática de información(ML Componente): LinkScribe utiliza NLP para extraer automáticamente información relevante de los enlaces, incluyendo el título, la descripción y la imagen de vista previa.
Búsqueda y filtrado avanzados: Los usuarios pueden buscar entre sus listas utilizando términos clave y palabras clave. También pueden filtrar las listas por categoría, fecha de creación y fecha de modificación.(Opcional)
Compartir listas: Los usuarios pueden compartir sus listas con amigos y colegas a través de un enlace público o una opción de invitación privada. (Opcional)

### Restricciones:
Datasets de entreno: Nuestros clientes presentan gran interés en las categorías representadas en los siguientes datasets, debe seleccionar 1 para entrenar el modelo:
https://www.kaggle.com/datasets/hetulmehta/website-classification/data
https://data.webarchive.org.uk/opendata/ukwa.ds.1/classification/

### BACKGROUND
Somos estudiantes de segundo semestre de la Especializacion en Inteligencia Artificial de la Universidad Autónoma de Occidente
Cali - Colombia

- Joaquin Andres Alarcon Guevara
- Jairo Velez
- Guillermo Leon Zapata Alvarez
- Yoniliman Galvis Aguirre

### BIBLIOGRAFIA
Nos basamos y usamos el conocimiento de los siguientes autores a los cuales les agradecemos su aporte a la comunidad
#### lmodel:
    - hetulmehta, Hetul Mehta, Kaggle Expert, Mumbai, Maharashtra, India, Technical Head at DataZen
        https://www.kaggle.com/code/hetulmehta/classification-of-websites
    - pagutierrez, Pedro Antonio Gutiérrez, Ph.D Computer Science and Artificial Intelligence, Spain, University of Córdoba
        https://notebook.community/pagutierrez/tutorial-sklearn/notebooks-spanish/11-extraccion_caracteristicas_texto
#### Backend
    - Vanessa Richie Alia-Trapero,  Senior Full Stack Web Dev & AI Enthusiast, Philippines
        https://github.com/vratengr/docker

## DOCKER
Vamos a tener 3 servicios docker:
    - Base de Datos, MariaDB
    - PHPmyAdmin (Necesaria para administracion de la DB)
    - Model NLP para WebScrapping
    - Streamlit, interface con el usuario

## Requisitos
- Si tienes windows debes instalar WSL para tener una terminal ubuntu en tu sistema, esta creará una unidad Ubuntu donde luego podrás clonar este repositorio
- Instala Visual Studio + la extension de WSL, recomendado instalar las extensiones de Docker, GitHub (no es necesario Github-copilot ya que requiere cuenta de pago y no es necesaria para este ejemplo), recomendado instalar las extenciones de prettier para yaml, toml, php, html 
- Una vez en la terminal ubuntu es necesario installar pip3, Docker, Docker Compose
- clona este repositorio desde la teminal de ubuntu, por defecto la carpeta debera crearse en ~/home/Webscrapping
- Usando Visual Studio abre area de trabajo y busca la carpeta (en la unidad de ubuntu) donde clonaste este git y abre webscrapping.code-workspace