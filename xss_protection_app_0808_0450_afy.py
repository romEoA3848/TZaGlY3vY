# 代码生成时间: 2025-08-08 04:50:06
import streamlit as st

"""
Streamlit application to demonstrate a simple XSS attack prevention mechanism.
"""

# Importing necessary libraries
from bs4 import BeautifulSoup
import html

# Function to sanitize input to prevent XSS attacks
def sanitize_input(input_text):
    """
    Sanitizes the input text to remove any potentially malicious scripts.
    
    Args:
        input_text (str): The text to be sanitized.
    
    Returns:
        str: Sanitized text.
    """
    # Use BeautifulSoup to parse the text and strip out malicious tags
    soup = BeautifulSoup(input_text, 'html.parser')
    # Remove all script and iframe tags
    for script in soup(["script", "iframe"]):
        script.decompose()
    # Return the sanitized text
    return str(soup)

# Create a Streamlit application
def main():
    st.title('XSS Attack Protection Demo')
    
    # Input box for user to enter text
    user_input = st.text_input('Enter text here', '', key='user_input')
    
    # Check if the user has entered some text
    if user_input:
        try:
            # Sanitize the user input
            sanitized_text = sanitize_input(user_input)
            # Display the sanitized text
            st.text_area('Sanitized Text:', sanitized_text, height=200)
        except Exception as e:
            # Handle any exceptions that occur during sanitization
            st.error(f'An error occurred: {str(e)}')
    else:
        st.write('Please enter some text to see the sanitized output.')

if __name__ == '__main__':
    main()