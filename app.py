import streamlit as st
import pickle

# Load the trained model
with open('spam_classifier.pkl', 'rb') as f:
    spam_classifier = pickle.load(f)

# Prediction function
def predict(sentences):
    return spam_classifier.predict(sentences)

# Streamlit UI
st.markdown("<h1 style='text-align: center;'>📩 SMS Spam Detector</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

sentence = st.text_input('Enter an SMS message')

if st.button('Predict'):
    prediction = predict([sentence])[0]
    if prediction.lower() == 'ham':
        st.markdown("<h2 style='text-align: center; color: green;'>✅ This message is NOT spam!</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='text-align: center; color: red;'>🚫 This message IS spam!</h2>", unsafe_allow_html=True)
