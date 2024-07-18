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

with st.sidebar:
    st.markdown(
        """
        # NotionHelper
        Your AI Notion Assistant
        """
    )
    st.markdown("---")  # Horizontal line
    st.markdown("### Pages")
    page = st.radio(
        "Select a page",
        ["Formulas", "Templates", "Widgets"],
    )

if page == "Formulas":
    from pages.Formulas import ai_sales_coach
    with st.expander("Instructions"):
        st.markdown("### Instructions")
        st.markdown(
            """
            1. Ask me anything about Notion formulas.
            2. Type your message in the chat box below and press Enter.
            3. I will provide you with the formula and explain how it works.",
            """
        )
    st.markdown("---")  # Horizontal line
    if "messages" not in st.session_state:
        st.session_state.messages = []  # Initialize chat history
        #clear chat history
        st.session_state.messages = []
        # Welcome message
        st.session_state.messages.append({"role": "assistant", "content": "Welcome! Type a message to get started."})
elif page == "Templates":
    from pages.Templates import ai_sales_coach
    with st.expander("Instructions"):
        st.markdown("### Instructions")
        st.markdown(
            """
            1. Ask me anything about Notion templates.
            2. Type your message in the chat box below and press Enter.
            3. I will guide you on how to create the template.",
            """
        )
    st.markdown("---")
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages = []
        st.session_state.messages.append({"role": "assistant", "content": "Welcome! Type a message to get started."})
elif page == "Widgets":
    from pages.Widgets import ai_sales_coach
    with st.expander("Instructions"):
        st.markdown("### Instructions")
        st.markdown(
            """
            1. Ask me anything about Notion widgets.
            2. Type your message in the chat box below and press Enter.
            3. I will guide you on how to create the widget.",
            """
        )
    st.markdown("---")
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages = []
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
    st.session_state.messages.append({"role": "assistant", "content": "Type a message to continue."})
    
