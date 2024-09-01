import streamlit as st
import helper
import pickle
import nltk
import joblib

nltk.download('punkt_tab')
model = joblib.load('model.joblib')
st.header("Quora Duplicate Input Finder")


q1 = st.text_input("Enter your question 1")
q2 = st.text_input("Enter your question 2")

if st.button('Find'):
    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')