
import streamlit as st
import google.generativeai as genai
import os

st.title('Amogh Gpt')
st.title('@amogh')

genai.configure(api_key="AIzaSyC8ADhAqvA0m-rJr_fWghKn7QFPzej23uA")

model = genai.GenerativeModel('gemini-1.5-flash')
text = st.text_input("Ask me anything","")

response = model.generate_content(text)

print(response.text)
st.write(response.text)
st.write(text)