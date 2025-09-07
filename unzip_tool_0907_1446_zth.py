# 代码生成时间: 2025-09-07 14:46:15
import streamlit as st
import zipfile
import os
import shutil

"""
压缩文件解压工具
使用STREAMLIT框架创建一个简单的压缩文件解压工具
"""

def unzip_file(file_path, target_folder):
    """解压缩文件到指定文件夹"""
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(target_folder)
            st.success(f'文件已解压到 {target_folder}')
    except zipfile.BadZipFile:
        st.error('无效的压缩文件')
    except Exception as e:
        st.error(f'解压过程中发生错误：{str(e)}')


def main():
    """主函数"""
    st.title('压缩文件解压工具')
    # 上传压缩文件
    uploaded_file = st.file_uploader("选择一个压缩文件