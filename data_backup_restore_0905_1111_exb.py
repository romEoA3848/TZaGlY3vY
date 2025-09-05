# 代码生成时间: 2025-09-05 11:11:36
import streamlit as st
import shutil
import os
from datetime import datetime

"""
Streamlit application for data backup and restore.
This application allows users to backup and restore data from a specified directory.
"""

# Define constants
BACKUP_DIR = "backups"
DATA_DIR = "data"

# Create backup directory if it does not exist
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

def backup_data():
    """
    Backup data from the data directory to the backup directory.
    """
    try:
        # Create timestamped backup directory
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(BACKUP_DIR, f"backup_{timestamp}")
        shutil.copytree(DATA_DIR, backup_path)
        st.success(f"Data backup successful. Backup saved in: {backup_path}")
    except Exception as e:
        st.error(f"Error during backup: {str(e)}")


def restore_data():
    """
    Restore data from the backup directory to the data directory.
    """
    try:
        # List all backup directories
        backups = [d for d in os.listdir(BACKUP_DIR) if os.path.isdir(os.path.join(BACKUP_DIR, d))]
        if backups:
            # Select backup to restore
            backup_to_restore = st.selectbox("Select backup to restore", backups)
            backup_path = os.path.join(BACKUP_DIR, backup_to_restore)
            shutil.rmtree(DATA_DIR)  # Remove existing data directory
            os.makedirs(DATA_DIR)  # Create new data directory
            shutil.copytree(backup_path, DATA_DIR)
            st.success(f"Data restored from: {backup_path}")
        else:
            st.error("No backups found to restore.")
    except Exception as e:
        st.error(f"Error during restore: {str(e)}")

def main():
    """
    Main function to run the Streamlit application.
    """
    st.title("Data Backup and Restore")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Backup")
        backup_button = st.button("Backup Data")
        if backup_button:
            backup_data()
    with col2:
        st.subheader("Restore")
        restore_button = st.button("Restore Data")
        if restore_button:
            restore_data()

if __name__ == "__main__":
    main()