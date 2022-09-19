# Streamlit Timeline Component Example

import streamlit as st
from streamlit_timeline import timeline
from PIL import Image
im = Image.open('IMG_7274k_colour_round_cut.png')
st.set_page_config(page_title='CV Oskar Schnappauf', page_icon=im, layout="wide")
#st.set_page_config(page_title='CV Oskar Schnappauf', page_icon=im)
#with open( "style.css" ) as css:
#    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

#image = Image.open('IMG_7274k_colour_round_cut.png')
#st.sidebar.image(image, width=None)
#st.sidebar.header('Oskar Schnappauf, Ph.D, FACMG')
#st.header('CURRICULUM VITAE - OSKAR SCHNAPPAUF, PHD, FACMG')
#col1, col2 = st.columns(2)

# with col1:
#    st.image(image, width=500)
#    st.subheader('CLINICAL MOLECULAR GENETICIST')
#
# with col2:
#    st.header("Contact")
#    st.subheader('+49 157 88224454')
#    st.subheader('Fedderstrasse 4')
#    st.subheader('79106 Freiburg im Breisgau')
#    st.subheader('oskar.schnappauf@gmail.com')
#    st.subheader('American and German Citizienship')

#st.header('Professional - OSKAR SCHNAPPAUF')

with open('Education_Work.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=1000)

with open('Certificates_Publications.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=1000)
