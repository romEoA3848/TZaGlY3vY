# 代码生成时间: 2025-09-22 14:12:31
import os
import streamlit as st
from pathlib import Path
import shutil

# 定义帮助函数，用于递归地整理文件夹内的文件
def organize_folder(directory: str, target_folder: str) -> None:
    for root, dirs, files in os.walk(directory):
        for file in files:
            old_file_path = os.path.join(root, file)
            file_extension = file.split('.')[-1] if '.' in file else ''
            new_folder_path = os.path.join(target_folder, file_extension)
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
            new_file_path = os.path.join(new_folder_path, file)
            shutil.move(old_file_path, new_file_path)

# Streamlit 主应用函数
def app():
    st.title('Folder Structure Organizer')
    
    # 用户输入源文件夹和目标文件夹
    source_dir = st.text_input('Enter the source directory path', 'C:/Users/YourName/Documents')
    target_dir = st.text_input('Enter the target directory path', 'C:/Users/YourName/Documents/Organized')
    
    # 检查输入路径是否存在
    if not os.path.exists(source_dir):
        st.error('Source directory does not exist.')
        return
    if not os.path.exists(target_dir):
        st.error('Target directory does not exist.')
        return
    
    # 用户点击按钮开始整理文件夹结构
    if st.button('Organize Folders'):
        try:
            organize_folder(source_dir, target_dir)
            st.success('Folders have been organized successfully.')
        except Exception as e:
            st.error(f'An error occurred: {e}')

if __name__ == '__main__':
    app()