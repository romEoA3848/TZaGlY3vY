# 代码生成时间: 2025-09-08 21:16:13
import streamlit as st
import requests
from urllib.parse import urlparse

"""
Streamlit application for validating URL links.

This application takes a URL as input and checks if it is valid and accessible.
"""
# 增强安全性

def is_valid_url(url):
    """
    Validates the given URL.
    
    Args:
# 添加错误处理
        url (str): The URL to validate.
    
    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def check_url_accessibility(url):
    """
    Checks if the URL is accessible.
    
    Args:
# 扩展功能模块
        url (str): The URL to check.
    
    Returns:
        bool: True if the URL is accessible, False otherwise.
    """
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def main():
    """
# NOTE: 重要实现细节
    The main function of the application.
    """
    st.title('URL Validator')
    
    # Create a text input for the user to enter the URL
    url_input = st.text_input('Enter a URL to validate:', '')
    
    if st.button('Validate URL'):
        if url_input:
            if is_valid_url(url_input):
                if check_url_accessibility(url_input):
                    st.success(f"The URL '{url_input}' is valid and accessible.")
# NOTE: 重要实现细节
                else:
                    st.error(f"The URL '{url_input}' is valid but not accessible.")
            else:
# 扩展功能模块
                st.error(f"The URL '{url_input}' is not valid.")
# TODO: 优化性能
        else:
            st.warning('Please enter a URL to validate.')

if __name__ == '__main__':
    main()