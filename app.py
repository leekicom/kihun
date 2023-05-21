import streamlit as st
import pandas as pd



st.title('나의 점수 미리알아보기')

test=st.selectbox('군을 선택해주세요',('','육군(기술행정병)', '해군(기술병)', '공군(기술병)','해병대(기술병)'))
test1=''
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
elif test == "해병대(기술병)":
  test4=st.selectbox('군사특기를 선택하세요',(gstg5))
else:
  st.text(test)

index = ['배점']
columns1 = {'기술자격·면허': [50],'전공학과': [40],'출결상황': [10],'가산점': [15]}
columns2 = {'기술자격·면허': [90],'출결상황': [10],'가산점': [15]}

if test1=='수송운용(차량운전)':
  st.title(test1)
  df = pd.DataFrame(columns2, index=index)
  st.table(df)
else:
  st.title(test1)
  df = pd.DataFrame(columns1, index=index)
  st.table(df)





