import streamlit as st
import pandas as pd
import numpy as np
import csv



st.title('나의 점수 미리알아보기')

test=st.selectbox('군을 선택해주세요',('','육군(기술행정병)', '해군(기술병)', '공군(기술병)','해병대(기술병)'))
if test == "육군(기술행정병)":
  test1=pd.read_csv('군사특기_육군.csv',encoding='utf-8')
  test1.columns = ['특기번호','특기1','특기2']
  genre = st.radio("2023년 입영유무를 선택하세요",('전체', '2023년 입영계획 있음'))
  if genre == '전체':
    test1=st.selectbox('군사특기를 선택하세요',(test1['특기1']))
  else:
    test1=st.selectbox('군사특기를 선택하세요',(test1['특기2']))
elif test == "해군(기술병)":
  test2=pd.read_excel('군사특기_해군.xls')
  test3=st.selectbox('군사특기를 선택하세요',(test2))
elif test == "공군(기술병)":
  test2=pd.read_excel('군사특기_해군.xls',sheet_name='군사특기_공군')
  test3=st.selectbox('군사특기를 선택하세요',(test2))
else:
    st.title(test)




