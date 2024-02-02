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
    query = "SELECT * FROM " + t
    conn = create_connection("mydatabase.db")
    query_result = conn.execute(query)
    cols = [column[0] for column in query_result.description]
    results_df = pd.DataFrame.from_records(data=query_result.fetchall(), columns=cols)
    conn.close()
    return results_df

def gstg1(txt1,txt2,txt3,txt4):
    query = "select distinct b.군사특기 from "+txt1+" a,직간접 b where a.군구분='"+txt2+"' and b.군별='"+txt2+"' and a.검사구분코드=b.관련분야코드 and b.직간접구분='"+txt3+"' and a.검사지침코드명='"+txt4+"'"
    conn = create_connection("mydatabase.db")
    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_df 
def gstg2(txt1,txt2,txt3,txt4,txt5):
    query = "select distinct b.군사특기,c.입영월,c.커트라인,c.선발인원 from "+txt1+" a,직간접 b,"+txt5+" c where a.군구분='"+txt2+"' and b.군별='"+txt2+"' and a.검사구분코드=b.관련분야코드 and b.직간접구분='"+txt3+"' and a.검사지침코드명='"+txt4+"' and b.군사특기=c.특기 and c.입영월=(select max(k.입영월) from "+txt5+" k where k.특기=c.특기)      "
    conn = create_connection("mydatabase.db")
    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_df 
def code_query(q):
    query = "select * from 특기코드 where 코드 like '"+q+"%'"
    conn = create_connection("mydatabase.db")
    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_code= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_code  
def emp1_query(t):
    query = "SELECT distinct * FROM " + t
    conn = create_connection("mydatabase.db")
    query_result = conn.execute(query)
    cols = [column[0] for column in query_result.description]
    results_df = pd.DataFrame.from_records(data=query_result.fetchall(), columns=cols)
    conn.close()
    return results_df
def emp_query(q):
    query = "select * from emp1 where 학교명='"+q+"%'"
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