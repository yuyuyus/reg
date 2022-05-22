import streamlit as st
import datetime
import pandas as pd
'''
@st.cache(allow_output_mutation=True)
st.sidebar.title('Menu')
menu = st.sidebar.radio("단어장을 작성할지, 조회할지 선택해 주세요.",
                          ("단어장 작성하기",
                           "단어장 조회하기"))

column_name = ['날짜', '단어', '뜻', '예문', '메모']
data_all = []



if menu == "단어장 작성하기":
    write_date = st.date_input("작성 날짜", datetime.datetime.now())
    write_word = st.text_input("단어 입력하는 곳", placeholder="필수 입력")
    write_mean = st.radio("위 단어의 뜻을 입력하시겠습니까?", ("아니오", "예"))
    if write_mean == '예':
       write_mean = st.text_input("뜻 입력하는 곳")
    else: 
       write_mean = '뜻 미입력'

    write_example = st.radio("위 단어의 예문을 입력하시겠습니까?", ("아니오", "예"))
    if write_example == '예':
       write_example = st.text_input("예문 입력하는 곳")
    else: 
       write_example = '예문 미입력'
          
    write_memo = st.radio("추가적으로 메모할 내용이 있습니까?", ("아니오", "예"))
    if write_memo == '예':
       write_memo = st.text_input("메모 입력하는 곳")
    else: 
       write_memo = '메모 미입력'

        
    if st.button('작성 완료하기'):
      wordlist1=list([[write_date, write_word, write_mean, write_example, write_memo]])
      wordlist2=list([[write_date, write_word, write_mean, write_example, write_memo]])

      wordlist_df1=pd.DataFrame(wordlist1, columns=column_name)
      wordlist_df2=pd.DataFrame(wordlist2, columns=column_name)
      

      st.table(wordlist_df1)  #st.dataframe(wordlist_df)
      st.table(wordlist_df2)
      
      wordlist_df1=wordlist_df1.append(wordlist_df2, ignore_index =True)
      st.table(wordlist_df1)
      st.success('작성한 내용이 저장되었습니다.')
'''
      
                    
          
          
option = st.sidebar.selectbox("단어장 조회 방법을 선택하세요.",
                          ["전체",
                           "기간",
                           "날짜"])

if option == "날짜":
    today = st.sidebar.date_input("날짜를 선택하세요.", datetime.datetime.now())

'''    
text = st.text_input("表示したい単語を入力してください")

if 'text_list' not in st.session_state:
  st.session_state["text_list"] = []

col1, col2 = st.columns(2)

with col1:
  if st.button("追加", key=2):
    st.session_state["text_list"].append(text)

with col2:
  if st.button("削除", key=3): 
    st.session_state["text_list"].remove(text)
      
for output_text in st.session_state["text_list"]:
  st.write("", output_text)    
'''
    
    
@st.cache(allow_output_mutation=True)
def cache_lst():
    lst = { }
    return lst
  

lst = cache_lst()
option = st.radio("옵션 선택하기", ("입력", "삭제", '수정'))
if option == '삭제':
  if len(lst) < 1:
    st.success('삭제할 단어가 존재하지 않습니다.')
  else:
    delete = st.multiselect('아래 목록에서 삭제할 단어를 선택하세요.', options=lst)
    if st.button('선택 지우기'):
      lst.extend(delete)
    if st.button('모두 지우기'):
      del lst[:]
      st.success('단어장이 텅 비었습니다.')
elif option == '수정':
  if len(lst) < 1:
    st.success('수정할 단어가 존재하지 않습니다.')
  else:
    change_from = st.selectbox('수정할 단어를 선택하세요.', options=lst)
    change_index = lst.index(change_from)
    change_to = st.text_input('아래와 같이 수정합니다.')
    if st.button('수정 완료하기'):
      lst.remove(change_from)
      lst.insert(change_index, change_to)
elif option == '입력':
  input = st.text_input('추가할 단어를 써 주세요.')
  if input == "":
    st.success('입력할 내용을 적고 입력 버튼을 눌러주세요.')
    st.button('입력하기')
  else : 
    if st.button('입력하기'):
      lst.append(input)


  
    

st.table(lst)

