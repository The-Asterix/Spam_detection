import streamlit as st
import joblib

spam_classifier = joblib.load('spam_classifier.joblib')

def predict(sentences):
    y_pred = spam_classifier.predict(sentences)
    return y_pred

st.markdown("<h1 style='text-align: center;'>SMS Spam Detector</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

sentence = st.text_input('Enter an SMS message')

if st.button('Predict'):
    prediction = predict([sentence])[0]
    if prediction == 0:
        st.markdown("<h2 style='text-align: center; color: green;'>This message is not spam!</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='text-align: center; color: red;'>This message is spam!</h2>", unsafe_allow_html=True)