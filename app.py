import streamlit as st
import datetime
import pandas as pd

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
      if st.button('작성 완료하기2'):
         wordlist2=[[write_date, write_word, write_mean, write_example, write_memo]]
         wordlist_df2=pd.DataFrame(wordlist2, columns=column_name)
         wordlist_df.loc[-1] = wordlist_df2
         st.table(wordlist_df2)  #st.dataframe(wordlist_df)
      
         st.success('작성한 내용이 저장되었습니다.')
      '''

                    
          
          
option = st.sidebar.selectbox("단어장 조회 방법을 선택하세요.",
                          ["전체",
                           "기간",
                           "날짜"])

if option == "날짜":
    today = st.sidebar.date_input("날짜를 선택하세요.", datetime.datetime.now())
    
    
from gsheetsdb import connect

url = "https://docs.google.com/spreadsheets/d/1v79IkkTNPr9FP3Z1gsOFE0V32y_LJcJTVUh_tj0frjc/edit?usp=sharing"
conn = connect()
rows = conn.execute(f'SELECT * FROM "{url}"')

df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)

'''
# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["https://docs.google.com/spreadsheets/d/1MevjWxh5MIRMn4ehaYTUBanNxmXNv-tv_fz8UXb86l8/edit#gid=0"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")
'''
    
    
    
