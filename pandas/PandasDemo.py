import pandas as pd
import streamlit as st

upload_file = st.file_uploader('excel文件', type=['xlsx'])
if upload_file is None:
    st.stop()


@st.cache_data
def load_data(file):
    print('加载缓存')
    return pd.read_excel(file, None)


dfs = load_data(upload_file)
names = list(dfs.keys())
sheet_selects = st.multiselect('工作表', names, [])
if len(sheet_selects) == 0:
    st.stop()
tabs = st.tabs(sheet_selects)
for tab, name in zip(tabs, sheet_selects):
    with tab:
        df = dfs[name]
        st.dataframe(df)
