# Streamlit Timeline Component Example

import streamlit as st
from streamlit_timeline import timeline
from PIL import Image

im = Image.open('IMG_7274k_colour_round_cut.png')
st.set_page_config(page_title='CV Oskar Schnappauf', page_icon=im, layout="wide")
image = Image.open('IMG_7274k_colour.jpg')
#st.sidebar.image(image, width=None)
#st.sidebar.header('Oskar Schnappauf, Ph.D, FACMG')
st.header('TIMELINE - OSKAR SCHNAPPAUF')
#st.image(image, width=400)
# use full page width
#st.set_page_config(page_title="Timeline Example", layout="wide")

# load data
with open('example.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=700)
