import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import json
  
st.title("Introduccion de Inteligencia Urbana")

st.write("Esta es la recopilación de trabajos que se han realizado en la materia de Inteligencia Urbana")

from PIL import Image

image = Image.open('Ciudade_Inteligentes.jpeg')
st.image(image)

