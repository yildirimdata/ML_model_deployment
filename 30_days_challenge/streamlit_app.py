import streamlit as st

st.write('Hello world!')

if st.button("Say hello"):
    st.write("hello there")
else:
    st.write("goodbye")