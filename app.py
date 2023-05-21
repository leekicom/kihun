import streamlit as st
import pandas as pd
import numpy as np
import csv



st.title('나의 점수 미리알아보기')

test=st.selectbox('군을 선택해주세요',('육군(기술행정병)', '해군(기술병)', '공군(기술병)','해병대'))
st.title(test)

with open('군사특기.csv',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)