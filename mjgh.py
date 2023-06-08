import sqlite3
import streamlit as st
import mod2

df1=mod2.gun1_query('모집계획')
st.header('군별 모집계획')
test1=st.selectbox('구분',df1['구분'].drop_duplicates(keep='first'),0)
st.subheader(test1)
df2=df1.query("구분=='"+test1+"'")
result=df2[['모집회차','입영월','지원서접수','1차발표','신검/면접','최종발표']]
result.set_index(['모집회차'],inplace=True)
st.dataframe(result)
    # df3=code_df.query("소분류=='"+test1+"'")
    # result3=df3['대분류'].values
    # result4=df3['코드'].values
    # txt3=''.join(result3)
    # txt4=''.join(result4)
    # st.text("대분류:"+txt3)
    # df2=df1.query("특기=='"+txt3+"'")

    # restult1=df2[['입영월','커트라인','선발인원']]
    # restult2=restult1.melt('입영월', var_name='구분', value_name='인원/점수')
    # restult1.set_index(['입영월'],inplace=True)
    # rst1=restult1.transpose()
    # st.dataframe(rst1)
    # c = alt.Chart(pd.DataFrame(restult2)).mark_line(point=True).encode(
    #     alt.Y('인원/점수:Q'),
    #     x='입영월:N',
    #     color='구분:N'
    # ).interactive()
    # st.altair_chart(c.interactive(),
    #     use_container_width=True)
    
    # code1_txt1=mod2.sogae_query(txt4)
    # mod2_html=''.join(code1_txt1['Column2'].values)
    # try:
    #     image = Image.open('image/'+txt4+'.jpeg')
    # except: 
    #     image = Image.open('image/'+txt4+'.gif')    
    # st.image(image, caption=txt4)
    # st.markdown(mod2_html, unsafe_allow_html=True)  