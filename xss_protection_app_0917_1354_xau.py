# 代码生成时间: 2025-09-17 13:54:59
import streamlit as st
from html import escape

"""
Streamlit application for demonstrating XSS (Cross-site Scripting) protection.
This application allows users to input text and displays it, but without allowing
the execution of any scripts, hence protecting against XSS attacks.
"""

# Define the title of the application
def main():
    st.title('XSS Attack Protection Demo')

    # Allow user to input their text
    user_input = st.text_input("Enter your text here: ", "")

    # Escape the user input to prevent XSS attacks
    safe_input = escape(user_input)

    # Display the escaped user input
    st.write("Displaying your input safely: ", safe_input)

    # Optional: Include a section to describe what XSS is and how this app protects against it
    st.subheader('About XSS Protection')
    st.write('Cross-site Scripting (XSS) is a type of computer security vulnerability typically found in web applications.')
    st.write('XSS allows attackers to inject malicious scripts into the content being delivered to a user\'s browser.')
    st.write('This application uses Python\'s html.escape function to ensure that any potentially harmful scripts are neutralized.')

if __name__ == '__main__':
    main()