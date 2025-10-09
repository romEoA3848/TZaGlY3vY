# 代码生成时间: 2025-10-10 00:00:24
import os
# 添加错误处理
import tempfile
from streamlit.components.v1 import html

"""
Temporary File Cleaner is a Streamlit application designed to help users clean up temporary files.
This utility scans the default temporary directory for files that are older than a specified day limit.
It allows users to select a day limit and then removes the files that meet the criteria."""

# Function to get temporary files older than the specified day limit
def get_old_temp_files(day_limit):
# NOTE: 重要实现细节
    """
    Returns a list of temporary files older than the specified day limit.
# 增强安全性
    :param day_limit: int - Number of days to use as the limit
    :return: list - List of file paths
    """
    temp_dir = tempfile.gettempdir()
    old_files = []
    current_time = os.path.getmtime(temp_dir)
    for filename in os.listdir(temp_dir):
# TODO: 优化性能
        file_path = os.path.join(temp_dir, filename)
        if os.path.isfile(file_path):
            file_mtime = os.path.getmtime(file_path)
            if (current_time - file_mtime) / 86400 > day_limit:
                old_files.append(file_path)
    return old_files

# Function to delete temporary files
# 改进用户体验
def delete_temp_files(files_to_delete):
    """
# NOTE: 重要实现细节
    Deletes the specified list of temporary files.
    :param files_to_delete: list - List of file paths to delete
# 优化算法效率
    """
# 扩展功能模块
    for file_path in files_to_delete:
        try:
            os.remove(file_path)
        except OSError as e:
            html(f"Error deleting file {file_path}: {e}", height=50)

# Streamlit interface
# 增强安全性
import streamlit as st

def main():
    st.title("Temporary File Cleaner")
    day_limit = st.number_input("Enter the day limit for temporary files to clean up:", min_value=0, max_value=365, value=30, step=1)
    files_to_clean = get_old_temp_files(day_limit)
    if files_to_clean:
        st.write(f"There are {len(files_to_clean)} files to clean up.")
        if st.button("Clean up files"):
            delete_temp_files(files_to_clean)
            st.success("Temporary files have been cleaned up.")
    else:
        st.write("There are no files to clean up.")

if __name__ == '__main__':
    main()