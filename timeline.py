# Streamlit Timeline Component Example

import streamlit as st
from streamlit_timeline import timeline
#from PIL import Image
#im = Image.open('IMG_7274k_colour_round_cut.png')
#st.set_page_config(page_title='CV Oskar Schnappauf', page_icon=im, layout="wide")
st.set_page_config(page_title='CV Oskar Schnappauf', layout="wide")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#st.set_page_config(page_title='CV Oskar Schnappauf', page_icon=im)
#with open( "style.css" ) as css:
#    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

#image = Image.open('IMG_7274k_colour_round_cut.png')
#st.sidebar.image(image, width=None)
#st.sidebar.header('Oskar Schnappauf, Ph.D, FACMG')
#st.header('CURRICULUM VITAE - OSKAR SCHNAPPAUF, PHD, FACMG')
#col1, col2 = st.columns(2)

with open('Education_Work_Certificates_Publications.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=1000)

# with open('Certificates_Publications.json', "r") as f:
#     data = f.read()
#
# # render timeline
# timeline(data, height=1000)
