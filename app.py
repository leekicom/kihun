import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
  page_icon="😆",
  page_title="대구병역진로설계지원센터",
)


st.header("나의 점수 미리알아보기")

test=st.selectbox('군을 선택해주세요',('','육군(기술행정병)', '해군(기술병)', '공군(기술병)','해병대(기술병)'))
test1=''
gstg1=pd.read_excel('군사특기.xlsx','군사특기_육군1')
gstg2=pd.read_excel('군사특기.xlsx','군사특기_육군2')
gstg3=pd.read_excel('군사특기.xlsx','군사특기_해군')
gstg4=pd.read_excel('군사특기.xlsx','군사특기_공군')
gstg5=pd.read_excel('군사특기.xlsx','군사특기_해병대')
gstg6=pd.read_excel('군사특기.xlsx','기술자격·면허증')
index = ['배점']
columns1 = {'기술자격·면허': [50],'전공학과': [40],'출결상황': [10],'가산점': [15]}
columns2 = {'기술자격·면허': [90],'출결상황': [10],'가산점': [15]}
index1 = ['국가기술자격증','국가기술자격증','국가기술자격증','일학습병행자격증','일학습병행자격증','일학습병행자격증','일반자격증','일반자격증','자격증 미소지']
columns3 = {'자격등급': ['기사이상','산업기사','기능사','L6, L5','L4, L3','L2','공인','일반',''],'직접관련': [50,45,40,50,45,40,30,26,20],'간접관련': [40,35,30,40,35,30,25,25,20]}
sum1=0
license1=''
license2=''


if test == "육군(기술행정병)":
  col1, col2 = st.columns(2)

  with col1:
    genre = st.checkbox("전체(2023년 입영유무 포함)", key="disabled")
  with col2:
    if  genre == True:
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

if test1=='수송운용(차량운전)':
  st.subheader(f":blue[{test1}]")
  df = pd.DataFrame(columns2, index=index)
  st.table(df)
elif test1!='수송운용(차량운전)' and test1!='':
  st.subheader(f":blue[{test1}]")
  df = pd.DataFrame(columns1, index=index)
  st.table(df)

  st.subheader("1.기술자격·면허증/배점 50점")
  image = Image.open('1.png')
  st.image(image)

  col1, col2 = st.columns(2)
  with col1:
    license1 = st.radio(
    "직접/간접관련을 선택하세요.",
    ('직접관련', '간접관련'))
  with col2:
    license2 = st.selectbox('기술자격·면허증을 선택하세요',(gstg6))
else:
  st.text(test)
if license1=='직접관련' and license2=='국가기술자격증(기사이상)':
  sum1=50
elif license1=='간접관련' and license2=='국가기술자격증(기사이상)':
  sum1=40
elif license1=='직접관련' and license2=='국가기술자격증(산업기사)':
  sum1=45
elif license1=='간접관련' and license2=='국가기술자격증(산업기사)':
  sum1=35
elif license1=='직접관련' and license2=='국가기술자격증(기능사)':
  sum1=40
elif license1=='간접관련' and license2=='국가기술자격증(기능사)':
  sum1=30
elif license1=='직접관련' and license2=='일학습병행자격증(L6,L5)':
  sum1=50
elif license1=='간접관련' and license2=='일학습병행자격증(L6,L5)':
  sum1=40
elif license1=='직접관련' and license2=='일학습병행자격증(L4,L3)':
  sum1=45
elif license1=='간접관련' and license2=='일학습병행자격증(L4,L3)':
  sum1=35
elif license1=='직접관련' and license2=='일학습병행자격증(L2)':
  sum1=40
elif license1=='간접관련' and license2=='일학습병행자격증(L2)':
  sum1=30
elif license1=='직접관련' and license2=='일반자격증(공인)':
  sum1=30
elif license1=='간접관련' and license2=='일반자격증(공인)':
  sum1=25
elif license1=='직접관련' and license2=='일반자격증(일반)':
  sum1=26
elif license1=='간접관련' and license2=='일반자격증(일반)':
  sum1=25
else:
  sum1=20
if test1!='':
  if st.button('다음'):
    st.subheader(f"1. :green[{sum1}]점")
    st.subheader("2. 전공학과/배점 40점")
    image = Image.open('2.png')
    st.image(image)
  col1, col2 = st.columns(2)
  with col1:
    hak1 = st.radio("학력구분을 선택하세요.",('대학교', '전문대','고졸','기타'))
  with col2:
    if hak1=='대학교':
      hak2 = st.selectbox('학력을 선택하세요',('4학년 수료이상','4학년 재학','3학년 수료','3학년 재학','2학년 수료','2학년 재학','1학년 수료','1학년 재학'))
    elif hak1=='전문대':
      hak2 = st.selectbox('학력을 선택하세요',('3학년 수료','3학년 재학','2학년 수료','2학년 재학','1학년 수료','1학년 재학'))        