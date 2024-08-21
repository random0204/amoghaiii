import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyC8ADhAqvA0m-rJr_fWghKn7QFPzej23uA")
t
model = genai.GenerativeModel('gemini-1.5-flash')
text = st.text_input("Ask me anything","")

response = model.generate_content(text)

print(response.text)
st.write(response.text)