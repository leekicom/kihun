import sqlite3
import base64
import streamlit as st
import mod2
import pandas as pd
import altair as alt
def mjgh():
    df1=mod2.gun1_query('모집계획')
    st.header('군별 모집계획')
    test1=st.selectbox('구분',df1['구분'].drop_duplicates(keep='first'),0)
    st.subheader(test1)
    df2=df1.query("구분=='"+test1+"'")
    result=df2[['모집회차','입영월','지원서접수','1차발표','신검/면접','최종발표']]
    result.set_index(['모집회차'],inplace=True)
    st.dataframe(result)
def mjhh():
    st.header("모집현황")
    df1 = mod2.gun1_query('hh2')
    test1 = st.selectbox('군을 선택하세요', df1['군별'].drop_duplicates(keep='first'), 0)
    df2 = df1.query("군별 == '" + test1 + "'")
    test2 = st.selectbox('군사특기를 선택하세요', df2['군사특기명'].drop_duplicates(keep='first'), 0)
    df3 = df2.query("군사특기명 == '" + test2 + "'")

    result1 = df3[['입영월', '접수인원', '지원인원', '커트라인']]
    result2 = result1.melt(id_vars='입영월', var_name='구분', value_name='인원/점수')
    result1.set_index('입영월', inplace=True)  # '입영월'을 인덱스로 설정
    st.dataframe(result1)

    c = alt.Chart(pd.DataFrame(result2)).mark_line(point=True).encode(
        alt.Y('인원/점수:Q'),
        x='입영월:N',
        color='구분:N'
    ).interactive()
    st.altair_chart(c.interactive(), use_container_width=True)


def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
def yg_jmtg():
    show_pdf('jmtg.pdf')
page_names_to_funcs = {
    "모집계획": mjgh,
    "모집현황": mjhh,
    "육군전문특기": yg_jmtg,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()