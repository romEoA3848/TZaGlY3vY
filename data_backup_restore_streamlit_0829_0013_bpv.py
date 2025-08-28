# 代码生成时间: 2025-08-29 00:13:30
import streamlit as st
import os
import shutil
import json
from datetime import datetime

"""
Data Backup and Restore application using Streamlit.
This application allows users to backup and restore data through a simple GUI.
"""

# Define the title of the Streamlit application
st.title('Data Backup and Restore')

# Function to backup data
def backup_data(directory_path, backup_name):
    """
    Function to backup data from the specified directory and save it with a timestamp.
    :param directory_path: Path to the directory to be backed up
    :param backup_name: Base name of the backup file
    """
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_path = f"{backup_name}_{timestamp}.zip"
    try:
        shutil.make_archive(backup_path, 'zip', directory_path)
        st.success(f'Backup successful. File saved as: {backup_path}')
    except Exception as e:
        st.error(f'An error occurred while backing up data: {str(e)}')

# Function to restore data
def restore_data(backup_path, restore_directory):
    """
    Function to restore data from a backup file to the specified directory.
    :param backup_path: Path to the backup file
    :param restore_directory: Path to the directory where data will be restored
    """
    try:
        shutil.unpack_archive(backup_path, restore_directory, 'zip')
        st.success(f'Data restored successfully to: {restore_directory}')
    except Exception as e:
        st.error(f'An error occurred while restoring data: {str(e)}')

# Get user input for backup
with st.form(key='backup_form'):
    dir_path = st.text_input('Enter the directory path to backup:', '/path/to/data')
    backup_name = st.text_input('Enter the backup file name:', 'data_backup')
    backup_button = st.form_submit_button(label='Backup Data')

    if backup_button:
        backup_data(dir_path, backup_name)

# Get user input for restore
with st.form(key='restore_form'):
    backup_file_path = st.file_uploader('Choose a backup file to restore:', type=['zip'])
    restore_dir = st.text_input('Enter the directory path to restore:', '/path/to/restore')
    restore_button = st.form_submit_button(label='Restore Data')

    if restore_button and backup_file_path is not None:
        restore_data(backup_file_path, restore_dir)
        # Clear the file uploader to allow new uploads
        st.empty()
        st.empty()
        st.empty()
        st.empty()