

import streamlit as st
import pandas as pd
import numpy as np
import joblib

def load_model():
    # 저장된 모델 불러오기
    model = joblib.load('model/pipeline.pkl')
    
    return model

def predict_diabetes(model, features):
    # 예측 수행
    prediction = model.predict(features.reshape(1, -1))
    probability = model.predict_proba(features.reshape(1, -1))
    return prediction[0], probability[0][1]

def run_ml():
    st.title('당뇨병 예측')

    # 모델과 스케일러 불러오기
    model = load_model()

    # 사용자 입력 받기
    st.subheader('환자 정보 입력')
    pregnancies = st.number_input('임신 횟수', min_value=0, max_value=20, value=0)
    glucose = st.number_input('포도당 농도', min_value=0, max_value=300, value=100)
    blood_pressure = st.number_input('최고 혈압(수축기 혈압)', min_value=0, max_value=300, value=120)
    insulin = st.number_input('인슐린', min_value=0, max_value=1000, value=80)
    bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, value=25.0)
    diabetes_pedigree = st.number_input('당뇨병 가족력', min_value=0.0, max_value=3.0, value=0.5)
    age = st.number_input('나이', min_value=0, max_value=120, value=30)

    # 예측 버튼
    if st.button('예측하기'):
        features = np.array([pregnancies, glucose, blood_pressure, insulin, bmi, diabetes_pedigree, age])
        prediction, probability = predict_diabetes(model, features)

        # 결과 표시
        st.subheader('예측 결과')
        if prediction == 1:
            st.warning('당뇨병 발병 가능성이 높습니다.')
        else:
            st.success('당뇨병 발병 가능성이 낮습니다.')
        
        st.write(f'당뇨병 발병 확률: {probability:.2%}')

