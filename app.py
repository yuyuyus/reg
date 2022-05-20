import streamlit as st

def auth():
    user_id = st.sidebar.text_input('Input Username')
    user_pw = st.sidebar.text_input('Input Password', type='password')
    

    if user_id == 'John1234' and  user_pw == 'password1234': # You can call this auth info from DB or somewhere safe.
        auth_result = True
    else:
        auth_result = False

    return auth_result




def main():
    create_layout()


if __name__ == '__main__':
    main()
