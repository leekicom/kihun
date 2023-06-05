import sqlite3
import streamlit as st
import pandas as pd
import altair as alt
import os
import mod1
import mod2
from PIL import Image


def marine_hh():
    st.header("해병대 군사특기별 현황")
    df1=mod2.gun1_query('해병대특기별현황')
    code_df=mod2.code_query()
    test1=st.selectbox('군사특기를 선택하세요',code_df['소분류'].drop_duplicates(keep='first'),0)
    df3=code_df.query("소분류=='"+test1+"'")

    result3=df3['대분류'].values
    result4=df3['코드'].values
    txt3=''.join(result3)
    txt4=''.join(result4)
    st.text("대분류:"+txt3)
    df2=df1.query("특기=='"+txt3+"'")

    restult1=df2[['입영월','1차','최종']]
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

def marine_jeomsu1(txt3,txt4,df2):
    sum1=0
    sum2=0
    sum4=0

    st.markdown(f":blue[{txt3}]")
    mod1_html=mod1.html18
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
            mod1_html=mod1.html21
            image4=st.markdown(mod1_html, unsafe_allow_html=True)

            options = st.multiselect(
                '가산점이 있으면 추가하세요.',['병역진로설계 지원자','다자녀(3) 가정 자녀','다자녀(2) 가정 자녀','수상인명구조자격증','공인회계사자격증','스키강사자격증','스킨스쿠버자격증','수영강사자격증',
                '무도유단자(3단이상)','무도유단자(1~2단)','수상인명구조자격증(수색)',
                '질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자','독립유공자 손·자녀 또는 국가유공자 자녀', '생계급여 수급권자'],['병역진로설계 지원자'])
            for i in options:
                if i in ('독립유공자 손·자녀 또는 국가유공자 자녀','생계급여 수급권자','다자녀(3) 가정 자녀','질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자'):
                    sum4=sum4+4
                elif i in ('무도유단자(3단이상)','수상인명구조자격증(수색)'):
                    sum4=sum4+5                      
                elif i in ('공인회계사자격증','스키강사자격증','스킨스쿠버자격증','수영강사자격증'):
                    sum4=sum4+10
                elif i in ('다자녀(2) 가정 자녀','무도유단자(1~2단)','수상인명구조자격증'):
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
                restult1=df2[['입영월','1차','최종']]
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
                mod1_html=mod1.html20
                image5=st.markdown(mod1_html, unsafe_allow_html=True)
def marine_jeomsu2(txt3,txt4,df2):
    sum1=0
    sum2=0
    sum3=0
    sum4=0

    st.markdown(f":blue[{txt3}]")
    mod1_html=mod1.html19
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
                mod1_html=mod1.html21
                image4=st.markdown(mod1_html, unsafe_allow_html=True)

                options = st.multiselect(
                '가산점이 있으면 추가하세요.',['병역진로설계 지원자','다자녀(3) 가정 자녀','다자녀(2) 가정 자녀','수상인명구조자격증','공인회계사자격증','스키강사자격증','스킨스쿠버자격증','수영강사자격증',
                '무도유단자(3단이상)','무도유단자(1~2단)','수상인명구조자격증(수색)',
                '질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자','독립유공자 손·자녀 또는 국가유공자 자녀', '생계급여 수급권자'],['병역진로설계 지원자'])
                for i in options:
                    if i in ('독립유공자 손·자녀 또는 국가유공자 자녀','생계급여 수급권자','다자녀(3) 가정 자녀','질병치료에 따른 병역처분변경','국외이주자 중 현역병복무지원자'):
                        sum4=sum4+4
                    elif i in ('무도유단자(3단이상)','수상인명구조자격증(수색)'):
                        sum4=sum4+5                      
                    elif i in ('공인회계사자격증','스키강사자격증','스킨스쿠버자격증','수영강사자격증'):
                        sum4=sum4+10
                    elif i in ('다자녀(2) 가정 자녀','무도유단자(1~2단)','수상인명구조자격증'):
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
                    restult1=df2[['입영월','1차','최종']]
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
                    mod1_html=mod1.html20
                    image5=st.markdown(mod1_html, unsafe_allow_html=True)
def marine_gunsa():
    st.header("해병대 군사특기 추천")
    txt5=''
    df1=mod2.gun1_query("자격면허")    
    test1=st.selectbox('자격면허를 선택하세요',df1['검사지침코드명'].drop_duplicates(keep='first'),0)
    txt3=''.join(test1)
    txt1=mod2.gstg1('자격면허','직접',txt3)
    #t_1=st.selectbox('직접관련 군사특기입니다.',txt1['군사특기'].drop_duplicates(keep='first'),0)
    st.text(txt1[['군사특기']])

    df2=mod2.gun1_query("전공")    
    test2=st.selectbox('전공을 선택하세요',df2['검사지침코드명'].drop_duplicates(keep='first'),0)

    txt4=''.join(test2)
    txt5=mod2.gstg1('전공','직접',txt4)
    if test1!='입력':
        t_3=st.selectbox('직접관련 군사특기입니다.',txt5['군사특기'].drop_duplicates(keep='first'),0)
def marine_jeomsu():
    st.header("나의 점수 미리알아보기")
    df1=mod2.gun1_query('해병대특기별현황')
    code_df=mod2.code_query()
    test1=st.selectbox('군사특기를 선택하세요',code_df['소분류'].drop_duplicates(keep='first'),0)
    df3=code_df.query("소분류=='"+test1+"'")

    result3=df3['대분류'].values
    result4=df3['코드'].values
    txt3=''.join(result3)
    txt4=''.join(result4)
    df2=df1.query("특기=='"+txt3+"'")
    if txt3 in ('일반'):
        marine_jeomsu1(txt3,txt4,df2)
    else:
        marine_jeomsu2(txt3,txt4,df2)  
page_names_to_funcs = {
    "군사특기 추천": marine_gunsa,
    "군사특기별 현황": marine_hh,
    "나의점수 알아보기": marine_jeomsu,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()