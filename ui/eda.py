
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import os
import matplotlib.font_manager as fm

@st.cache_data
def fontRegistered():
    font_dirs = [os.getcwd() + '/custom_fonts']
    font_files = fm.findSystemFonts(fontpaths=font_dirs)
    for font_file in font_files:
        fm.fontManager.addfont(font_file)
    fm._load_fontmanager(try_read_cache=False)


column_mapping = {
    'Pregnancies': '임신 횟수',
    'Glucose': '포도당',
    'BloodPressure': '혈압',
    'SkinThickness': '피부 두께',
    'Insulin': '인슐린',
    'BMI': '체질량 지수',
    'DiabetesPedigreeFunction': '당뇨병 가족력',
    'Age': '나이',
    'Outcome': '결과'
}

def translate_columns(df):
    df.rename(columns=column_mapping, inplace=True)
    return df


# 데이터 로드
@st.cache_data
def load_data():
    data = pd.read_csv('data/diabetes.csv')
    data.columns = [column_mapping.get(col, col) for col in data.columns]
    return data


def run_eda():
    fontRegistered()
    plt.rc('font', family='NanumGothic')

    st.title('당뇨병 데이터 분석')

    # 데이터 로드
    df = load_data()

    print(df.columns)

    # '결과' 열을 '음성'과 '양성'으로 변경
    df['결과'] = df['결과'].map({0: '음성', 1: '양성'})

    # 기본 통계 정보 표시
    st.subheader('데이터 기본 정보(전체 데이터 중 5개 예시)')
    st.write(df.head(5))

    # 상관관계 히트맵 (중요 특성만 선택)
    st.subheader('주요 특성 간 상관관계')
    important_features = ['포도당', '체질량 지수', '나이', '임신 횟수', '혈압']
    if st.button('상관관계 히트맵 표시'):
        fig, ax = plt.subplots(figsize=(10, 8))
        sb.heatmap(df[important_features].corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    # 특성별 분포 시각화 (KDE 플롯으로 변경)
    st.subheader('주요 특성별 분포')
    feature = st.selectbox('특성을 선택하세요:', important_features, key='feature_selectbox')
    if st.button('KDE 플롯 표시'):
        fig, ax = plt.subplots(figsize=(10, 6))
        sb.kdeplot(data=df, x=feature, hue='결과', shade=True, ax=ax)
        plt.title(f'{feature}의 분포 (음성 vs 양성)')
        st.pyplot(fig)

    # 박스플롯
    st.subheader('특성별 박스플롯')
    box_feature = st.selectbox('특성을 선택하세요:', important_features, key='box_feature')
    if st.button('박스플롯 표시'):
        fig, ax = plt.subplots(figsize=(10, 6))
        sb.boxplot(data=df, x='결과', y=box_feature, ax=ax)
        ax.set_title(f'{box_feature}의 분포 (음성 vs 양성)')
        st.pyplot(fig)