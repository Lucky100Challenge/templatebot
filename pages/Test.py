import streamlit as st
import google_bard
from dotenv import load_dotenv

# Load environment variables
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
        llm = google_bard.generate_text(prompt, api_key)
        return llm
    
with st.sidebar:
    #clear chat history
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        
# Don't show Chat History
st.markdown(
    """
    <style>
        .st-eb {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

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
        
    # Get response from AI
    response = ai_sales_coach(prompt)
    
    # Append AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response)
        
# Clear user input after sending message
st.session_state.messages = st.session_state.messages[-100:]  # Limit chat history to last 100 messages
        
        
