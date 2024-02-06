# 1. install streamlit
# import
import streamlit as st

# title
st.title('Streamlit Lab')

# header
st.header('This is a header')

# body
st.write('This is a body')

# input
st.text_input('Enter your name')
st.text_area('Enter your message')

# button
st.button('Click me!')

# cd StreamlitLab > streamlit run app.py