import sqlite3
import streamlit as st
import pandas as pd
import altair as alt
import os
import mod1
import mod2
from PIL import Image

def emp_hg():
    st.header("취업맞춤특기병 지원가능 학과")
    df1=mod2.emp1_query('emp1')
    test1=st.selectbox('학교를 선택하세요',df1['학교명'].drop_duplicates(keep='first'),0)
    txt3=''.join(test1)

    st.text("학교명:"+test1)
    emp_df=mod2.emp_query('emp1',txt3)
    test2=st.selectbox('학과를 선택하세요',emp_df['학과명'].drop_duplicates(keep='first'),0)
    txt4=''.join(test2)
    tt1=mod2.emp2_query('emp1',txt3,txt4)
    st.dataframe(tt1,width=800)
def emp_gy():
    mod1_html=mod1.html62
    st.markdown(mod1_html, unsafe_allow_html=True)
def emp_an():
    mod1_html1=mod1.html63
    st.markdown(mod1_html1, unsafe_allow_html=True)
def emp_jw():
    mod1_html2=mod1.html64
    st.markdown(mod1_html2, unsafe_allow_html=True)
page_names_to_funcs = {
    "취업맞춤특기병 지원가능 학과":emp_hg,
    "취업맞춤특기병 모집개요":emp_gy,
    "취업맞춤특기병 모집안내":emp_an,
    "취업맞춤특기병 지원절차":emp_jw,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()