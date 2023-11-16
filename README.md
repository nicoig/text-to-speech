# Transcripción de Audio a Texto con OpenAI

## Descripción
Este proyecto es una aplicación web desarrollada con Streamlit que permite a los usuarios subir archivos de audio y obtener su transcripción utilizando la API de OpenAI. Es una herramienta útil para convertir rápidamente grabaciones de voz o sonido en texto editable.

## Características
- Interfaz web sencilla para cargar archivos de audio.
- Uso de la API de OpenAI para realizar transcripciones de audio a texto.
- Capacidad para descargar el texto transcrito.

## Requisitos
- Python 3.x
- Streamlit
- Biblioteca OpenAI Python
- python-dotenv

## Instalación
Para instalar y ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. Clona el repositorio:
   git clone https://github.com/nicoig/speech-to-text.git

2. Navega al directorio del proyecto:
cd [Nombre del directorio del proyecto]

3. Instala las dependencias:
pip install -r requirements.txt

## Configuración
Debes proporcionar tu clave API de OpenAI en un archivo .env:

1. Crea un archivo .env en el directorio raíz del proyecto.
2. Añade la siguiente línea, reemplazando [Tu Clave API de OpenAI] con tu clave API real:
OPENAI_API_KEY=[Tu Clave API de OpenAI]

## Uso
Para ejecutar la aplicación, usa el siguiente comando:
streamlit run app.py

Después de ejecutarlo, Streamlit abrirá una ventana en tu navegador donde podrás cargar archivos de audio y obtener transcripciones.

## Contribución
Las contribuciones a este proyecto son bienvenidas. Si tienes sugerencias para mejorar la aplicación, no dudes en crear un 'issue' o un 'pull request'.

