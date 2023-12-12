import streamlit as st
import pandas as pd
from PIL import Image
import sqlite3
import altair as alt
import webbrowser
import mod1

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
def gstg1(txt,txt1,txt2):
    query = "select distinct c.군사특기명 from "+txt+" a,직간접 b,군사특기코드 c where a.군구분='육군' and a.검사구분코드=b.관련분야코드 and b.군사특기=c.코드 and b.직간접구분='"+txt1+"' and a.검사지침코드명='"+txt2+"'"
    conn = create_connection("mydatabase.db")

    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_df
def gunsa2_query():
    query = "select 입영월,입영부대,접수인원,지원인원,커트라인 from 군사특기별현황 where 군사특기명='수송운용(차량운전)' and 입영월<>'2023년9월'"
    conn = create_connection("mydatabase.db")

    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_df
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
def code_query(a):
    query = "select 코드 from 군사특기코드 where 군사특기명='"+a+"'"
    conn = create_connection("mydatabase.db")
    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_df
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
def jmtg_query(b):
    query = "select 내용 from 전문특기 where 전문특기='"+b+"'"
    conn = create_connection("mydatabase.db")
    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_df    
def gun_query():
    query = "select * from 군사특기별현황"
    conn = create_connection("mydatabase.db")
    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )  
    return results_df
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
def run_queryq(a1):

    query = "select 입영월,접수인원,지원인원,커트라인 from hh2 where 군사특기명='"+a1+"' "
    conn = create_connection("mydatabase.db")

    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
            )
    restult1=results_df.melt('입영월', var_name='구분', value_name='인원/점수')
    results_df.set_index(['입영월'],inplace=True)
    rst=results_df.transpose()
    st.dataframe(rst)
    c = alt.Chart(pd.DataFrame(restult1)).mark_line(point=True).encode(
        alt.Y('인원/점수:Q'),
        x='입영월:N',
        color='구분:N'
    ).interactive()
    st.altair_chart(c.interactive(),
    use_container_width=True)
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
    rst=results_df.transpose()
    st.dataframe(rst)
    c = alt.Chart(pd.DataFrame(restult1)).mark_line(point=True).encode(
        alt.Y('인원/점수:Q'),
        x='입영월:N',
        color='구분:N'
    ).interactive()
    st.altair_chart(c.interactive(),
    use_container_width=True)
def drive_act1(sum1):
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
    return sum1
def act2(sum3):
    conn = create_connection("mydatabase.db")
    query = conn.execute("select 자격증구분 from 점수계산 where 구분='결석일'")
    cols = [column[0] for column in query.description]
    results_df1= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols)  
    gylsuk=st.selectbox('결석일자를 선택하세요',results_df1)
    sum3=jeomsu_query('결석일',gylsuk)
    return sum3
def drive_act3(sum4):
    st.markdown("3. 가산점/배점 15점(접수마감일 기준)")
    options = st.multiselect(
            '가산점이 있으면 추가하세요.',['병역진로설계 지원자','군운전적성정밀검사','다자녀(3) 가정 자녀','다자녀(2) 가정 자녀','모집특기경력(6월~1년 미만)','모집특기경력(1년~2년 미만)','모집특기경력(2년 이상)',
                        '질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자','독립유공자 손·자녀 또는 국가유공자 자녀', '생계급여 수급권자'],['병역진로설계 지원자'])
    for i in options:
        if i in ('독립유공자 손·자녀 또는 국가유공자 자녀','생계급여 수급권자','다자녀(3) 가정 자녀','질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자','군운전적성정밀검사'):
            sum4=sum4+4
        elif i in ('모집특기경력(2년 이상)'):
            sum4=sum4+3
        elif i in ('다자녀(2) 가정 자녀','모집특기경력(1년~2년 미만)'):
            sum4=sum4+2
        else :
            sum4=sum4+1
    conn = create_connection("mydatabase.db")
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
    return sum4
