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
        df3=df1.query("군별=='"+test1+"'") 
        test2=st.selectbox('특기를 선택하세요',df3['특기'].drop_duplicates(keep="first"),0)
    df2=df1.query("군별=='"+test1+"' & 특기=='"+test2+"' ")
    restult1=df2[['특기','현실형','탐구형','예술형','사회형','진취형','관습형']]
    restult1.set_index(['특기'],inplace=True)
    st.dataframe(restult1,width=800)

    test7=st.selectbox('유형을 선택하세요',('현실형','탐구형','예술형','사회형','진취형','관습형'))
    df11=df1.query(""+test7+"==1 & 군별=='육군'")
    df11.set_index(['군별'],inplace=True)
    st.dataframe(df11,width=800)
    df12=df1.query(""+test7+"==1 & 군별=='해군'")
    st.dataframe(df12,width=800)
    df13=df1.query(""+test7+"==1 & 군별=='공군'")
    st.dataframe(df13,width=800)
    df14=df1.query(""+test7+"==1 & 군별=='해병'")
    st.dataframe(df14,width=800)
page_names_to_funcs = {
"직업선호도 유형":emp_hg,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()