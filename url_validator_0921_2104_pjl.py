# 代码生成时间: 2025-09-21 21:04:54
import streamlit as st
from urllib.parse import urlparse
import requests
import validators

"""
Streamlit application for validating URL links.
"""

# Function to validate URLs
def validate_url(url):
    # Check if the URL is valid according to the validators library
    if not validators.url(url):
        return False, "Invalid URL format."

    # Try to get the response from the URL
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        # Check if the URL is reachable
        if response.status_code == 200:
            return True, "URL is valid and reachable."
        else:
            return False, f"URL is not reachable. Status code: {response.status_code}"
    except requests.RequestException as e:
        return False, f"Error occurred while trying to reach the URL: {str(e)}"

# Streamlit app
def main():
    st.title('URL Validator')
    url_input = st.text_input("Enter the URL to validate: ", "")
    if url_input:
        valid, message = validate_url(url_input)
        if valid:
            st.success(message)
        else:
            st.error(message)

if __name__ == '__main__':
    main()