def army_jeomsu():
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    st.header("나의 점수 미리알아보기")
    test1=gunsa1_query()
    if test1 in ('수송운용(차량운전)', '견인차량운전', '경장갑차운전', 'K-53계열차량운전', '구난차량운전', '크레인차량운전'):
        st.markdown(f":blue[{test1}]")
        sum1=drive_act1(sum1)
        if test1!='' and sum1!=0 :
            sum2_a=st.markdown(f"1. :green[{sum1}]점")
            st.markdown("2. 출결상황/배점 10점")
            sum3=act2(sum3)
            mod1_html=mod1.html4
            image3=st.markdown(mod1_html, unsafe_allow_html=True)
        if test1!='' and sum1!=0 and sum3!=0:
            image3.empty()
            sum2_a.empty()
            sum3_a=st.markdown(f"1. :green[{sum1}]점,2. :green[{sum3}]점")
            sum4=drive_act3(sum4)
            mod1_html=mod1.html5
            image4=st.markdown(mod1_html, unsafe_allow_html=True)
        if test1!='' and sum1!=0 and sum3!=0 and sum4>1:
            image4.empty()
            sum3_a.empty()
            sumtotal=sum1+sum3+sum4
            st.subheader(f"1. :green[{sum1}]점,2. :green[{sum3}]점,3. :green[{sum4}]점 합계 : :violet[{sumtotal}]점")
            st.subheader(test1+'(육군훈련소)')
            run_query(test1)
   
    elif test1!='':
        st.markdown(f":blue[{test1}]")
        mod1_html=mod1.html1
        st.markdown(mod1_html, unsafe_allow_html=True)

        st.markdown("1.기술자격·면허증/배점 50점")
        mod1_html=mod1.html2
        image1=st.markdown(mod1_html, unsafe_allow_html=True)

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
            mod1_html=mod1.html3
            image2=st.markdown(mod1_html, unsafe_allow_html=True)

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
            mod1_html=mod1.html4
            image3=st.markdown(mod1_html, unsafe_allow_html=True)
            sum3=act2(sum3)

        if test1!='' and sum1!=0 and sum2!=0 and sum3!=0:
            image3.empty()
            sum2_a.empty()
            sum3_a=st.markdown(f"1. :green[{sum1}]점,2. :green[{sum2}]점,3. :green[{sum3}]점")
            st.markdown("4. 가산점/배점 15점(접수마감일 기준)")
            mod1_html=mod1.html5
            image4=st.markdown(mod1_html, unsafe_allow_html=True)

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
                sum3_a.empty()
                sumtotal=sum1+sum2+sum3+sum4
                st.subheader(f"1. :green[{sum1}]점,2. :green[{sum2}]점,3. :green[{sum3}]점,4. :green[{sum4}]점 합계 : :violet[{sumtotal}]점")
                st.subheader(test1)
                mod1_html=mod1.html6
                st.markdown(mod1_html, unsafe_allow_html=True)
                run_queryq(test1)
def susong():
    df1=gunsa2_query()
    df2=df1.drop(['접수인원', '지원인원'], axis=1)
    c = alt.Chart(pd.DataFrame(df2)).mark_line(point=True).encode(
        alt.Y('커트라인:Q',scale=alt.Scale(domain=[90, 115])),
        x='입영월:N',
        color='입영부대:N'
        ).interactive()
    df4=df1.set_index(['입영월'],inplace=True)
    st.header("수송운용(차량운전) 입영부대별 현황")
    st.altair_chart(c.interactive(),
        use_container_width=True)
    st.text('1사단 : 경기 파주시 문산읍 이천리 516(사임당로 492)  ')
    df_int=df1[df1['입영부대']=="1사단"]
    if st.button('열기(1사단)'):
        df_1=st.dataframe(df_int, width=640)

    st.text('25사단 : 경기도 양주시 남면 매곡리 216-3(휴암로 393-43)')
    df_int=df1[df1['입영부대']=="25사단"]
    if st.button('열기(25사단)'):
        df_1=st.dataframe(df_int, width=640)

    st.text('28사단 : 경기도 파주시 적성면 적암리 194-8(율곡로 3064)')
    df_int=df1[df1['입영부대']=="28사단"]
    if st.button('열기(28사단)'):
        df_1=st.dataframe(df_int, width=640)

    st.text('3사단 : 강원도 철원군 서면 자등리 402(금강로 7626)')
    df_int=df1[df1['입영부대']=="3사단"]
    if st.button('열기(3사단)'):
        df_1=st.dataframe(df_int, width=640)

    st.text('51사단 : 경기도 화성시 매송면 어천리 220-1(화성로 2337-36)')
    df_int=df1[df1['입영부대']=="51사단"]
    if st.button('열기(51사단)'):
        df_1=st.dataframe(df_int, width=640)

    st.text('55사단 : 경기도 용인시 처인구 포곡읍 포곡로 164')
    df_int=df1[df1['입영부대']=="55사단"]
    if st.button('열기(55사단)'):
        df_1=st.dataframe(df_int, width=640)

    st.text('5사단 : 경기도 연천군 청산면 궁평리 299-1(청창로 474)')
    df_int=df1[df1['입영부대']=="5사단"]
    if st.button('열기(5사단)'):
        df_1=st.dataframe(df_int, width=640)

    st.text('6사단 : 강원도 철원군 동송읍 상노리(상노로 73-26)')
    df_int=df1[df1['입영부대']=="6사단"]
    if st.button('열기(6사단)'):
        df_1=st.dataframe(df_int, width=640)

    st.text('9사단 : 경기도 고양시 일산동구 성석동 612')
    df_int=df1[df1['입영부대']=="9사단"]
    if st.button('열기(9사단)'):
        df_1=st.dataframe(df_int, width=640)

    st.text('육군훈련소 : 충남 논산시 연무읍 득안대로')
    df_int=df1[df1['입영부대']=="육군훈련소"]
    if st.button('열기(육군훈련소)'):
        df_1=st.dataframe(df_int, width=640)   
