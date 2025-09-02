# 代码生成时间: 2025-09-03 00:35:54
import streamlit as st
from urllib.parse import urlparse
import requests

"""
URL Validator using Streamlit

This program allows users to input a URL and checks its validity.
Appropriate error handling and feedback are provided.
"""

def is_valid_url(url):
    """
    Validates the URL by checking if it is accessible.
    
    Args:
        url (str): The URL to be validated.
        
    Returns:
        bool: True if the URL is valid and accessible, False otherwise.
    """
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException as e:
        # Handle exceptions such as network problems or invalid URLs
        st.error(f"An error occurred: {e}")
        return False

def main():
    """
    Main function to run the Streamlit app.
    """
    st.title('URL Validator')
    
    # Input box for URL
    url_input = st.text_input("Enter a URL to validate:", "")
    
    if st.button('Validate URL'):
        if url_input:
            # Parse the URL to check if it's well-formed
            parsed_url = urlparse(url_input)
            if parsed_url.scheme and parsed_url.netloc:
                if is_valid_url(url_input):
                    st.success("The URL is valid and accessible.")
                else:
                    st.error("The URL is not valid or not accessible.")
            else:
                st.error("Please enter a valid URL with scheme and netloc.")
        else:
            st.error("Please enter a URL to validate.")

if __name__ == '__main__':
    main()