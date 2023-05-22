import streamlit as st
import pandas as pd

st.set_page_config(
  page_icon="😆",
  page_title="대구병역진로설계지원센터",
)

df=pd.read_excel('육군.xlsx','합격점수')

# df_int=df[(df['군사특기명']=='수송운용(차량운전)')]
# st.dataframe(df_int, width=640)
# st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점',columns=['1사단','25사단'], width=0, height=0, use_container_width=True)

#df_int=df[(df['군사특기명'].str.contains('수송운용')) & (df['입영부대']=='1사단')]
df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='1사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)

df_int=df[(df['군사특기명']=='수송운용(차량운전)')  & (df['입영부대']=='25사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)

df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='28사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)

df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='3사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)

df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='51사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)

df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='55사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)

df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='5사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)

df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='6사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)

df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='9사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)

df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='육군훈련소')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)

