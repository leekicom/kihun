import streamlit as st
import pandas as pd
import numpy as np
import csv



st.title('나의 점수 미리알아보기')

test=st.selectbox('군을 선택해주세요',('','육군(기술행정병)', '해군(기술병)', '공군(기술병)','해병대(기술병)'))
gstg1=pd.read_excel('군사특기.xlsx','군사특기_육군1')
gstg2=pd.read_excel('군사특기.xlsx','군사특기_육군2')
gstg3=pd.read_excel('군사특기.xlsx','군사특기_해군')
gstg4=pd.read_excel('군사특기.xlsx','군사특기_공군')
gstg5=pd.read_excel('군사특기.xlsx','군사특기_해병대')
if test == "육군(기술행정병)":
  genre = st.radio("2023년 입영유무를 선택하세요",('전체', '2023년 입영계획 있음'))
  if genre == '전체':
    test1=st.selectbox('군사특기를 선택하세요',(gstg1))
  else:
    test1=st.selectbox('군사특기를 선택하세요',(gstg2))
elif test == "해군(기술병)":
  test2=st.selectbox('군사특기를 선택하세요',(gstg3))
elif test == "공군(기술병)":
  test3=st.selectbox('군사특기를 선택하세요',(gstg4))
else:
  test4=st.selectbox('군사특기를 선택하세요',(gstg5))




