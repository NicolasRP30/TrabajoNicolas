import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import json

with open('total_incidentes_transito.geojson', "r") as read_file:
    data = json.load(read_file)
  
st.title("Esta es la intro")


st.write("Esta es la recopilación de trabajos que se han realizado en la materia de Inteligencia Urbana")

