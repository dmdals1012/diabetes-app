
import streamlit as st


def run_home() :
    st.subheader('당뇨병 위험도를 분석하고 예측하는 App')
    st.text('데이터는 캐글에 있는 diabetes.csv를 사용합니다.')
    st.text('EDA 탭에서 데이터를 분석하고, ML 탭에서 예측 수행합니다.')