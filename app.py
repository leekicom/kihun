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
sum2=0
sum3=0
sum4=0

license1=''
license2=''
index01 = ['선택하세요','대형/특수','1종보통','2종보통']

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
  st.subheader("1.운전면허증 배점 90점 :대형/특수 : 90점, 1종보통 : 87점, 2종보통 : 85점")
  license = st.selectbox('운전면허증을 선택하세요',(index01))
  if license=='대형/특수':
    sum1=90
  elif license=='1종보통':
    sum1=87
  elif license=='2종보통':
    sum1=85
  else:
    sum1=0
  if test1!='' and sum1!=0:
    st.subheader(f"1. :green[{sum1}]점")
    st.subheader("2. 출결상황/배점 10점")
    image = Image.open('3.png')
    st.image(image)
    day = st.selectbox('결석일자를 선택하세요',('선택하세요','0일','1-2일','3-4일','5-6일','7일이상'))
    if day=='0일' :
      sum3=10
    elif day=='1-2일' :
      sum3=9
    elif day=='3-4일' :
      sum3=8
    elif day=='5-6일' :
      sum3=7
    elif day=='7일이상' :
      sum3=6
    else :
      sum3=0
    if test1!='' and sum1!=0 and sum3!=0:
      st.subheader(f"1. :green[{sum1}]점,2. :green[{sum3}]점")
      st.subheader("3. 가산점/배점 15점(접수마감일 기준)")
      image1 = Image.open('5_1.png')
      image2 = Image.open('5_2.png')
      st.image(image1)
      st.image(image2)   
      options = st.multiselect(
      '가산점이 있으면 추가하세요.',['병역진로설계 지원자','다자녀(3) 가정 자녀','다자녀(2) 가정 자녀','모집특기경력(6월~1년 미만)','모집특기경력(1년~2년 미만)','모집특기경력(2년 이상)',
                        '질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자','독립유공자 손·자녀 또는 국가유공자 자녀', '생계급여 수급권자'],['병역진로설계 지원자'])


      for i in options:
        if i in ('독립유공자 손·자녀 또는 국가유공자 자녀','생계급여 수급권자','다자녀(3) 가정 자녀','질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자'):
          sum4=sum4+4
        elif i in ('모집특기경력(2년 이상)'):
          sum4=sum4+3
        elif i in ('다자녀(2) 가정 자녀','모집특기경력(1년~2년 미만)'):
          sum4=sum4+2
        else :
          sum4=sum4+1
        col1, col2 = st.columns(2)
        with col1:
          blood1 = st.radio("헌혈/봉사를 선택하세요.",('헌혈', '봉사'))
        with col2:
          if blood1=='헌혈':
            blood2 = st.selectbox('헌혈횟수를 선택하세요',('선택하세요','1회','2회','3회','4회','5회','6회','7회','8회이상'))
          elif blood1=='봉사':
            blood2 = st.selectbox('봉사시간을 선택하세요',('선택하세요','8~15시간','16~23시간','24~31시간','32~39시간','40~47시간','48~55시간','56~63시간','64시간이상'))  
        if blood2=='8회이상' or  blood2=='64시간이상':
          sum4=sum4+8
        elif blood2=='7회' or  blood2=='56~63시간':
          sum4=sum4+7
        elif blood2=='6회' or  blood2=='48~55시간':
          sum4=sum4+6
        elif blood2=='5회' or  blood2=='40~47시간':
          sum4=sum4+5
        elif blood2=='4회' or  blood2=='32~39시간':
          sum4=sum4+4
        elif blood2=='3회' or  blood2=='24~31시간':
          sum4=sum4+3
        elif blood2=='2회' or  blood2=='16~23시간':
          sum4=sum4+2
        elif blood2=='1회' or  blood2=='8~15시간':
          sum4=sum4+1
        else :
          sum4=sum4+0
        if sum4>15:
          sum4=15
        sumtotal=sum1+sum3+sum4
        st.subheader(f"1. :green[{sum1}]점,2. :green[{sum3}]점,3. :green[{sum4}]점 합계 : :violet[{sumtotal}]점")

        df=pd.read_excel('육군.xlsx','합격점수')
        int_line=df['군사특기명'].str.contains(test1)
        df_int=df[int_line]
        st.dataframe(df_int)
        chart_data = pd.DataFrame(df_int)
        st.line_chart(data=chart_data, x='입영월', y='총점', width=640, height=0, use_container_width=True)





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
  elif license1=='직접관련' and license2=='선택하세요':
    sum1=0
  else:
    sum1=20
  if test1!='' and sum1!=0:
    st.subheader(f"1. :green[{sum1}]점")
    st.subheader("2. 전공학과/배점 40점")
    image = Image.open('2.png')
    st.image(image)
    col1, col2 = st.columns(2)
    with col1:
      hak1 = st.radio("학력구분을 선택하세요.",('대학교', '전문대','고졸','기타'))
    with col2:
      if hak1=='대학교':
        hak2 = st.selectbox('학력을 선택하세요',('선택하세요','4학년 수료이상','4학년 재학','3학년 수료','3학년 재학','2학년 수료','2학년 재학','1학년 수료','1학년 재학'))
      elif hak1=='전문대':
        hak2 = st.selectbox('학력을 선택하세요',('선택하세요','3학년 수료','3학년 재학','2학년 수료','2학년 재학','1학년 수료','1학년 재학'))    
      elif hak1=='고졸':
        hak2 = st.selectbox('학력을 선택하세요',('선택하세요','전공','비전공')) 
      else :
        hak2 = st.selectbox('학력을 선택하세요',('선택하세요','한국폴리텍 2년이상 수료','한국폴리텍 1년이상 수료','한국폴리텍 6개월이상 수료','비전공/고퇴이하','학점은행제 40점이상(학사)',
                          '학점은행제 40점이상(전문학사)','학점은행제 80점이상(학사)','학점은행제 80점이상(전문학사)','학점은행제 120점이상(학사)','학점은행제 120점이상(전문학사)',
                          '학점은행제 140점이상(학사)'))    
      if hak1=='대학교' and hak2=='4학년 수료이상':
        sum2=40
      elif hak1=='대학교' and hak2=='4학년 재학':
        sum2=38
      elif hak1=='대학교' and hak2=='3학년 수료':
        sum2=36
      elif hak1=='대학교' and hak2=='3학년 재학':
        sum2=34
      elif hak1=='대학교' and hak2=='2학년 수료':
        sum2=32
      elif hak1=='대학교' and hak2=='2학년 재학':
        sum2=30
      elif hak1=='대학교' and hak2=='1학년 수료':
        sum2=28
      elif hak1=='대학교' and hak2=='1학년 재학':
        sum2=26
      elif hak1=='전문대' and hak2=='3학년 수료':
        sum2=40
      elif hak1=='전문대' and hak2=='3학년 재학':
        sum2=38
      elif hak1=='전문대' and hak2=='2학년 수료':
        sum2=36
      elif hak1=='전문대' and hak2=='2학년 재학':
        sum2=34
      elif hak1=='전문대' and hak2=='1학년 수료':
        sum2=32
      elif hak1=='전문대' and hak2=='1학년 재학':
        sum2=30
      elif hak1=='고졸' and hak2=='전공':
        sum2=34
      elif hak1=='고졸' and hak2=='비전공':
        sum2=20
      elif hak1=='기타' and hak2=='한국폴리텍 2년이상 수료':
        sum2=32
      elif hak1=='기타' and hak2=='한국폴리텍 1년이상 수료':
        sum2=30
      elif hak1=='기타' and hak2=='한국폴리텍 6개월이상 수료':
        sum2=26
      elif hak1=='기타' and hak2=='비전공/고퇴이하':
        sum2=20
      elif hak1=='기타' and hak2=='학점은행제 40점이상(학사)':
        sum2=28
      elif hak1=='기타' and hak2=='학점은행제 40점이상(전문학사)':
        sum2=32
      elif hak1=='기타' and hak2=='학점은행제 80점이상(학사)':
        sum2=32
      elif hak1=='기타' and hak2=='학점은행제 80점이상(전문학사)':
        sum2=36
      elif hak1=='기타' and hak2=='학점은행제 120점이상(학사)':
        sum2=36
      elif hak1=='기타' and hak2=='학점은행제 120점이상(전문학사)':
        sum2=40
      elif hak1=='기타' and hak2=='학점은행제 140점이상(학사)':
        sum2=40
      else :
        sum2=0   
    if test1!='' and sum1!=0 and sum2!=0:
      st.subheader(f"1. :green[{sum1}]점,2. :green[{sum2}]점")
      st.subheader("3. 출결상황/배점 10점")
      image = Image.open('3.png')
      st.image(image)
      day = st.selectbox('결석일자를 선택하세요',('선택하세요','0일','1-2일','3-4일','5-6일','7일이상'))
      if day=='0일' :
        sum3=10
      elif day=='1-2일' :
        sum3=9
      elif day=='3-4일' :
        sum3=8
      elif day=='5-6일' :
        sum3=7
      elif day=='7일이상' :
        sum3=6
      else :
        sum3=0
      if test1!='' and sum1!=0 and sum2!=0 and sum3!=0:
        st.subheader(f"1. :green[{sum1}]점,2. :green[{sum2}]점,3. :green[{sum3}]점")
        st.subheader("4. 가산점/배점 15점(접수마감일 기준)")
        image1 = Image.open('5_1.png')
        image2 = Image.open('5_2.png')
        st.image(image1)
        st.image(image2)   
      options = st.multiselect(
        '가산점이 있으면 추가하세요.',['병역진로설계 지원자','다자녀(3) 가정 자녀','다자녀(2) 가정 자녀','모집특기경력(6월~1년 미만)','모집특기경력(1년~2년 미만)','모집특기경력(2년 이상)',
                        '질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자','독립유공자 손·자녀 또는 국가유공자 자녀', '생계급여 수급권자'],['병역진로설계 지원자'])


      for i in options:
        if i in ('독립유공자 손·자녀 또는 국가유공자 자녀','생계급여 수급권자','다자녀(3) 가정 자녀','질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자'):
          sum4=sum4+4
        elif i in ('모집특기경력(2년 이상)'):
          sum4=sum4+3
        elif i in ('다자녀(2) 가정 자녀','모집특기경력(1년~2년 미만)'):
          sum4=sum4+2
        else :
          sum4=sum4+1
        blood1 = st.selectbox('헌혈횟수를 선택하세요',('선택하세요','1회','2회','3회','4회','5회','6회','7회','8회이상'))
        blood2 = st.selectbox('봉사시간을 선택하세요',('선택하세요','8~15시간','16~23시간','24~31시간','32~39시간','40~47시간','48~55시간','56~63시간','64시간이상')) 
        sum41=0
        sum42=0
        if blood1=='8회이상':
          sum41=sum41+8
        elif blood2=='64시간이상':
          sum42=sum42+8
        elif blood1=='7회':
          sum41=sum41+7
        elif blood2=='56~63시간':
          sum42=sum42+7    
        elif blood1=='6회':
          sum41=sum41+6
        elif blood2=='48~55시간':
          sum42=sum42+6
        elif blood1=='5회':
          sum41=sum41+5
        elif blood2=='40~47시간':
          sum42=sum42+5
        elif blood1=='4회':
          sum41=sum41+4
        elif blood2=='32~39시간':
          sum42=sum42+4
        elif blood1=='3회':
          sum41=sum41+3
        elif blood2=='24~31시간':
          sum42=sum42+3
        elif blood1=='2회':
          sum41=sum41+2
        elif blood2=='16~23시간':
          sum42=sum42+2
        elif blood1=='1회':
          sum41=sum41+1
        elif blood2=='8~15시간':
          sum42=sum42+1
        else :
          sum41=sum41+0
          sum42=sum42+0
        if sum41+sum42>8:
          sum4=sum4+8
        else:
          sum4=sum4+sum41+sum42
        if sum4>15:
          sum4=15
        sumtotal=sum1+sum2+sum3+sum4
        st.subheader(f"1. :green[{sum1}]점,2. :green[{sum2}]점,3. :green[{sum3}]점,4. :green[{sum4}]점 합계 : :violet[{sumtotal}]점")

        df=pd.read_excel('육군.xlsx','합격점수')
        int_line=df['군사특기명'].str.contains(test1)
        df_int=df[int_line]
        st.dataframe(df_int)
        chart_data = pd.DataFrame(df_int)
        st.line_chart(data=chart_data, x='입영월', y='총점', width=640, height=0, use_container_width=True)
