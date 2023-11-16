# API de Texto a Voz de OpenAI con Streamlit

## Descripción
Este proyecto es una aplicación web desarrollada con Streamlit que permite a los usuarios convertir texto en habla utilizando la API de Texto a Voz (TTS) de OpenAI. La aplicación proporciona una interfaz interactiva para introducir texto, seleccionar un modelo y una voz, y generar audio basado en el texto ingresado.

## Características
- Interfaz web para ingresar texto a convertir en voz.
- Opción para seleccionar entre diferentes modelos y voces proporcionadas por OpenAI.
- Generación de audio y reproducción en la misma interfaz.

## Requisitos
- Python 3.x
- Streamlit
- Biblioteca OpenAI Python
- python-dotenv

## Instalación
Para instalar y ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. Clona el repositorio:
   git clone https://github.com/nicoig/text-to-speech.git

2. Navega al directorio del proyecto:
cd [Nombre del directorio del proyecto]

3. Instala las dependencias:
pip install -r requirements.txt

## Configuración
Debes proporcionar tu clave API de OpenAI en un archivo .env:

1. Crea un archivo .env en el directorio raíz del proyecto.
2. ñade la siguiente línea, reemplazando [Tu Clave API de OpenAI] con tu clave API real:
OPENAI_API_KEY=[Tu Clave API de OpenAI]

## Uso
Para ejecutar la aplicación, usa el siguiente comando:
streamlit run app.py

Después de ejecutarlo, Streamlit abrirá una ventana en tu navegador. Introduce el texto que deseas convertir en voz, selecciona el modelo y la voz, y haz clic en "Enviar" para generar el audio.

## Contribución
Las contribuciones a este proyecto son bienvenidas. Si tienes sugerencias para mejorar la aplicación, no dudes en crear un 'issue' o un 'pull request'.

