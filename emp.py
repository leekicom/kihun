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
    df1=mod2.gun1_query('emp1')

    test1=st.selectbox('학교를 선택하세요',df1['학교명'].drop_duplicates(keep='first'),0)

    df3=df1.query("학교명=='"+test1+"'")

    result3=df3['학교명'].values

    txt3=''.join(result3)

    st.text("대분류:"+txt3)
    emp_df=mod2.emp_query('txt3')
    test1=st.selectbox('학과를 선택하세요',emp_df['학과명'].drop_duplicates(keep='first'),0)

page_names_to_funcs = {
    "취업맞춤특기병 지원가능 학과":emp_hg,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()