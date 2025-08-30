# 代码生成时间: 2025-08-31 03:55:57
import streamlit as st
from html import escape

"""Streamlit application for demonstrating XSS protection."""

# Define a function to sanitize input to prevent XSS attacks
def sanitize_input(input_string):
    """Sanitize the input string to prevent XSS attacks."""
    # Escape HTML special characters
    return escape(input_string)

# Define the main function to handle the Streamlit application
def main():
    """Main function to run the Streamlit application."""
    # Create a title for the application
    st.title('XSS Protection Demo')

    # Text input box to take user input
    user_input = st.text_input('Enter text to sanitize:', "Type here...")

    # Check if the user has entered something
    if user_input:
        try:
            # Sanitize the user input
            sanitized_input = sanitize_input(user_input)

            # Display the sanitized and original input for comparison
            st.write(f"Original Input: {user_input}")
            st.write(f"Sanitized Input: {sanitized_input}")
        except Exception as e:
            # Handle any exceptions that may occur during sanitization
            st.error(f"An error occurred: {e}")
    else:
        st.write('Please enter some text to sanitize.')

# Run the Streamlit application
if __name__ == '__main__':
    main()