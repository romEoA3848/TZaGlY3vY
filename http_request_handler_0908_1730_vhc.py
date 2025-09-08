# 代码生成时间: 2025-09-08 17:30:38
import streamlit as st
from requests import get, post, put, delete, RequestException
from streamlit.components.v1 import html

"""
HTTP Request Handler Streamlit App

This application provides a simple interface to send HTTP requests to a specified URL.
It supports GET, POST, PUT, and DELETE methods.

Attributes:
    None

Methods:
    get_request(): Handles GET requests.
    post_request(): Handles POST requests.
    put_request(): Handles PUT requests.
    delete_request(): Handles DELETE requests.
"""

# Define a function to handle GET requests
def get_request(url, params):
    try:
        response = get(url, params=params)
        response.raise_for_status()
        return response.text
    except RequestException as e:
        return f"An error occurred: {e}"

# Define a function to handle POST requests
def post_request(url, json_payload):
    try:
        response = post(url, json=json_payload)
        response.raise_for_status()
        return response.text
    except RequestException as e:
        return f"An error occurred: {e}"

# Define a function to handle PUT requests
def put_request(url, json_payload):
    try:
        response = put(url, json=json_payload)
        response.raise_for_status()
        return response.text
    except RequestException as e:
        return f"An error occurred: {e}"

# Define a function to handle DELETE requests
def delete_request(url):
    try:
        response = delete(url)
        response.raise_for_status()
        return response.text
    except RequestException as e:
        return f"An error occurred: {e}"

# Streamlit app
def main():
    st.title('HTTP Request Handler')
    st.markdown('This app allows you to send HTTP requests to a specified URL.')

    # Input for URL
    url = st.text_input('Enter URL', 'https://example.com')
    # Input for request method
    method = st.selectbox('Select method', ('GET', 'POST', 'PUT', 'DELETE'))

    # Inputs based on selected method
    if method == 'GET':
        params = st.text_input('Enter query parameters (JSON format)', '{}')
        response = get_request(url, params=params)
    elif method == 'POST':
        json_payload = st.text_input('Enter JSON payload', '{}')
        response = post_request(url, json_payload=json_payload)
    elif method == 'PUT':
        json_payload = st.text_input('Enter JSON payload', '{}')
        response = put_request(url, json_payload=json_payload)
    elif method == 'DELETE':
        response = delete_request(url)

    # Display response
    st.write('Response:', html('<pre>' + response + '</pre>', height=400))

if __name__ == '__main__':
    main()
