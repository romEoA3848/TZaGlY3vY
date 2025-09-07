# 代码生成时间: 2025-09-08 04:06:33
import streamlit as st
from urllib.parse import urlparse
import requests

"""
Streamlit app to validate the validity of a URL.

This application will take a URL input from the user and validate it using
requests to check if the server responds with a status code in the 200 range.
"""

# Function to validate URL
def is_valid_url(url):
    """
    Validate if the URL is valid and the server responds with a 200 status code.

    Args:
        url (str): The URL to be validated.

    Returns:
        bool: True if the URL is valid and the server responds with a 200 status code, False otherwise.
    """
    try:
        response = requests.head(url)
        return 200 <= response.status_code < 300
    except requests.RequestException as e:
        st.error(f"Error validating URL: {e}")
        return False

# Streamlit app
def main():
    st.title('URL Validator')

    # Input field for URL
    url_input = st.text_input('Enter a URL', '')
    if url_input:
        # Check if URL is valid
        if is_valid_url(url_input):
            st.success('The URL is valid!')
        else:
            st.error('The URL is invalid or the server is not responding.')
    else:
        st.info('Please enter a URL to validate.')

if __name__ == '__main__':
    main()