import sqlite3
import streamlit as st
import pandas as pd
import altair as alt
import os


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        st.write(e)
    return conn

def gun_query():
    query = "select * from 군사특기별현황"
    conn = create_connection("mydatabase.db")
    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_df
df1=gun_query()

col1, col2 = st.columns(2) 
with col1:
    test1=st.selectbox('군사특기를 선택하세요',df1['군사특기명'].drop_duplicates(keep='first'),0)
with col2:
    test2=st.selectbox('입영부대를 선택하세요',df1['입영부대'].drop_duplicates(keep="first"),0)
df2=df1.query("군사특기명=='"+test1+"' & 입영부대=='"+test2+"' ")
restult1=df2[['입영월','접수인원','지원인원','커트라인']]
restult2=restult1.melt('입영월', var_name='구분', value_name='인원/점수')
restult1.set_index(['입영월'],inplace=True)
restult1.T

c = alt.Chart(pd.DataFrame(restult2)).mark_line(point=True).encode(
        alt.Y('인원/점수:Q'),
        x='입영월:N',
        color='구분:N'
    ).interactive()
st.altair_chart(c.interactive(),
    use_container_width=True)
