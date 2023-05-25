import sqlite3
import streamlit as st
import pandas as pd
import altair as alt
import os


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        st.write(e)

    return conn
def gunsa_query():
    query = "select distinct 군사특기명 from 군사특기별현황"
    query1 = "select distinct 입영부대 from 군사특기별현황"
    conn = create_connection("mydatabase.db")

    query = conn.execute(query)
    query1 = conn.execute(query1)
    cols = [column[0] for column in query.description]
    cols1 = [column[0] for column in query1.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    results_df1= pd.DataFrame.from_records(
                data = query1.fetchall(), 
                columns = cols1
            ) 
    col1, col2 = st.columns(2) 
    with col1:
        test1=st.selectbox('군사특기를 선택하세요',results_df)
    with col2:
        test2=st.selectbox('입영부대를 선택하세요',(results_df1))

    return test1,test2
def run_query(a1,a2):

    query = "select 입영월,접수인원,지원인원,커트라인 from 군사특기별현황 where 군사특기명='"+a1+"' and 입영부대='"+a2+"'"
    #query1 = "select 입영월,지원인원 from gunsa1 where 군사특기명='장갑차조종'"
    conn = create_connection("mydatabase.db")

    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )
    restult1=results_df.melt('입영월', var_name='구분', value_name='인원/점수')
   #results_df.drop(results_df.columns[-1],axis=1,inplace=True)
    results_df.set_index(['입영월'],inplace=True)
    results_df.T
   # st.line_chart(data=pd.DataFrame(results_df),  width=0, height=0, use_container_width=True)
    #   Create a chart with annotations

    #st.dataframe(restult1)

    c = alt.Chart(pd.DataFrame(restult1)).mark_line(point=True).encode(
        alt.Y('인원/점수:Q'),
        x='입영월:N',
        color='구분:N'
    ).interactive()
    st.altair_chart(c.interactive(),
    use_container_width=True)
a1,a2=gunsa_query()
run_query(a1,a2)
