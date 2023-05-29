import sqlite3
import streamlit as st
import os
import re
import webbrowser
import mod2
from PIL import Image

if st.button('Say hello'):
    st.write('Why hello there')
    webbrowser.open('http://www.naver.com')
else:
    st.write('Goodbye')
image = Image.open('image/K계열전차승무.jpeg')
st.image(image, caption='K계열전차승무')
mod2_html=mod2.k121101
st.markdown(mod2_html, unsafe_allow_html=True)
# dic_word=df_word.set_index('word').to_dict()['n']
# dic_word