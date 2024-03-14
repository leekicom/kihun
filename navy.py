import sqlite3
import streamlit as st
import pandas as pd
import altair as alt
import os
import mod1
import mod2
from PIL import Image

def navy_hh():
    st.header("해군 군사특기별 현황")
    df1=mod2.gun1_query('해군특기별현황')
    code_df=mod2.code_query('N')
    test1=st.selectbox('군사특기를 선택하세요',code_df['소분류'].drop_duplicates(keep='first'),0)

    df3=code_df.query("소분류=='"+test1+"'")

    result3=df3['대분류'].values
    result4=df3['코드'].values
    txt3=''.join(result3)
    txt4=''.join(result4)
    st.text("대분류:"+txt3)
    df2=df1.query("특기=='"+txt3+"'")

    restult1=df2[['입영월','접수인원','커트라인']]
    restult2=restult1.melt('입영월', var_name='구분', value_name='점수')
    restult1.set_index(['입영월'],inplace=True)
    rst1=restult1.transpose()
    st.dataframe(rst1)
    c = alt.Chart(pd.DataFrame(restult2)).mark_line(point=True).encode(
        alt.Y('점수:Q'),
        x='입영월:N',
        color='구분:N'
    ).interactive()
    st.altair_chart(c.interactive(),
        use_container_width=True)
    
    code1_txt1=mod2.sogae_query(txt4)
    mod2_html=''.join(code1_txt1['Column2'].values)
    try:
        image = Image.open('image/'+txt4+'.jpeg')
    except: 
        image = Image.open('image/'+txt4+'.gif')    
    st.image(image, caption=txt4)
    st.markdown(mod2_html, unsafe_allow_html=True)
def navy_jeomsu():
    st.header("나의 점수 미리알아보기")
    df1=mod2.gun1_query('해군특기별현황')
    code_df=mod2.code_query('N')
    test1=st.selectbox('군사특기를 선택하세요',code_df['소분류'].drop_duplicates(keep='first'),0)
    df3=code_df.query("소분류=='"+test1+"'")

    result3=df3['대분류'].values
    result4=df3['코드'].values
    txt3=''.join(result3)
    txt4=''.join(result4)
    df2=df1.query("특기=='"+txt3+"'")
    if txt3 in ('일반'):
        navy_jeomsu1(txt3,txt4,df2)
    else:
        navy_jeomsu2(txt3,txt4,df2)  
