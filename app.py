from multiprocessing.sharedctypes import Value
import streamlit as st
import os

st.set_page_config(
  page_icon="😆",
  page_title="대구병역진로설계지원센터",
)
root = os.path.join(os.path.dirname(__file__))

dashboards = {
    "육군": os.path.join(root, "army1.py"),
    "해군": os.path.join(root, "navy.py"),
    "공군": os.path.join(root, "airforce.py"),
    "해병대": os.path.join(root, "marine.py"),
    "테스트": os.path.join(root, "test.py"),
    "Database": os.path.join(root, "datatest.py")
}

choice_from_url = query_params = st.experimental_get_query_params().get("육군", ["육군"])[0]
index = list(dashboards.keys()).index(choice_from_url)

choice = st.sidebar.radio("군을 선택하세요!!!", list(dashboards.keys()), index=index)

path = dashboards[choice]

with open(path, encoding="utf-8") as code:
    c = code.read()
    exec(c, globals())

#     with st.expander('Code for this example:'):
#         st.markdown(f"""``` python
# {c}```""")