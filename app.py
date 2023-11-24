# Para crear el requirements.txt ejecutamos 
# pipreqs --encoding=utf8 --force

# Primera Carga a Github
# git init
# git add .
# git remote add origin https://github.com/nicoig/text-to-speech.git
# git commit -m "Initial commit"
# git push -u origin master

# Actualizar Repo de Github
# git add .
# git commit -m "Se actualizan las variables de entorno"
# git push origin master

# En Render
# agregar en variables de entorno
# PYTHON_VERSION = 3.9.12

# git remote set-url origin https://github.com/nicoig/text-to-speech.git
# git remote -v
# git push -u origin main

################################################



import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import tempfile

# Cargar variables de entorno
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Función Texto a Voz
def tts(text, model, voice):
    if api_key == '':
        st.error('Por favor, configura tu clave API de OpenAI en el archivo .env')
        return None
    else:
        try:
            client = OpenAI(api_key=api_key)

            response = client.audio.speech.create(
                model=model, # "tts-1", "tts-1-hd"
                voice=voice, # 'alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'
                input=text,
            )
            return response.content
        except Exception as error:
            st.error(f"Se produjo un error al generar el habla: {error}")
            return None

# Diseño de la Aplicación Streamlit
st.title("API de Texto a Voz de OpenAI con Streamlit")

model = st.selectbox("Modelo", ['tts-1', 'tts-1-hd'], index=0)
voice = st.selectbox("Opciones de Voz", ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'], index=0)

# Variable de estado para el campo de texto
text = st.text_area("Ingresa el texto:", "", key="text_state")

if st.button("Enviar"):
    with st.spinner('Cargando...'):
        audio_content = tts(text, model, voice)
        if audio_content is not None:
            st.success('Se ha generado el audio')
            # Guardar el audio en un archivo temporal
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tmp_file.write(audio_content)
                tmp_file_path = tmp_file.name
            # Mostrar el audio y el botón de descarga
            st.audio(tmp_file_path, format="audio/mp3")
            st.download_button(label="Descargar Audio", data=audio_content, file_name="audio_generado.mp3", mime="audio/mp3")
