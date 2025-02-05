
import streamlit as st

from ui.ml import run_ml
from ui.eda import run_eda
from ui.home import run_home


def main():
    st.title('당뇨 위험도 테스트')

    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        run_ml()






if __name__=='__main__':
    main()