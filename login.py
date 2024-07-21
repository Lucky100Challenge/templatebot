import streamlit as st
import os

# Function to read credentials from a file
def load_credentials(file_path):
    credentials = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                user, pwd = line.strip().split(':')
                credentials[user] = pwd
    return credentials

# Function to validate login
def validate_login(username, password, credentials):
    return credentials.get(username) == password

# Load credentials
credentials = load_credentials('credentials.txt')

# Title of the app
st.title("Login Page")

# Login form
username = st.text_input("Username")
password = st.text_input("Password", type='password')
login_button = st.button("Login")

# Check login
if login_button:
    if validate_login(username, password, credentials):
        st.success("Login successful!")
        
        # Display contents of chatter.py
        if os.path.exists('chatter.py'):
            with open('chatter.py', 'r') as f:
                chatter_code = f.read()
            st.code(chatter_code, language='python')
        else:
            st.error("chatter.py not found.")
    else:
        st.error("Invalid username or password.")
