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

#input = st.text_input("검색어를 쓰세요")

import os
import sys
import urllib.request
client_id = "6ZHRcT3n_3XFRz64iWNo"
client_secret = "c9ZUOpIks6"
#word=input('검색어를 입력하세요')
encText = urllib.parse.quote('라면')
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    #print(response_body.decode('utf-8'))
    st.write(response_body.decode('utf-8'))
