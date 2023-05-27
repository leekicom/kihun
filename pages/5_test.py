import sqlite3
import streamlit as st
import os
import re
import webbrowser

moon=open('speech_moon.txt',encoding='UTF-8').read()
moon=re.sub('[^가-힣]',' ',moon)


font='DoHyeon-Regular.ttf'
if st.button('Say hello'):
    st.write('Why hello there')
    webbrowser.open('http://www.naver.com')
else:
    st.write('Goodbye')
html = """
    <table class="table_col">
	<thead>
		<tr>
			<th rowspan="2" scope="col">구분</th>
			<th colspan="4" scope="col" align="center">1차 평가</th>
			<th scope="col" align="center">2차 평가</th>
			<th rowspan="2" scope="col" align="center">계</th>
		</tr>
		<tr>
			<th scope="col">기술자격·면허</th>
			<th scope="col">전공학과</th>
			<th scope="col">출결상황</th>
			<th scope="col">가산점</th>
			<th scope="col" align="center">면접</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td align="center">50</td>
			<td align="center">40</td>
			<td align="center">10</td>
			<td align="center">15</td>
			<td>적격/부적격</td>
			<td>115</td>
		</tr>
	</tbody>
</table>
"""
st.markdown(html, unsafe_allow_html=True)
# dic_word=df_word.set_index('word').to_dict()['n']
# dic_word