import streamlit as st
import datetime

option = st.sidebar.selectbox("단어장 조회 방법을 선택하세요.",
                          ["전체",
                           "기간",
                           "날짜"])

if option == "날짜":
    today = st.sidebar.date_input("날짜를 선택하세요.", datetime.datetime.now())
