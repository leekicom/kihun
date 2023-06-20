import streamlit as st
import pandas as pd
from PIL import Image
import sqlite3
import altair as alt
import webbrowser
import mod1
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        st.write(e)
    return conn
st.markdown("# Upload Data")
table_name = st.text_input('Table Name to Insert')
conn = create_connection("mydatabase.db")
uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
    try:
        data = pd.read_excel(uploaded_file, sheet_name='기술병')
        cell_value = [['입영월','군별', '군사특기명', '접수인원', '지원인원', '커트라인']]
        for i in range(3, 304):
            for j in range(0, 24):
                if j < 12:
                    month = j + 1
                    row = ['2022년' + str(month) + '월'] + data.iloc[i, [1, 6, j+11, j+35, j+83]].tolist()
                    cell_value.append(row)
                else:
                    month = j - 11
                    row = ['2023년' + str(month) + '월'] + data.iloc[i, [1, 6, j+11, j+35, j+83]].tolist()
                    cell_value.append(row)   

                # 데이터 전처리: 군사특기명 컬럼 수정
        for row in cell_value[1:]:
            row[2] = str(row[2]).replace('\n', '')   

        conn = create_connection("mydatabase.db")
        cursor = conn.cursor()
# 테이블 생성
        cursor.execute("DROP TABLE IF EXISTS "+table_name)
        cursor.execute("CREATE TABLE IF NOT EXISTS "+table_name+" (입영월, 군별, 군사특기명, 접수인원, 지원인원, 커트라인)")
# 데이터 삽입
        for row in cell_value[1:]:
            query = "INSERT INTO "+table_name+" VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(query, row)

        conn.commit()
        conn.close()
        st.write('Data uploaded successfully.')
    except Exception as e:
        st.write(e)



