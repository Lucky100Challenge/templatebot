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

# Dashboard with cards for each helper
st.markdown("# Notion Helper")
st.markdown("Welcome to Notion Helper! Choose a helper below to get started.")
st.markdown("---")  # Horizontal line

# Helper selection
helper = st.radio(
    "Select a helper:",
    ["Formulas", "Widgets", "Templates"],
    index=0,
)

# Load the selected helper
if helper == "Formulas":
    from pages.Formulas import ai_sales_coach

    ai_sales_coach()
elif helper == "Widgets":
    from pages.Widgets import ai_sales_coach

    ai_sales_coach()
elif helper == "Templates":
    from pages.Templates import ai_sales_coach

    ai_sales_coach()
else:
    st.error("Invalid helper selected. Please select a valid helper.")

    