def navy_jeomsu1(txt3,txt4,df2):
    sum1=0
    sum2=0
    sum4=0

    st.markdown(f":blue[{txt3}]")
    mod1_html=mod1.html15
    st.markdown(mod1_html, unsafe_allow_html=True)
    st.markdown("1.자격.면허/배점 70점")
    mod1_html=mod1.html8
    image1=st.markdown(mod1_html, unsafe_allow_html=True)
    conn = mod2.create_connection("mydatabase.db")
    query = conn.execute("select 자격증구분 from 공군점수계산 where 구분='일반자격'")

    cols = [column[0] for column in query.description]
    results_df1= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
                )  
    license1="일반자격"
    license2=st.selectbox('자격증구분을 선택하세요',results_df1)
    sum1=mod2.jeomsu_query(license1,license2)  

    if txt3!='' and sum1!=0:
        image1.empty()
        sum1_a=st.markdown(f"1. :green[{sum1}]점")
        st.markdown("2. 고교 출결사항 20점")
        mod1_html=mod1.html9
        image2=st.markdown(mod1_html, unsafe_allow_html=True)

        query = conn.execute("select 자격증구분 from 공군점수계산 where 구분='일반결석일'")
        cols = [column[0] for column in query.description]
        results_df1= pd.DataFrame.from_records(
                    data = query.fetchall(), 
                    columns = cols)  
        hak2=st.selectbox('결석일자를 선택하세요',results_df1)
        hak1="일반결석일"
        sum2=mod2.jeomsu_query(hak1,hak2)
        if txt3!='' and sum1!=0 and sum2!=0:
            image2.empty()
            sum1_a.empty()
            sum3_a=st.markdown(f"1. :green[{sum1}]점,2. :green[{sum2}]점")
            st.markdown("3. 가산점/배점 15점(접수마감일 기준)")
            mod1_html=mod1.html17
            image4=st.markdown(mod1_html, unsafe_allow_html=True)

            options = st.multiselect(
                '가산점이 있으면 추가하세요.',['병역진로설계 지원자','다자녀(3) 가정 자녀','다자녀(2) 가정 자녀','수영관련자격증(잠수기능사)','수영관련자격증(수상안전강사)','수영관련자격증(인명구조)','수영관련자격증(잠수자격)','수송계열(건설기계 운전자격증)',
                '관련분야 직업경력(2년이상)','관련분야 직업경력(1~2년미만)','관련분야 직업경력(6개월~1년미만)','관련분야 직업경력(6개월미만)',
                '전산계열(컴퓨터속기,한글속기 3년이상)','전산계열(컴퓨터속기,한글속기 1년이상)','전산계열(컴퓨터속기,한글속기 6개월이상)','전산계열(한글속기 20편이상)','전산계열(한글속기 20편미만)',
                '질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자','독립유공자 손·자녀 또는 국가유공자 자녀', '생계급여 수급권자'],['병역진로설계 지원자'])
            for i in options:
                if i in ('독립유공자 손·자녀 또는 국가유공자 자녀','생계급여 수급권자','다자녀(3) 가정 자녀','질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자','전산계열(컴퓨터속기,한글속기 1년이상)','관련분야 직업경력(1~2년미만)'):
                    sum4=sum4+4
                elif i in ('전산계열(컴퓨터속기,한글속기 3년이상)','관련분야 직업경력(2년이상)','수영관련자격증(잠수기능사)','수영관련자격증(수상안전강사)'):
                    sum4=sum4+5                      
                elif i in ('모집특기경력(2년 이상)','전산계열(컴퓨터속기,한글속기 6개월이상)','관련분야 직업경력(6개월~1년미만)'):
                    sum4=sum4+3
                elif i in ('수영관련자격증(인명구조)','수영관련자격증(잠수자격)','수송계열(건설기계 운전자격증)'):
                    sum4=sum4+2.5
                elif i in ('다자녀(2) 가정 자녀','전산계열(한글속기 20편이상)','관련분야 직업경력(6개월미만)'):
                    sum4=sum4+2
                else :
                    sum4=sum4+1

            query = conn.execute("select 자격증구분 from 점수계산 where 구분='헌혈'")
            cols = [column[0] for column in query.description]
            results_df1= pd.DataFrame.from_records(
                    data = query.fetchall(), 
                    columns = cols)  
            blood1=st.selectbox('헌혈횟수를 선택하세요',results_df1)
            sum41=mod2.jeomsu_query('헌혈',blood1)

            query = conn.execute("select 자격증구분 from 점수계산 where 구분='봉사시간'")
            cols = [column[0] for column in query.description]
            results_df1= pd.DataFrame.from_records(
                    data = query.fetchall(), 
                    columns = cols)  
            blood2=st.selectbox('봉사시간을 선택하세요',results_df1)
            sum42=mod2.jeomsu_query('봉사시간',blood2)
            if sum41+sum42>8 :
                sum4=sum4+8
            else:
                sum4=sum4+sum41+sum42
            if sum4>15:
                sum4=15

            if txt3!='' and sum1!=0 and sum2!=0 and sum4>1:
                image4.empty()
                sum3_a.empty()
                sumtotal=sum1+sum2+sum4
                st.subheader(f"1. :green[{sum1}]점,2. :green[{sum2}]점,3. :green[{sum4}]점 합계 : :violet[{sumtotal}]점")
                st.subheader(txt3+"-"+txt4)
                restult1=df2[['입영월','접수인원','커트라인']]
                restult2=restult1.melt('입영월', var_name='구분', value_name='점수')
                restult1.set_index(['입영월'],inplace=True)
                rst1=restult1.transpose()
                st.dataframe(rst1)
                c = alt.Chart(pd.DataFrame(restult2)).mark_line(point=True).encode(
                        alt.Y('점수:Q'),
                        x='입영월:N',
                        color='구분:N'
                    ).interactive()
                st.altair_chart(c.interactive(),
                        use_container_width=True)
    
                code1_txt1=mod2.sogae_query(txt4)
                mod2_html=''.join(code1_txt1['Column2'].values)
                try:
                    image = Image.open('image/'+txt4+'.jpeg')
                except: 
                    image = Image.open('image/'+txt4+'.gif')    
                st.image(image, caption=txt4)
                st.markdown(mod2_html, unsafe_allow_html=True)
