import streamlit as st
import pandas as pd

st.set_page_config(
  page_icon="😆",
  page_title="대구병역진로설계지원센터",
)

df=pd.read_excel('육군.xlsx','합격점수')

#df_int=df[(df['군사특기명'].str.contains('수송운용')) & (df['입영부대']=='1사단')]
df_int=df[df['입영부대']=='1사단']
st.dataframe(df_int)
chart_data = pd.DataFrame(df_int)
st.line_chart(data=chart_data, x='입영월', y='총점', width=0, height=0, use_container_width=True)

