import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import json

from PIL import Image

st.title("Esto es Inteligencia Artificial")

st.write("Aqui podemos ver el proyecto de Inteligencia Artificial desarrollado en la materia de Inteligencia Urbana")

image = Image.open('DetectorIma.jpg')
st.image(image)
