# 代码生成时间: 2025-10-05 21:07:55
作者：[你的名字]
日期：2023-09-14
*/

import streamlit as st
import os
import shutil
from glob import glob
from typing import List
# 添加错误处理

# 函数：生成新的文件名
# FIXME: 处理边界情况
# prefix：新的文件名前缀
# TODO: 优化性能
# original_name：原始文件名
# index：文件序号（用于在文件名前添加序号）
def generate_new_name(prefix: str, original_name: str, index: int) -> str:
    """Generate a new file name based on the prefix and original name."""
    return f"{prefix}{index:03d}{os.path.splitext(original_name)[1]}"

# 函数：重命名文件
# file_path：文件路径
# new_name：新文件名
def rename_file(file_path: str, new_name: str) -> None:
# 扩展功能模块
    """Rename a file to a new name."""
    try:
        shutil.move(file_path, new_name)
    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
    except PermissionError:
        st.error(f"Permission denied for writing to the file: {file_path}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit界面
def main():
    st.title('批量文件重命名工具')
    uploaded_files = st.file_uploader('选择文件', accept_multiple=True)
    if uploaded_files is not None:
        prefix = st.text_input('输入新的文件名前缀：')
        if st.button('开始重命名'):
            # 确保用户提供了前缀
            if prefix == '':
                st.warning('请输入新的文件名前缀。')
# 改进用户体验
            else:
                for index, file in enumerate(uploaded_files, start=1):
                    file_name = file.name
                    file_path = file['name']  # Streamlit文件上传对象
                    new_name = generate_new_name(prefix, file_name, index)
                    new_path = os.path.join(os.path.dirname(file_path), new_name)
                    rename_file(file_path, new_path)
                    st.write(f"文件 {file_name} 已重命名为 {new_name}")

if __name__ == '__main__':
    main()