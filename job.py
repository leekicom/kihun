import sqlite3
import streamlit as st
import pandas as pd
import altair as alt
import os
import mod1
import mod2
from PIL import Image

def emp_hg():
    st.header("직업선호도 유형")
    df1=mod2.emp1_query('직업선호도')
    col1, col2 = st.columns(2) 
    with col1:
        test1=st.selectbox('군을 선택하세요',df1['군별'].drop_duplicates(keep='first'),0)
    with col2:    
        test2=st.selectbox('특기를 선택하세요',df1['특기'].drop_duplicates(keep="first"),0)
    df2=df1.query("군별=='"+test1+"' & 특기=='"+test2+"' ")
    # restult1=df2[['특기','현실형','탐구형','예술형','사회형','진취형','관습형']]
    st.dataframe(df2)
 
    # df1=gun_query()
    # col1, col2 = st.columns(2) 
    # with col1:
    #     test1=st.selectbox('군사특기를 선택하세요',df1['군사특기명'].drop_duplicates(keep='first'),0)
    # with col2:
    #     test2=st.selectbox('입영부대를 선택하세요',df1['입영부대'].drop_duplicates(keep="first"),0)
    # df2=df1.query("군사특기명=='"+test1+"' & 입영부대=='"+test2+"' ")
    # restult1=df2[['입영월','접수인원','지원인원','커트라인']]
    # restult2=restult1.melt('입영월', var_name='구분', value_name='인원/점수')
    # restult1.set_index(['입영월'],inplace=True)
    # rst1=restult1.transpose()
    # st.dataframe(rst1)
page_names_to_funcs = {
"직업선호도 유형":emp_hg,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()