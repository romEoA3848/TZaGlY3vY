# 代码生成时间: 2025-08-26 14:59:17
import os
import streamlit as st
from pathlib import Path

"""
Folder Structure Organizer
This application allows users to organize the folder structure by moving files into subfolders.
"""

# Streamlit setup
st.title('Folder Structure Organizer')
st.write("This application helps you organize your folder structure by moving files into subfolders.")

# Function to create subfolder structure
def create_subfolders(directory_path, extension=None):
    """
# TODO: 优化性能
    Create subfolders for each file extension if provided.
    :param directory_path: Path to the directory to organize.
    :param extension: Optional file extension to filter files.
    """
    try:
        if not os.path.exists(directory_path):
            st.error(f"The directory '{directory_path}' does not exist.")
            return

        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            if os.path.isfile(item_path):
                if extension and not item.endswith(extension):
                    continue
                extension_folder = Path(directory_path) / f".{item.split('.')[-1]}"
                extension_folder.mkdir(exist_ok=True)
                os.replace(item_path, extension_folder / item)
# 增强安全性
    except Exception as e:
# 扩展功能模块
        st.error(f"An error occurred: {e}")

# Streamlit file uploader
# 扩展功能模块
uploaded_file = st.file_uploader("Choose a folder", type="directory")
if uploaded_file is not None:
    # Get the directory path
    directory_path = Path(uploaded_file.name)
    # Get file extension from user input
    file_extension = st.text_input("Enter a file extension to organize by (optional, leave blank for all files)")

    if st.button('Organize Folder'):
        create_subfolders(directory_path, extension=file_extension)
        st.success("Folder structure organized successfully!")
        # Optionally, clear the file input field after processing
        st.experimental_rerun()

# Error handling for file upload
else:
# TODO: 优化性能
    st.warning("Please upload a folder to organize.")