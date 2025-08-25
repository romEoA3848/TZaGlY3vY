# 代码生成时间: 2025-08-25 23:16:48
import streamlit as st
import zipfile
import os
from pathlib import Path

"""
Streamlit application for unzipping files.
"""


# 配置页面标题
st.set_page_config(page_title='Unzip Tool', page_icon='📦')

# 创建一个侧边栏并添加文件上传器
with st.sidebar:
    # 文件上传器
    st.title('Upload a zip file')
    uploaded_file = st.file_uploader('Choose a zip file', type='zip')

# 如果用户上传了文件，展示并解压
if uploaded_file is not None:
    # 获取zip文件的文件名
    zip_file_name = uploaded_file.name
    st.write(f'Uploaded File: {zip_file_name}')

    # 清理文件名以确保路径有效
    zip_file_name = zip_file_name.split('/')[-1]  # 移除路径分隔符
    zip_file_name = zip_file_name.replace('.zip', '')  # 移除文件扩展名
    target_dir = Path(zip_file_name)

    # 检查目标文件夹是否存在，如果存在，则提醒用户
    if target_dir.exists():
        st.warning(f'The directory {target_dir} already exists.')
    else:
        # 创建目标目录
        target_dir.mkdir(parents=True)

        try:
            # 解压文件
            with zipfile.ZipFile(uploaded_file, 'r') as zip_ref: zip_ref.extractall(target_dir)
            st.success(f'Files extracted successfully to {target_dir}')
        except zipfile.BadZipFile as e:  # 错误处理：损坏的zip文件
            st.error('The uploaded file is not a valid zip file: ' + str(e))
        except Exception as e:  # 错误处理：其他异常
            st.error(f'An error occurred: {str(e)}')

# 展示解压后的文件列表（如果存在）
if target_dir.exists():
    files_in_dir = [f'{target_dir}/{f}' for f in os.listdir(target_dir)]
    st.write('Files extracted to:', files_in_dir)
