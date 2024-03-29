import streamlit as st
import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta
st.title('내가 찾은 단어 담벼락')

d = st.date_input(
     "When's your birthday",
     datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)


t = st.select_slider(
     '기간 선택',
     options=['10년 전부터', '9년 전부터','8년 전부터','7년 전부터','6년 전부터','5년 전부터','4년 전부터','3년 전부터','2년 전부터','1년 전부터'])

days = int(''.join(list(filter(str.isdigit, t))))

now = datetime.datetime.now().date() #.strftime('%Y-%m-%d')
tt =  datetime.datetime.now().date()-relativedelta(years=days)
st.text(tt)

     
     
     
     
     
@st.cache(allow_output_mutation=True)

def cache_lst():
    lst = []
    return lst

  
lst = cache_lst()
option = st.radio("옵션 선택하기", ("입력", "삭제", '수정'))

if option == '삭제':
  if len(lst) < 1:
    st.success('삭제할 단어가 존재하지 않습니다.')
  else:
    delete = st.multiselect('아래 목록에서 삭제할 단어를 선택하세요.', options=lst)
    if st.button('선택 지우기'):
      for i in delete:
        if i in lst:
          lst.remove(i)
          
      
    if st.button('모두 지우기'):
      del lst[:]
      st.success('단어장이 텅 비었습니다.')
      
if option == '수정':
  if len(lst) < 1:
    st.success('수정할 단어가 존재하지 않습니다.')
  else:
    change_from = st.selectbox('수정할 단어를 선택하세요.', options=lst)
    change_index = lst.index(change_from)
    change_to = st.text_input('아래와 같이 수정합니다.')
    if st.button('수정 완료하기'):
      lst.remove(change_from)
      lst.insert(change_index, change_to)
      
if option == '입력':
  input = st.text_input('추가할 단어를 써 주세요.')
  if input == "":
    st.success('입력할 내용을 적고 입력 버튼을 눌러주세요.')
    st.button('입력하기')
  else : 
    if st.button('입력하기'):
      lst.append(input)
      
st.subheader('기록된 단어 목록')
st.dataframe(lst, width=2000)

