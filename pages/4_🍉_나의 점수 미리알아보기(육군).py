import streamlit as st
import pandas as pd
from PIL import Image
import sqlite3
import altair as alt

st.set_page_config(
  page_icon="😆",
  page_title="대구병역진로설계지원센터",
)

index = ['배점']
gstg6=['선택하세요','국가기술자격증(기사이상)','국가기술자격증(산업기사)','국가기술자격증(기능사)','일학습병행자격증(L6,L5)','일학습병행자격증(L4,L3)','일학습병행자격증(L2)','일반자격증(공인)',
       '일반자격증(일반)','자격증 미소지']
columns1 = {'기술자격·면허': [50],'전공학과': [40],'출결상황': [10],'가산점': [15]}
columns2 = {'기술자격·면허': [90],'출결상황': [10],'가산점': [15]}
index1 = ['국가기술자격증','국가기술자격증','국가기술자격증','일학습병행자격증','일학습병행자격증','일학습병행자격증','일반자격증','일반자격증','자격증 미소지']
columns3 = {'자격등급': ['기사이상','산업기사','기능사','L6, L5','L4, L3','L2','공인','일반',''],'직접관련': [50,45,40,50,45,40,30,26,20],'간접관련': [40,35,30,40,35,30,25,25,20]}
index01 = ['선택하세요','대형/특수','1종보통','2종보통']
sum1=0
sum2=0
sum3=0
sum4=0
sumtotal=0
license1=''
license2=''

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        st.write(e)
    return conn

def gunsa1_query():
    query = "select distinct 군사특기명 from 군사특기별현황"
    conn = create_connection("mydatabase.db")

    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    tes=st.selectbox('군사특기를 선택하세요',results_df)
    return tes

st.header("나의 점수 미리알아보기")
test1=gunsa1_query()

def jeomsu_query(a,b):
    query = "select 점수 from 점수계산 where 구분='"+a+"' and 자격증구분='"+b+"'"
    conn = create_connection("mydatabase.db")

    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df1= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    sum1=int(results_df1.values)

    return sum1

def run_query(a1):

    query = "select 입영월,접수인원,지원인원,커트라인 from 군사특기별현황 where 군사특기명='"+a1+"' and 입영부대='육군훈련소'"
    conn = create_connection("mydatabase.db")

    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )
    restult1=results_df.melt('입영월', var_name='구분', value_name='인원/점수')
    results_df.set_index(['입영월'],inplace=True)
    results_df.T
    c = alt.Chart(pd.DataFrame(restult1)).mark_line(point=True).encode(
        alt.Y('인원/점수:Q'),
        x='입영월:N',
        color='구분:N'
    ).interactive()
    st.altair_chart(c.interactive(),
    use_container_width=True)



if test1=='수송운용(차량운전)':
  st.markdown(f":blue[{test1}]")
  df = pd.DataFrame(columns2, index=index)
  st.table(df)
  st.markdown("1.운전면허증 배점 90점 :대형/특수 : 90점, 1종보통 : 87점, 2종보통 : 85점")
  license = st.selectbox('운전면허증을 선택하세요',(index01))
  if license=='대형/특수':
    sum1=90
  elif license=='1종보통':
    sum1=87
  elif license=='2종보통':
    sum1=85
  else:
    sum1=0
  if test1!='' and sum1!=0 :
    sum2_a=st.markdown(f"1. :green[{sum1}]점")
    st.markdown("3. 출결상황/배점 10점")
    image3=st.image(Image.open('3.png'))
    conn = create_connection("mydatabase.db")
    query = conn.execute("select 자격증구분 from 점수계산 where 구분='결석일'")
    cols = [column[0] for column in query.description]
    results_df1= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols)  
    gylsuk=st.selectbox('결석일자를 선택하세요',results_df1)
    sum3=jeomsu_query('결석일',gylsuk)

    if test1!='' and sum1!=0 and sum3!=0:
      image3.empty()
      sum2_a.empty()
      sum3_a=st.markdown(f"1. :green[{sum1}]점,2. :green[{sum3}]점")
      st.markdown("4. 가산점/배점 15점(접수마감일 기준)")
      image4=st.image(Image.open('5_1.png'))
      image5=st.image(Image.open('5_2.png'))


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

      query = conn.execute("select 자격증구분 from 점수계산 where 구분='헌혈'")
      cols = [column[0] for column in query.description]
      results_df1= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols)  
      blood1=st.selectbox('헌혈횟수를 선택하세요',results_df1)
      sum41=jeomsu_query('헌혈',blood1)

      query = conn.execute("select 자격증구분 from 점수계산 where 구분='봉사시간'")
      cols = [column[0] for column in query.description]
      results_df1= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols)  
      blood2=st.selectbox('봉사시간을 선택하세요',results_df1)
      sum42=jeomsu_query('봉사시간',blood2)
      if sum41+sum42>8 :
          sum4=sum4+8
      else:
          sum4=sum4+sum41+sum42
      if sum4>15:
          sum4=15
      if test1!='' and sum1!=0 and sum3!=0 and sum4>1:
        image4.empty()
        image5.empty()
        sum3_a.empty()
        sumtotal=sum1+sum2+sum3+sum4
        st.subheader(f"1. :green[{sum1}]점,2. :green[{sum3}]점,3. :green[{sum4}]점 합계 : :violet[{sumtotal}]점")
        st.subheader(test1+'(육군훈련소)')
        run_query(test1)
   

