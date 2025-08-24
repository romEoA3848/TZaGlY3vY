# 代码生成时间: 2025-08-24 22:42:06
import streamlit as st
from bs4 import BeautifulSoup
import requests
import json

"""
Web Page Scraper Streamlit App
===========================

This app allows users to input a URL and get the HTML content of the webpage.
It demonstrates the use of Streamlit for creating web apps and BeautifulSoup for HTML parsing.
"""

# Streamlit sidebar title
st.sidebar.title('Web Page Scraper')

# Streamlit input for URL
url = st.sidebar.text_input('URL', 'https://example.com')

# Function to fetch and return HTML content of the webpage
def fetch_html_content(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        st.error(f'An error occurred: {e}')
        return None

# Function to display the HTML content in the Streamlit app
def display_html_content(html_content):
    if html_content is not None:
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')
        # Display the HTML content as plain text
        st.write(soup.prettify())
    else:
        st.error('Failed to retrieve HTML content.')

# When the user enters a URL and presses the 'Scrape' button
if st.sidebar.button('Scrape'):
    # Fetch the HTML content of the webpage
    html_content = fetch_html_content(url)
    # Display the HTML content in the app
    display_html_content(html_content)