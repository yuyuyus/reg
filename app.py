import streamlit as st
import datetime
import pandas as pd

st.sidebar.title('Menu')
menu = st.sidebar.radio("단어장을 작성할지, 조회할지 선택해 주세요.",
                          ("단어장 작성하기",
                           "단어장 조회하기"))

if menu == "단어장 작성하기":
    write_date = st.date_input("작성 날짜", datetime.datetime.now())
    write_word = st.text_input("Enter Your First Name", "Type Here ...")
    #write_mean = 
    



column_name = ['날짜', '단어', '뜻', '예', '메모']




option = st.sidebar.selectbox("단어장 조회 방법을 선택하세요.",
                          ["전체",
                           "기간",
                           "날짜"])

if option == "날짜":
    today = st.sidebar.date_input("날짜를 선택하세요.", datetime.datetime.now())

    
    
    
