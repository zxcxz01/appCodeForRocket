## st_chatbot.py
import google.generativeai as genai 
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

## 키 입력해주기
my_api_key = os.getenv("GOOGLE_API_KEY")
# my_api_key = "AIzaSyBxZemX60BWmK25nlhBPAwAZdCW-6Bqs_4"
genai.configure(api_key=my_api_key)

##제목을 위에 적어주기
st.title("Gemini-Bot")
@st.cache_resource
def load_model():
    model = genai.GenerativeModel('gemini-pro')
    print("model loaded...")
    return model

model = load_model()

if "chat_session" not in st.session_state:    
    st.session_state["chat_session"] = model.start_chat(history=[]) 

for content in st.session_state.chat_session.history:
    with st.chat_message("ai" if content.role == "model" else "user"):
        st.markdown(content.parts[0].text)

if prompt := st.chat_input("메시지를 입력하세요."):  # 입력 메시지 컨테이너
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("ai"):
        response = st.session_state.chat_session.send_message(prompt)        
        st.markdown(response.text)
