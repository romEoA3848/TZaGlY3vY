# 代码生成时间: 2025-08-09 02:17:58
import streamlit as st
import pandas as pd
import numpy as np

"""
Data Cleaning and Preprocessing Tool using Streamlit
"""

# Streamlit title
st.title('Data Cleaning and Preprocessing Tool')

# Sidebar to upload data
file_buffer = st.sidebar.file_uploader("Choose a CSV file", type=['csv'])

def clean_data(df):
    """
    Cleans the data by handling missing values and duplicates.
    Args:
        df (pd.DataFrame): The input DataFrame to clean.
    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    try:
        # Drop duplicates
        df = df.drop_duplicates()
        
        # Fill missing values
        df = df.fillna(method='ffill')
        
        return df
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Function to display the data
def display_data(df):
    """
    Displays the DataFrame in the Streamlit app.
    Args:
        df (pd.DataFrame): The DataFrame to display.
    """
    if df is not None:
        st.subheader('Original Data')
        st.write(df.head())
        st.subheader('Cleaned Data')
        st.write(df.head())
    else:
        st.error('No data to display.')

# Main functionality
if file_buffer is not None:
    # Read the data
    df = pd.read_csv(file_buffer)
    
    # Clean the data
    cleaned_df = clean_data(df)
    
    # Display the data
    display_data(cleaned_df)