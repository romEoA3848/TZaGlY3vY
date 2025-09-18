# 代码生成时间: 2025-09-18 22:26:26
import streamlit as st
from html import escape

"""
Streamlit application to demonstrate a simple XSS (Cross Site Scripting) protection.

This application filters user inputs to prevent injection of malicious scripts.
"""


# Function to sanitize user input to prevent XSS attacks
def sanitize_input(user_input):
    """Sanitize the input to prevent XSS attacks."""
    # Use html.escape to encode HTML special characters
    sanitized_input = escape(user_input, quote=False)
    return sanitized_input


def main():
    """Main function to run the Streamlit app."""
    # Set the page title
    st.title('XSS Protection Demo')
    
    # Create a text input field for user input
    user_input = st.text_input("Enter your text:",
                            help="This field accepts user input for demonstration.",
                            key="user_input")
    
    # Display a warning message about potential XSS vulnerabilities
    st.warning("Be cautious with user input to prevent XSS attacks!")
    
    # Check if the user has entered something
    if user_input:
        # Sanitize the user input
        safe_input = sanitize_input(user_input)
        
        # Display the sanitized input
        st.text("Sanitized Input: " + safe_input)
    else:
        st.text("No input provided.")

# Run the app if this file is executed as the main program
if __name__ == '__main__':
    main()