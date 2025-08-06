# 代码生成时间: 2025-08-06 08:55:01
import streamlit as st
# 改进用户体验
import os
import re
# 改进用户体验

"""
Batch File Renamer using Streamlit.
This application allows users to rename multiple files in a directory.
It provides functionality to apply a prefix, suffix, or both to the filenames.
"""

# Function to rename files
def rename_files(directory, prefix, suffix):
    try:
        for filename in os.listdir(directory):
            # Skip if the file is a directory
            if os.path.isdir(os.path.join(directory, filename)):
                continue
# 添加错误处理

            # Construct new filename
            new_filename = f"{prefix}{filename}{suffix}"
# 增强安全性
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        return True
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False

# Streamlit app layout
def main():
    st.title('Batch File Renamer')

    # Directory selection
    st.subheader('Select Directory')
# 添加错误处理
    directory = st.text_input('Enter directory path:', '')
    if st.button('Choose Directory'):
# 添加错误处理
        # Validate directory
        if not os.path.isdir(directory):
            st.error('Invalid directory path.')
        else:
            st.success('Directory selected successfully.')

    # Prefix and suffix input
    st.subheader('Apply Prefix and/or Suffix')
    prefix = st.text_input('Enter prefix (optional):', '')
# 改进用户体验
    suffix = st.text_input('Enter suffix (optional):', '')
# 优化算法效率

    # Rename button
# 扩展功能模块
    if st.button('Rename Files'):
# NOTE: 重要实现细节
        # Check if directory is selected
# TODO: 优化性能
        if not directory:
            st.warning('Please select a directory first.')
        else:
            # Rename files
            if rename_files(directory, prefix, suffix):
                st.success('Files renamed successfully.')
            else:
                st.error('Failed to rename files.')

if __name__ == '__main__':
    main()