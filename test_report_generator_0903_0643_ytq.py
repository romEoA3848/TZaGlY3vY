# 代码生成时间: 2025-09-03 06:43:27
import streamlit as st
import pandas as pd
from PIL import Image
import os
import json

"""
Test Report Generator using Streamlit

This application allows users to generate test reports by uploading a test result file.
It can display the results in a structured way and visualize the data.
"""

# Function to load and process test results
def load_test_results(file_path):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            st.error(f"File {file_path} does not exist.")
            return None
        
        with open(file_path, 'r') as file:
            test_results = json.load(file)
            
        # Convert test results to a pandas DataFrame for easier manipulation
        test_df = pd.json_normalize(test_results)
        return test_df
    except json.JSONDecodeError:
        st.error("Invalid JSON file.")
        return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

# Streamlit sidebar for user inputs
def get_user_input():
    # File uploader for test results
    uploaded_file = st.sidebar.file_uploader("Upload Test Results File", type=['json'])
    if uploaded_file is not None:
        # Read the contents of the uploaded file
        file_path = uploaded_file.name
        test_df = load_test_results(uploaded_file)
        return file_path, test_df
    return None, None

# Main function to run the application
def main():
    # Set the page title
    st.title('Test Report Generator')

    # Get user input from the sidebar
    file_path, test_results_df = get_user_input()

    # Check if test results are available
    if test_results_df is not None:
        # Display the test results
        st.write('Test Results:')
        st.dataframe(test_results_df)
        
        # Additional visualizations can be added here
        # such as bar charts, pie charts, etc.
        # st.line_chart(test_results_df['some_column'])

        # Display an image if provided
        with st.expander("Show Report Image"):
            if file_path:
                image_file = file_path.replace('.json', '.png')
                if os.path.exists(image_file):
                    image = Image.open(image_file)
                    st.image(image, use_column_width=True)
                else:
                    st.error("Report image not found.")

if __name__ == '__main__':
    main()