def army_hh():
    st.header("육군 군사특기별 현황")
    df1=gun_query()
    col1, col2 = st.columns(2) 
    with col1:
        test1=st.selectbox('군사특기를 선택하세요',df1['군사특기명'].drop_duplicates(keep='first'),0)
    with col2:
        test2=st.selectbox('입영부대를 선택하세요',df1['입영부대'].drop_duplicates(keep="first"),0)
    df2=df1.query("군사특기명=='"+test1+"' & 입영부대=='"+test2+"' ")
    restult1=df2[['입영월','접수인원','지원인원','커트라인']]
    restult2=restult1.melt('입영월', var_name='구분', value_name='인원/점수')
    restult1.set_index(['입영월'],inplace=True)
    rst1=restult1.transpose()
    st.dataframe(rst1)

    c = alt.Chart(pd.DataFrame(restult2)).mark_line(point=True).encode(
        alt.Y('인원/점수:Q'),
        x='입영월:N',
        color='구분:N'
        ).interactive()
    st.altair_chart(c.interactive(),
        use_container_width=True)
    code1_txt=0
    code1=code_query(test1)
    code1_txt=code1['코드'].values
    txt2=''.join(code1_txt)

    code1_txt1=sogae_query(txt2)
    mod2_html=''.join(code1_txt1['Column2'].values)
    try:
        image = Image.open('image/'+txt2+'.jpeg')
    except: 
        image = Image.open('image/'+txt2+'.bmp')    
    st.image(image, caption=txt2)
    st.markdown(mod2_html, unsafe_allow_html=True)
def army_gunsa():
    st.header("육군 군사특기 추천")
    txt5=''
    txt6=''
    df1=gun1_query("자격면허")    
    test1=st.selectbox('자격면허를 선택하세요',df1['검사지침코드명'].drop_duplicates(keep='first'),0)
    txt3=''.join(test1)
    txt1=gstg1('자격면허','직접',txt3)
    txt2=gstg1('자격면허','간접',txt3)
    col1, col2 = st.columns(2)
    with col1:
        t_1=st.selectbox('직접관련 군사특기입니다.',txt1['군사특기명'].drop_duplicates(keep='first'),0)
    with col2:
        t_2=st.selectbox('간접관련 군사특기입니다.',txt2['군사특기명'].drop_duplicates(keep='first'),0)

    df2=gun1_query("전공")    
    test2=st.selectbox('전공을 선택하세요',df2['검사지침코드명'].drop_duplicates(keep='first'),0)
    st.text(test2)
    txt4=''.join(test2)
    txt5=gstg1('전공','직접',txt4)
    txt6=gstg1('전공','간접',txt4)
    if test1!='입력':
        col3, col4 = st.columns(2)
        with col3:
            st.text('직접관련 군사특기입니다.')
            st.dataframe(txt5,width=300)
        with col4:
            st.text('간접관련 군사특기입니다.')
            st.dataframe(txt6,width=300)
def jmtg():
    st.header("전문특기병 안내")
    df1=gun1_query("전문특기")    
    test1=st.selectbox('전문특기를 선택하세요',df1['전문특기'].drop_duplicates(keep='first'),0)
    txt1=''.join(test1)
    st.text(txt1)
    code1_txt1=jmtg_query(txt1)
    txt2=''.join(code1_txt1['내용'])
    st.markdown(txt2, unsafe_allow_html=True)
page_names_to_funcs = {
    "군사특기 추천": army_gunsa,
    "군사특기별 현황": army_hh,
    "수송운용(차량운전) 현황": susong,
    "전문특기병 안내": jmtg,    
    "나의점수 알아보기": army_jeomsu,
}

selected_page = st.sidebar.selectbox("원하시는 메뉴를 선택하세요!", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()