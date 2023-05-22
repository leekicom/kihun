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
st.text('1사단 : 경기 파주시 문산읍 이천리 516(사임당로 492)')
df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='1사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)
st.text('25사단 : 경기도 양주시 남면 매곡리 216-3(휴암로 393-43)')
df_int=df[(df['군사특기명']=='수송운용(차량운전)')  & (df['입영부대']=='25사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)
st.text('28사단 : 경기도 파주시 적성면 적암리 194-8(율곡로 3064)')
df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='28사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)
st.text('3사단 : 강원도 철원군 서면 자등리 402(금강로 7626)')
df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='3사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)
st.text('51사단 : 경기도 화성시 매송면 어천리 220-1(화성로 2337-36)')
df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='51사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)
st.text('55사단 : 경기도 용인시 처인구 포곡읍 포곡로 164')
df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='55사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)
st.text('5사단 : 경기도 연천군 청산면 궁평리 299-1(청창로 474)')
df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='5사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)
st.text('6사단 : 강원도 철원군 동송읍 상노리(상노로 73-26)')
df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='6사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)
st.text('9사단 : 경기도 고양시 일산동구 성석동 612')
df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='9사단')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)
st.text('육군훈련소 : 충남 논산시 연무읍 득안대로')
df_int=df[(df['군사특기명']=='수송운용(차량운전)') & (df['입영부대']=='육군훈련소')]
st.dataframe(df_int, width=640)
st.line_chart(data=pd.DataFrame(df_int), x='입영월', y='총점', width=0, height=0, use_container_width=True)

