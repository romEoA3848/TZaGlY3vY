# 代码生成时间: 2025-08-12 07:54:23
import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

"""
Web Content Scraper
This Streamlit application is designed to scrape content from a given webpage.
It allows users to input a URL and then displays the scraped content in a structured way.
"""

# Streamlit title
st.title('Web Content Scraper')

# URL input field
url = st.text_input('Enter the URL of the webpage to scrape:', placeholder='https://example.com')

# Button to trigger scraping
if st.button('Scrape Webpage'):
    # Checking if the URL is provided
    if url:
        try:
            # Make a GET request to the specified URL
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all the paragraphs and headings in the webpage
            paragraphs = soup.find_all('p')
            headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

            # Display the extracted content
            st.header('Extracted Content')
            st.subheader('Paragraphs')
            for paragraph in paragraphs:
                st.write(paragraph.text.strip())

            st.subheader('Headings')
            for heading in headings:
                st.write(heading.text.strip())

        except requests.RequestException as e:
            # Handle any request-related errors (e.g., network issues, invalid URL)
            st.error(f'Error fetching the webpage: {e}')
        except Exception as e:
            # Handle any other unforeseen errors
            st.error(f'An unexpected error occurred: {e}')
    else:
        # Inform the user to enter a URL
        st.warning('Please enter a valid URL.')
        