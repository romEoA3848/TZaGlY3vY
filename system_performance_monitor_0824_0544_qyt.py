# 代码生成时间: 2025-08-24 05:44:26
import streamlit as st
import psutil
from datetime import datetime

"""
System Performance Monitor using Streamlit

This script provides a simple system performance monitoring tool, which displays
# FIXME: 处理边界情况
CPU, memory, and disk usage statistics using Streamlit.
# 增强安全性
"""

# Function to get CPU usage
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

# Function to get memory usage
def get_memory_usage():
    memory = psutil.virtual_memory()
# 优化算法效率
    return memory.percent

# Function to get disk usage
def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

# Main Streamlit app
def main():
    # Set the page title
    st.title('System Performance Monitor')
    
    # Get current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    st.write(f'Timestamp: {timestamp}')
    
    try:  # Error handling
        # Display CPU usage
# NOTE: 重要实现细节
        st.subheader('CPU Usage')
        cpu_usage = get_cpu_usage()
# TODO: 优化性能
        st.write(f'CPU Usage: {cpu_usage}%')
        
        # Display memory usage
        st.subheader('Memory Usage')
        memory_usage = get_memory_usage()
        st.write(f'Memory Usage: {memory_usage}%')
# 优化算法效率
        
        # Display disk usage
        st.subheader('Disk Usage')
        disk_usage = get_disk_usage()
        st.write(f'Disk Usage: {disk_usage}%')
    except Exception as e:
        st.error(f'An error occurred: {e}')

if __name__ == '__main__':
    main()