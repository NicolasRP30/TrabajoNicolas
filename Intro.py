import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import json

from PIL import Image

st.title("Introduccion de Inteligencia Urbana")

st.write("Esta es la recopilación de trabajos que se han realizado en la materia de Inteligencia Urbana")

image = Image.open('Ciudades_Inteligentes.jpg')
st.image(image)

