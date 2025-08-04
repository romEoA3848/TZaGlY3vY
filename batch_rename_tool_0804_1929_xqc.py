# 代码生成时间: 2025-08-04 19:29:07
import streamlit as st
import os
from pathlib import Path

"""
Batch Rename Tool using Streamlit.
This tool allows users to select a directory and a naming pattern, then renames all files in the directory according to the pattern.
"""

# Define the title of the application
st.title('Batch File Rename Tool')

# Create a sidebar for user input
with st.sidebar:
    # Text input for the directory path
    dir_path = st.text_input('Enter the directory path:', '/path/to/directory')
    # Checkbox to confirm if the user wants to preview changes
    preview_changes = st.checkbox('Preview changes only', value=True)
    # Text input for the naming pattern
    pattern = st.text_input('Enter the naming pattern:', 'file_{:03d}.ext')

# Function to rename files in the directory
def rename_files(directory, pattern, preview=False):
    path = Path(directory)
    if not path.exists():
        raise ValueError(f"The directory {directory} does not exist.")
    if not path.is_dir():
        raise ValueError(f"The path {directory} is not a directory.")

    for idx, file in enumerate(path.iterdir()):
        if file.is_file():
            new_name = pattern.format(idx + 1)
            new_path = path / new_name
            if not preview:
                file.rename(new_path)
            print(f'Renamed {file} to {new_path}')

# Function to validate the user input
def validate_input(dir_path, pattern):
    return dir_path and pattern and os.path.isdir(dir_path)

# Main execution block
if st.button('Rename Files'):
    if validate_input(dir_path, pattern):
        try:
            rename_files(dir_path, pattern, preview_changes)
            st.success('Files renamed successfully!')
        except ValueError as ve:
            st.error(ve)
        except Exception as e:
            st.error(f'An error occurred: {e}')
    else:
        st.error('Please enter a valid directory path and naming pattern.')

# Display the preview (if selected)
if preview_changes:
    try:
        rename_files(dir_path, pattern, preview=True)
        st.write('Preview of renamed files:')
    except Exception as e:
        st.error(f'An error occurred during preview: {e}')
