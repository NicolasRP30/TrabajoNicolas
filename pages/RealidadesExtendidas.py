import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import json
import os
import base64
from openai import OpenAI
from PIL import Image

st.title("Esto es Realidades extendidas")

st.write("En este capitulo de realidades extendidas exploramos otros planos para la presentación de proyectos y sobre todo para realizar" 
"inmesiones en espacios del metaverso")
         
st.write("Te invitamos a que explores nuestra galeria y veas los proyectos realizados en este semestre:" 
"https://www.spatial.io/s/nrestrepops-Digital-Hangout-66314548ff215563ea47ef04")
         

image = Image.open('avatar.png')
st.image(image)