elif test1!='수송운용(차량운전)' and test1!='':
  st.markdown(f":blue[{test1}]")
  df = pd.DataFrame(columns1, index=index)
  st.table(df)

  st.markdown("1.기술자격·면허증/배점 50점")
  image1=st.image(Image.open('1.png'))

  col1, col2 = st.columns(2)
  with col1:
    license1 = st.radio(
    "직접/간접관련을 선택하세요.",
    ('직접관련', '간접관련'))
  with col2:
    conn = create_connection("mydatabase.db")
    query = conn.execute("select 자격증구분 from 점수계산 where 구분='직접관련'")

    cols = [column[0] for column in query.description]
    results_df1= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    license2=st.selectbox('자격증구분을 선택하세요',results_df1)

    sum1=jeomsu_query(license1,license2)


  if test1!='' and sum1!=0:
    image1.empty()
    sum1_a=st.markdown(f"1. :green[{sum1}]점")
    st.markdown("2. 전공학과/배점 40점")
    image2=st.image(Image.open('2.png'))
    col1, col2 = st.columns(2)
    with col1:
      hak1 = st.radio("학력구분을 선택하세요.",('대학교', '전문대','고졸','기타'))
    with col2:
      query = conn.execute("select 자격증구분 from 점수계산 where 구분='"+hak1+"'")
      cols = [column[0] for column in query.description]
      results_df1= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols)  
      hak2=st.selectbox('학력구분을 선택하세요',results_df1)
      sum2=jeomsu_query(hak1,hak2)


    if test1!='' and sum1!=0 and sum2!=0:
      image2.empty()
      sum1_a.empty()
      sum2_a=st.markdown(f"1. :green[{sum1}]점,2. :green[{sum2}]점")
      st.markdown("3. 출결상황/배점 10점")
      image3=st.image(Image.open('3.png'))

      query = conn.execute("select 자격증구분 from 점수계산 where 구분='결석일'")
      cols = [column[0] for column in query.description]
      results_df1= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols)  
      gylsuk=st.selectbox('결석일자를 선택하세요',results_df1)
      sum3=jeomsu_query('결석일',gylsuk)

      if test1!='' and sum1!=0 and sum2!=0 and sum3!=0:
        image3.empty()
        sum2_a.empty()
        sum3_a=st.markdown(f"1. :green[{sum1}]점,2. :green[{sum2}]점,3. :green[{sum3}]점")
        st.markdown("4. 가산점/배점 15점(접수마감일 기준)")
        image4=st.image(Image.open('5_1.png'))
        image5=st.image(Image.open('5_2.png'))


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

        query = conn.execute("select 자격증구분 from 점수계산 where 구분='헌혈'")
        cols = [column[0] for column in query.description]
        results_df1= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols)  
        blood1=st.selectbox('헌혈횟수를 선택하세요',results_df1)
        sum41=jeomsu_query('헌혈',blood1)

        query = conn.execute("select 자격증구분 from 점수계산 where 구분='봉사시간'")
        cols = [column[0] for column in query.description]
        results_df1= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols)  
        blood2=st.selectbox('봉사시간을 선택하세요',results_df1)
        sum42=jeomsu_query('봉사시간',blood2)
        if sum41+sum42>8 :
          sum4=sum4+8
        else:
          sum4=sum4+sum41+sum42
        if sum4>15:
          sum4=15


        if test1!='' and sum1!=0 and sum2!=0 and sum3!=0 and sum4>1:
          image4.empty()
          image5.empty()
          sum3_a.empty()
          sumtotal=sum1+sum2+sum3+sum4
          st.subheader(f"1. :green[{sum1}]점,2. :green[{sum2}]점,3. :green[{sum3}]점,4. :green[{sum4}]점 합계 : :violet[{sumtotal}]점")
          st.subheader(test1)
          run_query(test1)
   
