import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import json

from PIL import Image

st.title("Esta es la intro a la Inteligencia Urbana")

st.write("Esta es la recopilación de trabajos que se han realizado en la materia de Inteligencia Urbana en el semestre 2024 - 1" 
"en compañia con el profesor Carlos Mario. Este semestre hemos profundizado en conceptos como IoT o tambien conocido como" 
"Internet de las Cosas, Analitica de datos y la famosa AI con sus herramientas. Para el diseño urbano estas son herrmaientas" 
"poderosas para el dar soluciones a retos urbanos y rurales que mejoren la calidad de vida de los habitantes")

image = Image.open('Ciudades_Inteligentes.jpg')
st.image(image)

