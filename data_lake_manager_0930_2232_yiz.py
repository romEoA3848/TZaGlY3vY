# 代码生成时间: 2025-09-30 22:32:53
import streamlit as st
import pandas as pd
import os
from typing import Any

"""
Data Lake Management Tool
=====================

This tool allows users to manage data lakes by creating, reading, updating, and deleting data files.
"""

# Define constants for directories and file types
DATA_DIR = "data_lake/"
ALLOWED_EXTENSIONS = {'csv', 'json', 'parquet'}

# Initialize Streamlit app
def main():
    st.title("Data Lake Management Tool")
    
    page = st.sidebar.selectbox(
        "Choose a page",
        ("Home", "Create", "Read", "Update", "Delete")
    )
    
    if page == "Home":
        home()
    elif page == "Create":
        create()
    elif page == "Read":
        read()
    elif page == "Update":
        update()
    elif page == "Delete":
        delete()
        
# Home page
def home():
    st.write("Welcome to the Data Lake Management Tool")
    st.write("This tool allows you to manage your data lake by creating, reading, updating, and deleting data files.")
    
# Create page
def create():
    st.subheader("Create Data File")
    file_type = st.selectbox("Select file type", ALLOWED_EXTENSIONS)
    file_name = st.text_input("Enter file name")
    file_content = st.text_area("Enter file content")
    
    if st.button("Create File"):
        try:
            create_file(file_type, file_name, file_content)
            st.success("File created successfully")
        except Exception as e:
            st.error(f"Error creating file: {e}")
            
# Read page
def read():
    st.subheader("Read Data File")
    file_name = st.text_input("Enter file name")
    if st.button("Read File\):
        try:
            file_content = read_file(file_name)
            st.write(file_content)
        except Exception as e:
            st.error(f"Error reading file: {e}")
    
# Update page
def update():
    st.subheader("Update Data File")
    file_name = st.text_input("Enter file name\)
    new_content = st.text_area("Enter new file content\)
    if st.button("Update File\):
        try:
            update_file(file_name, new_content)
            st.success("File updated successfully\)
        except Exception as e:
            st.error(f"Error updating file: {e}")
    
# Delete page
def delete():
    st.subheader("Delete Data File\)
    file_name = st.text_input("Enter file name\)
    if st.button("Delete File\):
        try:
            delete_file(file_name)
            st.success("File deleted successfully\)
        except Exception as e:
            st.error(f"Error deleting file: {e}")
            
# Helper function to create a file
def create_file(file_type: str, file_name: str, file_content: str) -> None:
    file_path = os.path.join(DATA_DIR, f"{file_name}.{file_type}")
    with open(file_path, "w\) as file:
        file.write(file_content)

# Helper function to read a file
def read_file(file_name: str) -> Any:
    file_path = os.path.join(DATA_DIR, f"{file_name}.*\)
    for file in os.listdir(DATA_DIR):
        if file.startswith(file_name):
            with open(os.path.join(DATA_DIR, file), "r\) as file:
                return file.read()
    raise FileNotFoundError(f"No file found with name {file_name}")

# Helper function to update a file
def update_file(file_name: str, new_content: str) -> None:
    file_path = os.path.join(DATA_DIR, f"{file_name}.*\)
    for file in os.listdir(DATA_DIR):
        if file.startswith(file_name):
            with open(os.path.join(DATA_DIR, file), "w\) as file:
                file.write(new_content)
            return
    raise FileNotFoundError(f"No file found with name {file_name}")

# Helper function to delete a file
def delete_file(file_name: str) -> None:
    file_path = os.path.join(DATA_DIR, f"{file_name}.*\)
    for file in os.listdir(DATA_DIR):
        if file.startswith(file_name):
            os.remove(os.path.join(DATA_DIR, file))
            return
    raise FileNotFoundError(f"No file found with name {file_name}")

if __name__ == "__main__":
    main()