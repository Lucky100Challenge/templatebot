import time
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json
import fpdf as FPDF

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
        You will act as a professional marketer, and copywriter.
        I will tell you about my project and its features, and then you will create me a sales page for it.
        The page is meant to be a sales page for a Gumroad product.
        The page should be designed to convert visitors into customers.
        
        
        
        
        Please provide a comprehensive response to the following request:
        {user_input}
        """
        llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
        return llm.invoke(prompt)


# UI Title
with st.expander("Instructions"):
    st.markdown("### Instructions")
    st.markdown(
        """
        1. Tell me about your product and it's features.
        2. Type your message in the chat box below and press Enter.
        3. I will provide you with a sales page for your Gumroad product.",
        """
    )
    
with st.sidebar:
    #clear chat history
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.session_state.messages.append({"role": "assistant", "content": "Chat history cleared."})
    #line
    st.markdown("---")
    #save chat history to file as pdf
    if st.button("Save Chat History"):
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        for message in st.session_state.messages:
            pdf.cell(200, 10, txt = message["content"], ln = True, align = 'L')
            
        pdf.output("gumroad_chat_history.pdf")

# Don't show Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []  # Initialize chat history
    #clear chat history
    st.session_state.messages = []
    # Welcome message
    st.session_state.messages.append({"role": "assistant", "content": "Welcome! Type a message to get started."})


# Display chat messages
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
        message_placeholder.markdown("Assstiant is typing...")

    # Get and append AI response (with a delay to simulate typing)
    time.sleep(1)  # Adjust the delay as needed
    response = ai_sales_coach(prompt)
    message_placeholder.markdown(response)  # Update the placeholder
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Clear user input after sending message
    st.session_state.messages = st.session_state.messages[-100:]  # Limit chat history to last 100 messages
    
    
  
