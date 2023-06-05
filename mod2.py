import sqlite3
import streamlit as st
import pandas as pd


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        st.write(e)
    return conn
def gun1_query(t):
    query = "select * from "+t+""
    conn = create_connection("mydatabase.db")
    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_df 
def gstg1(txt,txt1,txt2):
    query = "select distinct b.군사특기 from "+txt+" a,직간접 b where a.군구분='해군' and a.검사구분코드=b.관련분야코드 and b.직간접구분='"+txt1+"' and a.검사지침코드명='"+txt2+"'"
    conn = create_connection("mydatabase.db")
    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_df 
def code_query():
    query = "select * from 특기코드 where 코드 like 'M%'"
    conn = create_connection("mydatabase.db")
    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_code= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_code  
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
def jeomsu_query(a,b):
    query = "select 점수 from 공군점수계산 where 구분='"+a+"' and 자격증구분='"+b+"'"
    conn = create_connection("mydatabase.db")

    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df1= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    sum1=int(results_df1.values)
    return sum1