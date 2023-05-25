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



def run_query():
    query = "select 입영월,접수인원,지원인원 from gunsa1 where 군사특기명='장갑차조종'"
    query1 = "select 입영월,지원인원 from gunsa1 where 군사특기명='장갑차조종'"
    conn = create_connection("mydatabase.db")


    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )
   #results_df.drop(results_df.columns[-1],axis=1,inplace=True)
  #  results_df.set_index(['입영월'],inplace=True)
    st.dataframe(results_df)
   # st.line_chart(data=pd.DataFrame(results_df),  width=0, height=0, use_container_width=True)
    #   Create a chart with annotations
    restult1=results_df.melt('입영월', var_name='company', value_name='price')
    st.dataframe(restult1)

    c = alt.Chart(pd.DataFrame(restult1)).mark_line(point=True).encode(
        alt.Y('price:Q'),
        x='입영월:N',
        color='company:N'
    ).interactive()
    st.altair_chart(c.interactive(),
    use_container_width=True)
run_query()
