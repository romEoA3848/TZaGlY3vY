# 代码生成时间: 2025-09-20 07:29:56
import os
import shutil
# NOTE: 重要实现细节
from streamlit import session, st

"""
Folder Structure Organizer
This Streamlit application allows users to upload a list of files and folders,
# NOTE: 重要实现细节
organize them based on their extensions, and move them to designated folders."""


# Constants for file types and their corresponding folder names
FILE_TYPES = {
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
# TODO: 优化性能
    'documents': ['.pdf', '.doc', '.docx', '.txt'],
    'videos': ['.mp4', '.mov', '.avi'],
    'audio': ['.mp3', '.wav', '.aac'],
    'archives': ['.zip', '.rar', '.tar.gz'],
# 扩展功能模块
    'code': ['.py', '.js', '.java', '.c', '.cpp']
}

# Function to get the folder name based on the file extension
def get_folder_name(file_extension):
    for folder, extensions in FILE_TYPES.items():
        if file_extension in extensions:
            return folder
    return 'others'

# Function to move files to their designated folders
def organize_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
# FIXME: 处理边界情况
            file_extension = os.path.splitext(file)[1].lower()
            folder_name = get_folder_name(file_extension)
            destination_folder = os.path.join(folder_path, folder_name)
            os.makedirs(destination_folder, exist_ok=True)
            shutil.move(file_path, destination_folder)
            print(f'Moved {file_path} to {destination_folder}')

# Streamlit interface
def main():
    st.title('Folder Structure Organizer')
    st.write('Upload a zip file containing your files and folders to organize.')
    uploaded_file = st.file_uploader('Choose a ZIP file', type=['zip'])

    if uploaded_file is not None:
        # Extract the zip file
        with st.spinner('Extracting files...'):
            extract_path = st.text_input('Enter the path to extract files', '/tmp/extracted_files')
# 优化算法效率
            with zipfile.ZipFile(uploaded_file) as zip_ref:
                zip_ref.extractall(extract_path)
                st.success('Files extracted successfully!')
                organize_files(extract_path)
                st.write(f'Files have been organized in {extract_path}')
# 增强安全性
            session_state.extracted_path = extract_path
        with st.expander('Show file organization details'):
            st.code(os.listdir(extract_path))

if __name__ == '__main__':
    main()