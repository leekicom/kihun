import sqlite3
import streamlit as st
import pandas as pd
import altair as alt
import os
import mod2
from PIL import Image

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        st.write(e)
    return conn
  
def gun_query():
    query = "select * from 해병대특기별현황"
    conn = create_connection("mydatabase.db")
    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_df
def marine_hh():
    st.header("해병대 군사특기별 현황")
    df1=gun_query()
    test1=st.selectbox('군사특기를 선택하세요',df1['특기'].drop_duplicates(keep='first'),0)
    df2=df1.query("특기=='"+test1+"'")
    restult1=df2[['입영월','1차','최종']]
    restult2=restult1.melt('입영월', var_name='구분', value_name='점수')
    restult1.set_index(['입영월'],inplace=True)
    restult1.T
    c = alt.Chart(pd.DataFrame(restult2)).mark_line(point=True).encode(
        alt.Y('점수:Q'),
        x='입영월:N',
        color='구분:N'
    ).interactive()
    st.altair_chart(c.interactive(),
        use_container_width=True)
def marine_jeomsu():
    df1=0
page_names_to_funcs = {
    "군사특기별 현황": marine_hh,
    "나의점수 알아보기": marine_jeomsu,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()