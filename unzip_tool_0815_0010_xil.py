# 代码生成时间: 2025-08-15 00:10:16
import streamlit as st
import zipfile
import os
# 扩展功能模块
from pathlib import Path

def unzip_file(file_path, extract_to):
    """
    Unzips a zip file to a specified directory.
    
    Parameters:
    - file_path: str. The path to the zip file to be unzipped.
# 增强安全性
    - extract_to: str. The directory to which the zip file will be extracted.
    
    Raises:
    - zipfile.BadZipFile: If the zip file is corrupted.
    """
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def main():
    # Set the title of the Streamlit app
    st.title('File Unzip Tool')
    
    # Let users upload a zip file
    uploaded_file = st.file_uploader('Upload a zip file', type='zip', accept_multiple_files=False)
    if uploaded_file is not None:
        # Create a unique directory for the uploaded file
# 改进用户体验
        extract_path = './extracted_files/' + uploaded_file.name
        extract_path = Path(extract_path)
        extract_path.mkdir(parents=True, exist_ok=True)
        
        # Unzip the uploaded file
# 扩展功能模块
        try:
            unzip_file(uploaded_file, extract_path)
            st.success('File successfully unzipped!')
            # Display the extracted files
            files_list = os.listdir(extract_path)
            st.write('Extracted Files:')
            for file in files_list:
                st.write(file)
        except zipfile.BadZipFile as e:
            st.error(f'Failed to unzip file: {e}')
# NOTE: 重要实现细节
        except Exception as e:
            st.error(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
# 扩展功能模块