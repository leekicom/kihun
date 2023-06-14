import sqlite3
import streamlit as st
import pandas as pd
import altair as alt
import os
import mod1
import mod2
from PIL import Image

def air_force_hh():
    st.header("공군 군사특기별 현황")
    df1=mod2.gun1_query('공군특기별현황')
    code_df=mod2.code_query('A')
    test1=st.selectbox('군사특기를 선택하세요',code_df['소분류'].drop_duplicates(keep='first'),0)
    df3=code_df.query("소분류=='"+test1+"'")
    result3=df3['대분류'].values
    result4=df3['코드'].values
    txt3=''.join(result3)
    txt4=''.join(result4)
    st.text("대분류:"+txt3)
    df2=df1.query("특기=='"+txt3+"'")

    restult1=df2[['입영월','커트라인','선발인원']]
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
    
    code1_txt1=mod2.sogae_query(txt4)
    mod2_html=''.join(code1_txt1['Column2'].values)
    try:
        image = Image.open('image/'+txt4+'.jpeg')
    except: 
        image = Image.open('image/'+txt4+'.gif')    
    st.image(image, caption=txt4)
    st.markdown(mod2_html, unsafe_allow_html=True)  
def air_force_jeomsu():
    st.header("나의 점수 미리알아보기")
    df1=mod2.gun1_query('공군특기별현황')
    code_df=mod2.code_query('A')
    test1=st.selectbox('군사특기를 선택하세요',code_df['소분류'].drop_duplicates(keep='first'),0)
    df3=code_df.query("소분류=='"+test1+"'")

    result3=df3['대분류'].values
    result4=df3['코드'].values
    txt3=''.join(result3)
    txt4=''.join(result4)
    df2=df1.query("특기=='"+txt3+"'")
    if txt3 in ('일반'):
        air_force_jeomsu1(txt3,txt4,df2)
    else:
        air_force_jeomsu2(txt3,txt4,df2)                 
def air_force_jeomsu1(txt3,txt4,df2):
    sum1=0
    sum2=0
    sum4=0

    st.markdown(f":blue[{txt3}]")
    mod1_html=mod1.html7
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
            mod1_html=mod1.html10
            image4=st.markdown(mod1_html, unsafe_allow_html=True)

            options = st.multiselect(
                '가산점이 있으면 추가하세요.',['병역진로설계 지원자','다자녀(3) 가정 자녀','다자녀(2) 가정 자녀','지정특기(방공포,군사경찰,조리)','화생방 직종(운전면허-2종보통이상)','항공정비사(기사급) 또는 항공정비 기초인력 인증서',
                '한국사능력검정(3,4급)','한국사능력검정(1,2급)','한국어능력검정(3,4급)','한국어능력검정(1,2급)','토익(520~),토플(59~),텝스(201~)','토익(730~),토플(82~),텝스(277~)',
                '질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자','독립유공자 손·자녀 또는 국가유공자 자녀', '생계급여 수급권자'],['병역진로설계 지원자'])
            for i in options:
                if i in ('독립유공자 손·자녀 또는 국가유공자 자녀','생계급여 수급권자','다자녀(3) 가정 자녀','질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자','지정특기(방공포,군사경찰,조리)','화생방 직종(운전면허-2종보통이상)','항공정비사(기사급) 또는 항공정비 기초인력 인증서'):
                    sum4=sum4+4
                elif i in ('모집특기경력(2년 이상)'):
                    sum4=sum4+3
                elif i in ('다자녀(2) 가정 자녀','모집특기경력(1년~2년 미만)','한국사능력검정(1,2급)','한국어능력검정(1,2급)','토익(730~),토플(82~),텝스(277~)'):
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
                restult1=df2[['입영월','커트라인','선발인원']]
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
    
                code1_txt1=mod2.sogae_query(txt4)
                mod2_html=''.join(code1_txt1['Column2'].values)
                try:
                    image = Image.open('image/'+txt4+'.jpeg')
                except: 
                    image = Image.open('image/'+txt4+'.gif')    
                st.image(image, caption=txt4)
                st.markdown(mod2_html, unsafe_allow_html=True)
def air_force_jeomsu2(txt3,txt4,df2):
    sum1=0
    sum2=0
    sum3=0
    sum4=0

    st.markdown(f":blue[{txt3}]")
    mod1_html=mod1.html11
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
                mod1_html=mod1.html10
                image4=st.markdown(mod1_html, unsafe_allow_html=True)

                options = st.multiselect(
                '가산점이 있으면 추가하세요.',['병역진로설계 지원자','다자녀(3) 가정 자녀','다자녀(2) 가정 자녀','지정특기(방공포,군사경찰,조리)','화생방 직종(운전면허-2종보통이상)','항공정비사(기사급) 또는 항공정비 기초인력 인증서',
                '한국사능력검정(3,4급)','한국사능력검정(1,2급)','한국어능력검정(3,4급)','한국어능력검정(1,2급)','토익(520~),토플(59~),텝스(201~)','토익(730~),토플(82~),텝스(277~)',
                '질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자','독립유공자 손·자녀 또는 국가유공자 자녀', '생계급여 수급권자'],['병역진로설계 지원자'])
                for i in options:
                    if i in ('독립유공자 손·자녀 또는 국가유공자 자녀','생계급여 수급권자','다자녀(3) 가정 자녀','질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자','지정특기(방공포,군사경찰,조리)','화생방 직종(운전면허-2종보통이상)','항공정비사(기사급) 또는 항공정비 기초인력 인증서'):
                        sum4=sum4+4
                    elif i in ('모집특기경력(2년 이상)'):
                        sum4=sum4+3
                    elif i in ('다자녀(2) 가정 자녀','모집특기경력(1년~2년 미만)','한국사능력검정(1,2급)','한국어능력검정(1,2급)','토익(730~),토플(82~),텝스(277~)'):
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
                    restult1=df2[['입영월','커트라인','선발인원']]
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
    
                    code1_txt1=mod2.sogae_query(txt4)
                    mod2_html=''.join(code1_txt1['Column2'].values)
                    try:
                        image = Image.open('image/'+txt4+'.jpeg')
                    except: 
                        image = Image.open('image/'+txt4+'.gif')    
                    st.image(image, caption=txt4)
                    st.markdown(mod2_html, unsafe_allow_html=True)

                    st.markdown(f":blue[{txt3}]")    
def air_force_gunsa():
    st.header("공군 군사특기 추천")
    txt5=''
    df1=mod2.gun1_query("자격면허")    
    test1=st.selectbox('자격면허를 선택하세요',df1['검사지침코드명'].drop_duplicates(keep='first'),0)
    txt3=''.join(test1)
    st.text(txt3)
    txt1=mod2.gstg2('자격면허','공군','직접',txt3,'공군특기별현황')
    st.dataframe(txt1)


    df2=mod2.gun1_query("전공")    
    test2=st.selectbox('전공을 선택하세요',df2['검사지침코드명'].drop_duplicates(keep='first'),0)

    txt4=''.join(test2)
    txt5=mod2.gstg2('전공','공군','직접',txt4,'공군특기별현황')
    st.dataframe(txt5,width=300)
def jmtg():
    st.header("전문특기병 안내")
    st.markdown(mod1.html60, unsafe_allow_html=True)    
page_names_to_funcs = {
    "군사특기 추천": air_force_gunsa,
    "군사특기별 현황": air_force_hh,
    "전문특기병 안내": jmtg,
    "나의점수 알아보기": air_force_jeomsu,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()