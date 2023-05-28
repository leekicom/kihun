import sqlite3
import streamlit as st
import os
import re
import webbrowser
import mod2

moon=open('speech_moon.txt',encoding='UTF-8').read()
moon=re.sub('[^가-힣]',' ',moon)


font='DoHyeon-Regular.ttf'
if st.button('Say hello'):
    st.write('Why hello there')
    webbrowser.open('http://www.naver.com')
else:
    st.write('Goodbye')
mod2_html=mod2.K계열전차승무
st.markdown(mod2_html, unsafe_allow_html=True)
# dic_word=df_word.set_index('word').to_dict()['n']
# dic_word