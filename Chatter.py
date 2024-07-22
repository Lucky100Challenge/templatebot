import time
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json


# Load environment va   riables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")


st.set_page_config(
    page_title="NotionHelper - Your AI Notion Assistant",
    page_icon=":robot:",
    layout="wide",
)



def ai_sales_coach(user_input):
    if not user_input:
        return "Please provide a valid question or request."
    elif "help" in user_input:
        return "I'm here to help you with any questions you have about Notion. How can I assist you today?"
    else:
    
        prompt = f"""
        
        {user_input}
        """
        llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
        return llm.invoke(prompt)


with st.sidebar:
    #clear chat history
    if st.button("Clear Chat History"):
        st.session_state.messages = []
    

    st.session_state.messages = []
    # Welcome message
    st.session_state.messages.append({"role": "assistant", "content": "Welcome! Type a message to get started."})


with st.container():  # Use container for styling
    for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
# User Input
if prompt := st.chat_input("Your message"):
    # Append user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display "Sales Coach is typing..."
    with st.chat_message("assistant"):
        message_placeholder = st.empty() 
        message_placeholder.markdown("Sales Coach is typing...")

    # Get and append AI response (with a delay to simulate typing)
    time.sleep(1)  # Adjust the delay as needed
    if response.contains("sales coach"):
        response = "I'm here to help! What do you need assistance with today?"
    else:
        response = ai_sales_coach(prompt)
    
        st.session_state.messages = []
    response = ai_sales_coach(prompt)
    message_placeholder.markdown(response)  # Update the placeholder
    st.session_state.messages.append({"role": "assistant", "content": response})
  
    
    
  
