# Para crear el requirements.txt ejecutamos 
# pipreqs --encoding=utf8 --force

# Primera Carga a Github
# git init
# git add .
# git remote add origin https://github.com/nicoig/speech-to-text.git
# git commit -m "Initial commit"
# git push -u origin master

# Actualizar Repo de Github
# git add .
# git commit -m "Se actualizan las variables de entorno"
# git push origin master

# En Render
# agregar en variables de entorno
# PYTHON_VERSION = 3.9.12

################################################



import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Función Audio a Texto
def audio_to_text(audio_file):
    if api_key == '':
        st.error('Por favor, configura tu clave API de OpenAI en el archivo .env')
        return None
    else:
        try:
            client = OpenAI(api_key=api_key)

            # Se asume que el archivo es un objeto tipo BytesIO
            transcriptions = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )
            return transcriptions

        except Exception as error:
            st.error(f"Se produjo un error al procesar el audio: {error}")
            return None

# Diseño de la Aplicación Streamlit
st.title("Audio a Texto con OpenAI")

# Inicializar la variable de estado
if 'transcription_result' not in st.session_state:
    st.session_state.transcription_result = ""

uploaded_file = st.file_uploader("Sube un archivo de audio", type=['mp3', 'wav'], on_change=lambda: setattr(st.session_state, 'transcription_result', ''))

if uploaded_file is not None and st.button("Enviar"):
    with st.spinner('Cargando...'):
        text_result = audio_to_text(uploaded_file)
        if text_result is not None:
            st.session_state.transcription_result = text_result
            st.success('Transcripción completada')

if st.session_state.transcription_result:
    st.text_area("Texto resultante:", st.session_state.transcription_result, height=300)
    st.download_button(
        label="Descargar Texto",
        data=st.session_state.transcription_result,
        file_name="transcripcion.txt",
        mime="text/plain"
    )
