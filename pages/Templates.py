import time
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json
from fpdf import FPDF

# Load environment va   riables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")


st.set_page_config(
    page_title="NotionHelper - Your AI Notion Assistant",
    page_icon=":robot:",
    layout="wide",
)


def ai_sales_coach(user_input):
    prompt = f"""
    Your instructions are as follows:

1. **Primary Role**: Provide assistance on all aspects of using Notion, with a focus on formula-related issues. Offer comprehensive, friendly, and knowledgeable advice.

2. **Template Recommendations**: Help users find the best Notion templates by presenting them in a structured markdown format, including title, description, link, and price.

3.   **Prioritizing Knowledge Sources**: Use the provided Notion documents and your understanding of Notion formulas to assist users effectively.

Your role is to also assist users in creating and monetizing Notion templates, offering practical and actionable advice tailored to their experience level. 
You'll focus on providing real-world examples and detailed guidance, avoiding abstract answers and complex legal or financial advice. 
You'll engage users with interactive reply buttons and always end responses with a promotional footer for premium Notion templates.
You'll also assist users with development of the templates; including all blocks, pages and any and all databases. Instructions must be comprehensive so that the user can follow your instructions to develop the templates 

        {user_input}
        """
    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
    return llm.invoke(prompt)


# UI Title
with st.expander("Instructions"):
    st.markdown("### Instructions")
    st.markdown(
        """
        1. Ask me anything about Notion templates.
        2. Type your message in the chat box below and press Enter.
        3. I will guide you on how to create the template.",
        """
    )
st.markdown("---")  # Horizontal line

with st.sidebar:
    #clear chat history
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.session_state.messages.append({"role": "assistant", "content": "Chat history cleared."})


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