def navy_jeomsu2(txt3,txt4,df2):
    sum1=0
    sum2=0
    sum3=0
    sum4=0

    st.markdown(f":blue[{txt3}]")
    mod1_html=mod1.html16
    st.markdown(mod1_html, unsafe_allow_html=True)
    st.markdown("1.자격.면허/배점 50점")
    mod1_html=mod1.html12
    image1=st.markdown(mod1_html, unsafe_allow_html=True)
    conn = mod2.create_connection("mydatabase.db")
    query = conn.execute("select 자격증구분 from 공군점수계산 where 구분='전문자격'")

    cols = [column[0] for column in query.description]
    results_df1= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols
                )  
    license1="전문자격"
    license2=st.selectbox('자격증구분을 선택하세요',results_df1)
    sum1=mod2.jeomsu_query(license1,license2)  

    if txt3!='' and sum1!=0:
        image1.empty()
        sum1_a=st.markdown(f"1. :green[{sum1}]점")
        st.markdown("2. 전공학과/배점 40점")
        mod1_html=mod1.html3
        image2=st.markdown(mod1_html, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            hak1 = st.radio("학력구분을 선택하세요.",('대학교', '전문대','고졸','기타'))
        with col2:
            query = conn.execute("select 자격증구분 from 공군점수계산 where 구분='"+hak1+"'")
            cols = [column[0] for column in query.description]
            results_df1= pd.DataFrame.from_records(
                data = query.fetchall(), 
                columns = cols)  
            hak2=st.selectbox('학력구분을 선택하세요',results_df1)
            sum2=mod2.jeomsu_query(hak1,hak2)
        if txt3!='' and sum1!=0 and sum2!=0:
            image2.empty()
            sum1_a.empty()
            sum2_a=st.markdown(f"1. :green[{sum1}]점,2. :green[{sum2}]점")
            st.markdown("3. 고교 출결사항 20점")
            mod1_html=mod1.html14
            image3=st.markdown(mod1_html, unsafe_allow_html=True)

            query = conn.execute("select 자격증구분 from 공군점수계산 where 구분='전문결석일'")
            cols = [column[0] for column in query.description]
            results_df1= pd.DataFrame.from_records(
                    data = query.fetchall(), 
                    columns = cols)  
            hak2=st.selectbox('결석일자를 선택하세요',results_df1)
            hak1="전문결석일"
            sum3=mod2.jeomsu_query(hak1,hak2)
            if txt3!='' and sum1!=0 and sum2!=0 and sum3!=0:
                image3.empty()
                sum2_a.empty()
                sum3_a=st.markdown(f"1. :green[{sum1}]점,2. :green[{sum2}]점,3. :green[{sum3}]점")
                st.markdown("3. 가산점/배점 15점(접수마감일 기준)")
                mod1_html=mod1.html17
                image4=st.markdown(mod1_html, unsafe_allow_html=True)

                options = st.multiselect(
                '가산점이 있으면 추가하세요.',['병역진로설계 지원자','다자녀(3) 가정 자녀','다자녀(2) 가정 자녀','수영관련자격증(잠수기능사)','수영관련자격증(수상안전강사)','수영관련자격증(인명구조)','수영관련자격증(잠수자격)','수송계열(건설기계 운전자격증)',
                '관련분야 직업경력(2년이상)','관련분야 직업경력(1~2년미만)','관련분야 직업경력(6개월~1년미만)','관련분야 직업경력(6개월미만)',
                '전산계열(컴퓨터속기,한글속기 3년이상)','전산계열(컴퓨터속기,한글속기 1년이상)','전산계열(컴퓨터속기,한글속기 6개월이상)','전산계열(한글속기 20편이상)','전산계열(한글속기 20편미만)',
                '질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자','독립유공자 손·자녀 또는 국가유공자 자녀', '생계급여 수급권자'],['병역진로설계 지원자'])
                for i in options:
                    if i in ('독립유공자 손·자녀 또는 국가유공자 자녀','생계급여 수급권자','다자녀(3) 가정 자녀','질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자','전산계열(컴퓨터속기,한글속기 1년이상)','관련분야 직업경력(1~2년미만)'):
                        sum4=sum4+4
                    elif i in ('전산계열(컴퓨터속기,한글속기 3년이상)','관련분야 직업경력(2년이상)','수영관련자격증(잠수기능사)','수영관련자격증(수상안전강사)'):
                        sum4=sum4+5                      
                    elif i in ('모집특기경력(2년 이상)','전산계열(컴퓨터속기,한글속기 6개월이상)','관련분야 직업경력(6개월~1년미만)'):
                        sum4=sum4+3
                    elif i in ('수영관련자격증(인명구조)','수영관련자격증(잠수자격)','수송계열(건설기계 운전자격증)'):
                        sum4=sum4+2.5
                    elif i in ('다자녀(2) 가정 자녀','전산계열(한글속기 20편이상)','관련분야 직업경력(6개월미만)'):
                        sum4=sum4+2
                    else :
                        sum4=sum4+1

                query = conn.execute("select 자격증구분 from 점수계산 where 구분='헌혈'")
                cols = [column[0] for column in query.description]
                results_df1= pd.DataFrame.from_records(
                    data = query.fetchall(), 
                    columns = cols)  
                blood1=st.selectbox('헌혈횟수를 선택하세요',results_df1)
                sum41=mod2.jeomsu_query('헌혈',blood1)

                query = conn.execute("select 자격증구분 from 점수계산 where 구분='봉사시간'")
                cols = [column[0] for column in query.description]
                results_df1= pd.DataFrame.from_records(
                    data = query.fetchall(), 
                    columns = cols)  
                blood2=st.selectbox('봉사시간을 선택하세요',results_df1)
                sum42=mod2.jeomsu_query('봉사시간',blood2)
                if sum41+sum42>8 :
                    sum4=sum4+8
                else:
                    sum4=sum4+sum41+sum42
                if sum4>15:
                    sum4=15

                if txt3!='' and sum1!=0 and sum2!=0 and sum4>1:
                    image4.empty()
                    sum3_a.empty()
                    sumtotal=sum1+sum2+sum3+sum4
                    st.subheader(f"1. :green[{sum1}]점,2. :green[{sum2}]점,3. :green[{sum3}]점,4. :green[{sum4}]점 합계 : :violet[{sumtotal}]점")
                    st.subheader(txt3+"-"+txt4)
                    restult1=df2[['입영월','접수인원','커트라인']]
                    restult2=restult1.melt('입영월', var_name='구분', value_name='점수')
                    restult1.set_index(['입영월'],inplace=True)
                    rst1=restult1.transpose()
                    st.dataframe(rst1)
                    c = alt.Chart(pd.DataFrame(restult2)).mark_line(point=True).encode(
                        alt.Y('점수:Q'),
                        x='입영월:N',
                        color='구분:N'
                    ).interactive()
                    st.altair_chart(c.interactive(),
                        use_container_width=True)
    
                    code1_txt1=mod2.sogae_query(txt4)
                    mod2_html=''.join(code1_txt1['Column2'].values)
                    try:
                        image = Image.open('image/'+txt4+'.jpeg')
                    except: 
                        image = Image.open('image/'+txt4+'.gif')    
                    st.image(image, caption=txt4)
                    st.markdown(mod2_html, unsafe_allow_html=True)

                    st.markdown(f":blue[{txt3}]")    
def navy_gunsa():
    st.header("해군 군사특기 추천(자격면허)")
    txt5=''
    df1=mod2.gun1_query("자격면허")    
    test1=st.selectbox('자격면허를 선택하세요',df1['검사지침코드명'].drop_duplicates(keep='first'),0)
    txt3=''.join(test1)
    txt1=mod2.gstg1('자격면허','해군','직접',txt3)
    st.text(txt1[['군사특기']])

   st.header("해군 군사특기 추천(전공)")
    df2=mod2.gun1_query("전공")    
    test2=st.selectbox('전공을 선택하세요',df2['검사지침코드명'].drop_duplicates(keep='first'),0)

    txt4=''.join(test2)
    txt5=mod2.gstg1('전공','해군','직접',txt4)
    if test1!='입력':
            st.dataframe(txt5,width=300)
def jmtg():
    st.header("전문특기병 안내")
    st.markdown(mod1.html61, unsafe_allow_html=True)    
page_names_to_funcs = {
    "군사특기 추천": navy_gunsa,
    "군사특기별 현황": navy_hh,
    "전문특기병 안내": jmtg,
    "나의점수 알아보기": navy_jeomsu,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()