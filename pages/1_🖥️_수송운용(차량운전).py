import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import sqlite3

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

def gunsa1_query():
    query = "select 입영월,입영부대,접수인원,지원인원,커트라인 from 군사특기별현황 where 군사특기명='수송운용(차량운전)' and 입영월<>'2023년9월'"
    conn = create_connection("mydatabase.db")

    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_df
df1=gunsa1_query()

df2=df1.drop(['접수인원', '지원인원'], axis=1)


c = alt.Chart(pd.DataFrame(df2)).mark_line(point=True).encode(
        alt.Y('커트라인:Q',scale=alt.Scale(domain=[90, 115])),
        x='입영월:N',
        color='입영부대:N'
    ).interactive()

# restult1=df2.melt('입영월', var_name='구분', value_name='인원/점수')

# c = alt.Chart(pd.DataFrame(restult1)).mark_line(point=True).encode(
#         alt.Y('인원/점수:Q'),
#         x='입영월:N',
#         color='구분:N'
#     ).interactive()
# st.altair_chart(c.interactive(),
#     use_container_width=True)

df4=df1.set_index(['입영월'],inplace=True)

st.header("수송운용(차량운전) 입영부대별 현황")
#st.line_chart(data=pd.DataFrame(df1),  width=0, height=0, use_container_width=True)
st.altair_chart(c.interactive(),
    use_container_width=True)

st.text('1사단 : 경기 파주시 문산읍 이천리 516(사임당로 492)  ')
df_int=df1[df1['입영부대']=="1사단"]
if st.button('열기(1사단)'):
  df_1=st.dataframe(df_int, width=640)

st.text('25사단 : 경기도 양주시 남면 매곡리 216-3(휴암로 393-43)')
df_int=df1[df1['입영부대']=="25사단"]
if st.button('열기(25사단)'):
  df_1=st.dataframe(df_int, width=640)

st.text('28사단 : 경기도 파주시 적성면 적암리 194-8(율곡로 3064)')
df_int=df1[df1['입영부대']=="28사단"]
if st.button('열기(28사단)'):
  df_1=st.dataframe(df_int, width=640)

st.text('3사단 : 강원도 철원군 서면 자등리 402(금강로 7626)')
df_int=df1[df1['입영부대']=="3사단"]
if st.button('열기(3사단)'):
  df_1=st.dataframe(df_int, width=640)

st.text('51사단 : 경기도 화성시 매송면 어천리 220-1(화성로 2337-36)')
df_int=df1[df1['입영부대']=="51사단"]
if st.button('열기(51사단)'):
  df_1=st.dataframe(df_int, width=640)

st.text('55사단 : 경기도 용인시 처인구 포곡읍 포곡로 164')
df_int=df1[df1['입영부대']=="55사단"]
if st.button('열기(55사단)'):
  df_1=st.dataframe(df_int, width=640)

st.text('5사단 : 경기도 연천군 청산면 궁평리 299-1(청창로 474)')
df_int=df1[df1['입영부대']=="5사단"]
if st.button('열기(5사단)'):
  df_1=st.dataframe(df_int, width=640)

st.text('6사단 : 강원도 철원군 동송읍 상노리(상노로 73-26)')
df_int=df1[df1['입영부대']=="6사단"]
if st.button('열기(6사단)'):
  df_1=st.dataframe(df_int, width=640)

st.text('9사단 : 경기도 고양시 일산동구 성석동 612')
df_int=df1[df1['입영부대']=="9사단"]
if st.button('열기(9사단)'):
  df_1=st.dataframe(df_int, width=640)

st.text('육군훈련소 : 충남 논산시 연무읍 득안대로')
df_int=df1[df1['입영부대']=="육군훈련소"]
if st.button('열기(육군훈련소)'):
  df_1=st.dataframe(df_int, width=640)


