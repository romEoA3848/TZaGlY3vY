# 代码生成时间: 2025-08-09 12:40:21
import streamlit as st
import zipfile
import os
from pathlib import Path

# Streamlit界面标题
st.set_page_config(page_title="Unzip Tool")

# 定义函数来解压文件
def unzip_file(zip_path, extract_to):
    """解压ZIP文件到指定目录。

    参数:
        zip_path (str): ZIP文件的路径。
        extract_to (str): 提取文件的目标目录。
    """
    if not zipfile.is_zipfile(zip_path):
        raise ValueError("The provided file is not a valid zip file.")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# 主函数，用于创建Streamlit界面
def main():
    # 标题
    st.title('File Unzip Tool')

    # 上传ZIP文件
    st.subheader('Upload Zip File')
    zip_file_buffer = st.file_uploader("Choose a zip file", type=['zip'])

    # 如果上传了文件
    if zip_file_buffer is not None:
        # 显示文件信息
        st.write('Uploaded File:', zip_file_buffer.name)
        st.write('File Size:', len(zip_file_buffer), 'bytes')

        # 提取文件的路径
        extract_path = Path('.') / zip_file_buffer.name[:-4]  # 去掉.zip后缀

        # 解压文件
        try:
            unzip_file(zip_file_buffer, extract_path)
            st.success(f'Unzipped files successfully to {extract_path}')
        except Exception as e:
            st.error(f'An error occurred: {str(e)}')

# 运行Streamlit应用
if __name__ == '__main__':
    main()