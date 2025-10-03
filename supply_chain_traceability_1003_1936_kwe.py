# 代码生成时间: 2025-10-03 19:36:52
import streamlit as st
import pandas as pd
import json
from PIL import Image

"""
Supply Chain Traceability Streamlit App
This application enables users to trace the origin of products in a supply chain.
"""

# Function to load and display product data
def load_product_data(file_path):
    try:
        # Load JSON data from file
        with open(file_path, 'r') as file:
            data = json.load(file)
        return pd.DataFrame(data)
    except FileNotFoundError:
        st.error("File not found. Please check the file path.")
        return None
    except json.JSONDecodeError:
        st.error("Invalid JSON format. Please check the file content.")
        return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

# Function to display product details
def display_product_details(data):
    if data is not None and not data.empty:
        st.write("Product Details:")
        st.write(data)
    else:
        st.write("No product data to display.")

# Streamlit App
def main():
    # Set page title and favicon
    st.set_page_config(page_title="Supply Chain Traceability", page_icon="🔍")
    
    # Display a welcome message
    st.title("Supply Chain Traceability App")
    st.write("This app allows you to trace the origin of products in a supply chain.")

    # Add a section for file upload
    file_uploaded = st.file_uploader("Upload a product data JSON file", type=['json'], accept_multiple_files=False)

    # Load and display product data
    if file_uploaded is not None:
        product_data = load_product_data(file_uploaded)
        display_product_details(product_data)

    # Add a section for displaying a product image
    product_image = st.file_uploader("Upload a product image (optional)", type=['jpg', 'jpeg', 'png'], accept_multiple_files=False)
    if product_image is not None:
        st.image(Image.open(product_image), caption='Product Image', use_column_width=True)

# Run the app
if __name__ == '__main__':
    main()