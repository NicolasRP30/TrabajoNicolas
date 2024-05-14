import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import json
import os
import base64
from openai import OpenAI
from PIL import Image

st.title("Esto es Internet de las cosas")

st.write("El concepto también conocido como IoT se refiere a la interconexión de dispositivos físicos que están integrados con sensores, software" 
"y conectividad para recopilar y compartir datos entre sí y con otras plataformas. En el contexto de la inteligencia urbana" 
"y las ciudades inteligentes, el IoT desempeña un papel clave para hacer más eficientes los servicios urbanos. Al conectar dispositivos" 
"como semáforos, sensores de calidad del aire, medidores de agua y sistemas de transporte público, se puede recopilar información en" 
"tiempo real para tomar decisiones más informadas y mejorar la calidad de vida de los ciudadanos." 

st.subheader("Soluciones inteligentes:")
st.write("EL internet de las cosas hace parte de las soluciones innovadoras en áreas como la gestión del tráfico, la conservación de energía," 
"la seguridad pública y la prestación de servicios urbanos más personalizados y eficientes. En resumen, el IoT es un habilitador clave para" 
"la transformación de las ciudades hacia entornos más inteligentes y conectados.")
"Te invitamos a que monitorees con nosotros la humedad y temperatura de la ciudad para definir como estoas variables inciden" 
"en el trafico urbano. Ingresa a https://demo.thingsboard.io/dashboards/0a666910-121d-11ef-b68a-bfe4060367e5")
         

image = Image.open('Sensores humedad y temperatura.jpeg')
st.image(image)

# Function to encode the image to base64
def encode_image(image_file):
    return base64.b64encode(image_file.getvalue()).decode("utf-8")
