import streamlit as st
import pandas as pd
import numpy as np
import csv



st.title('나의 점수 미리알아보기')

test=st.selectbox('군을 선택해주세요',('','육군(기술행정병)', '해군(기술병)', '공군(기술병)','해병대(기술병)'))
st.title(test)
if test == "육군(기술행정병)":
    with open('군사특기_육군.csv',newline='', encoding="utf8") as f:
      reader = csv.reader(f)
      header = next(reader)
elif test == "해군(기술병)":
    with open('군사특기_해군.csv',newline='', encoding="utf8") as f:
      reader = csv.reader(f)
      header = next(reader)
else:
    st.title(test)

for row in reader:
    st.table(row)


