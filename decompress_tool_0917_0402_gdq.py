# 代码生成时间: 2025-09-17 04:02:12
import streamlit as st
import zipfile
import tarfile
import os
from pathlib import Path

"""
压缩文件解压工具
使用Streamlit框架实现一个用户界面，允许用户选择压缩文件并解压到指定目录。
"""

# 函数：解压ZIP文件
def decompress_zip(zip_path, extract_dir):
    """解压ZIP文件到指定目录"""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
            return f"成功解压ZIP文件到 {extract_dir}"
    except Exception as e:
        return f"解压ZIP文件时发生错误：{e}"

# 函数：解压TAR文件
def decompress_tar(tar_path, extract_dir):
    """解压TAR文件到指定目录"""
    try:
        with tarfile.open(tar_path, 'r') as tar_ref:
            tar_ref.extractall(extract_dir)
            return f"成功解压TAR文件到 {extract_dir}"
    except Exception as e:
        return f"解压TAR文件时发生错误：{e}"

# Streamlit应用的主函数
def main():
    st.title('压缩文件解压工具')
    
    # 用户上传压缩文件
    uploaded_file = st.file_uploader('请选择压缩文件', type=['zip', 'tar', 'tar.gz', 'tgz'])
    
    if uploaded_file is not None:
        # 获取文件的扩展名
        file_ext = Path(uploaded_file.name).suffix
        
        # 根据文件类型选择解压函数
        if file_ext in ['.zip']:
            result = decompress_zip(uploaded_file, 'extracted_files')
        elif file_ext in ['.tar', '.tar.gz', '.tgz']:
            result = decompress_tar(uploaded_file, 'extracted_files')
        else:
            result = '不支持的文件格式'
        
        # 显示解压结果
        st.write(result)

if __name__ == '__main__':
    main()