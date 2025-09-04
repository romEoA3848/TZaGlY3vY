# 代码生成时间: 2025-09-04 10:36:16
import streamlit as st
import time
import requests

"""
Performance Test App using Streamlit.
This application allows users to test the performance of a given URL.
"""

# Define the title of the Streamlit application
st.title('Performance Test App')

# Create a text input for the user to enter the URL
url = st.text_input('Enter URL to test:', 'http://example.com')

# Function to perform a GET request and measure the response time
def test_performance(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.elapsed.total_seconds()
    except requests.RequestException as e:
        st.error(f'An error occurred: {e}')
        return None

# Button to trigger the performance test
if st.button('Test Performance'):
    # Check if the URL is not empty
    if url:
        response_time = test_performance(url)
        if response_time is not None:
            st.success(f'The URL responded in {response_time:.2f} seconds.')
        else:
            st.error('Failed to get a response from the URL.')
    else:
        st.warning('Please enter a URL to test.')

# Add space for better readability
st.empty()