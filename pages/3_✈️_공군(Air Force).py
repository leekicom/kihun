import sqlite3
import streamlit as st
import pandas as pd
import altair as alt
import os
import mod2
from PIL import Image

st.set_page_config(
  page_icon="😆",
  page_title="대구병역진로설계지원센터",
)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        st.write(e)
    return conn
def code_query():
    query = "select * from 특기코드 where 코드 like 'A%'"
    conn = create_connection("mydatabase.db")
    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_code= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_code      
def gun_query():
    query = "select * from 공군특기별현황"
    conn = create_connection("mydatabase.db")
    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_df
def air_force_hh():
    st.header("공군 군사특기별 현황")
    df1=gun_query()
    code_df=code_query()
    test1=st.selectbox('군사특기를 선택하세요',code_df['소분류'].drop_duplicates(keep='first'),0)

    df3=code_df.query("소분류=='"+test1+"'")
    result3=df3['대분류'].values
    result4=df3['코드'].values
    txt3=''.join(result3)
    txt4=''.join(result4)
    st.text("대분류:"+txt3)
    df2=df1.query("특기=='"+txt3+"'")
    restult1=df2[['입영월','커트라인','선발인원']]
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
    
    code1_txt1=sogae_query(txt4)
    mod2_html=''.join(code1_txt1['Column2'].values)
    try:
        image = Image.open('image/'+txt4+'.jpeg')
    except: 
        image = Image.open('image/'+txt4+'.gif')    
    st.image(image, caption=txt4)
    st.markdown(mod2_html, unsafe_allow_html=True)
def sogae_query(b):
    query = "select Column2 from 군사특기소개 where Column1='"+b+"'"
    conn = create_connection("mydatabase.db")
    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_df       
def air_force_jeomsu():
    df1=gun_query()
page_names_to_funcs = {
    "군사특기별 현황": air_force_hh,
    "나의점수 알아보기": air_force_jeomsu,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()