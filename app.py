import streamlit as st
from seleniumbase import BaseCase
import cv2
import time

st.title("Streamlit Test")
st.write("hello worlddd")
st.write("""
# MarkDown
> comment
- one
- two
- three
""")

input = st.text_input("검색어를 쓰세요")

from selenium import webdriver

from bs4 import BeautifulSoup

import time

from selenium.webdriver.common.keys import Keys

from urllib.request import urlopen

from urllib.parse import quote_plus

from selenium.webdriver.common.keys import Keys

import time

import sys

from openpyxl import Workbook

import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


wd = webdriver.Chrome('chromedriver',options=options)





# 검색할 단어 리스트 만들기
keyword_list = ['라면']
#kw1=input('단어1의 연관검색어: ')
#keyword_list.append(kw1)



# 검색할 단어 목록 반복하여 크롤링 후 결과 수집
final = {}

for i in range(len(keyword_list)):
    URL = "https://search.naver.com/search.naver?ie=UTF-8&sm=whl_hty&query={}".format(keyword_list[i])
    wd.get(URL)
    wd.implicitly_wait(3)

    searches = wd.find_elements_by_css_selector(".lst_related_srch li")

    temp = []

    for keyword in searches:
        result = keyword.text
        temp.append(result)

    final[keyword_list[i]] = pd.Series(temp)

df = pd.DataFrame(final)

print(df)
