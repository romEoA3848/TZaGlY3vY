# 代码生成时间: 2025-08-06 00:14:33
import streamlit as st
import os
import shutil
# FIXME: 处理边界情况
from datetime import datetime
from pathlib import Path

# 定义一个函数用于同步文件
# TODO: 优化性能

def sync_files(source, destination):
    # 检查源目录是否存在
    if not os.path.exists(source):
        raise FileNotFoundError("源目录不存在")
# 扩展功能模块

    # 检查目标目录是否存在，如果不存在则创建
    Path(destination).mkdir(parents=True, exist_ok=True)

    # 获取源目录中的所有文件
    for filename in os.listdir(source):
        src_file = os.path.join(source, filename)
        dst_file = os.path.join(destination, filename)

        # 如果是文件，则复制
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dst_file)
            print(f"文件 {filename} 已同步到 {destination}")
        # 如果是目录，则递归同步
        elif os.path.isdir(src_file):
            sync_files(src_file, dst_file)

# Streamlit App 定义
def main():
# NOTE: 重要实现细节
    # 页面标题和介绍
    st.title('文件备份和同步工具')
    st.write('欢迎使用文件备份和同步工具，可以一键同步文件至指定目录。')

    # 选择源目录
    source = st.text_input("输入源目录路径", key='source_path')
    if source and not os.path.exists(source):
        st.error('源目录不存在，请检查路径！')
    else:
        # 选择目标目录
        destination = st.text_input("输入目标目录路径