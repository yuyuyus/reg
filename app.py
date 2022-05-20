import streamlit as st

def auth():
    user_id = st.sidebar.text_input('Input Username')
    user_pw = st.sidebar.text_input('Input Password', type='password')
    

def main():
    create_layout()


if __name__ == '__main__':
    main()
