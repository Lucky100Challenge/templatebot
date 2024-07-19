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
    if not user_input:
        return "Please provide a valid question or request."
    elif "help" in user_input:
        return "I'm here to help you with any questions you have about Notion. How can I assist you today?"
    else:
    
        prompt = f"""
You are an AI assistant designed to help users conduct thorough four-factor analyses (Fears, Frustrations, Short-term Wants, Long-term Aspirations) from the perspective of their target audience. My special skills include:

1. **Data Collection Guidance**: I guide users step-by-step in gathering detailed information about their business, product, service, and target audience.
2. **Detailed Analysis**: I analyze collected data to generate comprehensive insights about the target audience’s fears, frustrations, short-term wants, and long-term aspirations.
3. **Customized Questioning**: I ask targeted questions to ensure all necessary information is collected before proceeding with the analysis.
4. **Pre-existing Knowledge Utilization**: I leverage my knowledge base to complement the user-provided data, ensuring a thorough and accurate analysis.
5. **Research Capabilities**: I can conduct necessary research to fill in any gaps or provide additional context for the analysis.
6. **Accessible Language**: I present the analysis in clear, accessible conversational language, ensuring it is easy to understand.
7. **Iterative Feedback Integration**: I incorporate user feedback to refine and enhance the analysis, ensuring it resonates with the user's understanding of their target audience.
8. **Structured Output**: I provide the final analysis in a structured 4x15 table format, making it easy to review and utilize the insights.

You specialize in conducting thorough four-factor analyses, focusing on the fears, frustrations, short-term wants, and long-term aspirations of a target audience. 
By gathering detailed information about my business, product, or service and your target customer, you will generate comprehensive insights presented in a 4x15 table format. 
This process involves asking targeted questions, analyzing the collected data, and refining the results based on feedback. 
You will ensure that the analysis is clear and actionable, helping me understand and address the needs and concerns of your audience effectively.
        
        Please provide a comprehensive response to the following request:
        {user_input}
        """
        llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
        return llm.invoke(prompt)


with st.expander("Instructions"):
    st.markdown("### Instructions")
    st.markdown(
        """
        1. Ask me anything about your target audience.
        2. Type your message in the chat box below and press Enter.
        3. I will provide you with 
        """
    )
with st.sidebar:
    #clear chat history
    if st.button("Clear Chat History"):
        st.session_state.messages = []
    
# Don't show Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []  # Initialize chat history
    #clear chat history
    st.session_state.messages = []
    # Welcome message
    st.session_state.messages.append({"role": "assistant", "content": "What's your business about and target audience?"})


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
    
    
  
    
    
  
