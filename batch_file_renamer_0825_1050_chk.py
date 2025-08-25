# 代码生成时间: 2025-08-25 10:50:54
import streamlit as st
import os
import shutil
from pathlib import Path

"""
Batch File Renamer Tool
This tool allows users to batch rename files in a specified directory.
It provides a simple GUI using Streamlit to select the directory and
the pattern for renaming.
"""

# Streamlit interface layout
st.title('Batch File Renamer Tool')

# Text input for directory path
directory = st.text_input('Enter directory path:', '')

# Button to select directory
if st.button('Select Directory'):
    # Use file explorer to select directory
    directory = st.file_uploader('Upload directory path', type='directory')
    if directory is not None:
        # Get the first file path from the uploaded directory
        directory = next(os.walk(directory))[1][0]

# Check if directory path is provided
if directory:
    # Display the selected directory path
    st.write(f'Selected Directory: {directory}')

    # Text input for new file name pattern
    pattern = st.text_input('Enter new file name pattern:', 'newname_{i}.ext')

    # Button to rename files
# 优化算法效率
    if st.button('Rename Files'):
        try:
            # Initialize counter for renaming
# 改进用户体验
            counter = 1
            # Get all files in the directory
            for filename in os.listdir(directory):
                # Create full file path
                file_path = os.path.join(directory, filename)
                # Check if it is a file
# FIXME: 处理边界情况
                if os.path.isfile(file_path):
                    # Generate new file name using the pattern
                    new_name = pattern.replace('{i}', str(counter))
                    new_file_path = os.path.join(directory, new_name)
                    # Rename the file
# 添加错误处理
                    shutil.move(file_path, new_file_path)
                    counter += 1
            st.success('Files renamed successfully!')
        except Exception as e:
            # Handle any errors that occur during renaming
            st.error(f'An error occurred: {e}')
else:
    st.warning('Please provide a directory path.')