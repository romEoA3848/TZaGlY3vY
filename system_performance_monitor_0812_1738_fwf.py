# 代码生成时间: 2025-08-12 17:38:06
import streamlit as st
import psutil
import platform
import time
from datetime import datetime

# 获取系统信息的函数
def get_system_info():
    system_info = {
        "OS": platform.system(),
        "Machine": platform.machine(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Processor": platform.processor(),
        "Num CPU": psutil.cpu_count(logical=False),
        "CPU cores": psutil.cpu_count(logical=True),
        "CPU Frequency": psutil.cpu_freq().max,
        "RAM": psutil.virtual_memory().total / (1024 ** 3),  # GB
    }
    return system_info

# 获取CPU使用率的函数
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent()
    return cpu_usage

# 获取内存使用情况的函数
def get_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.used / memory.total * 100
    return memory_usage

# 获取磁盘使用情况的函数
def get_disk_usage():
    disk_usage = {
        "Total": psutil.disk_usage('/').total / (1024 ** 3),  # GB
        "Used": psutil.disk_usage('/').used / (1024 ** 3),  # GB
        "Free": psutil.disk_usage('/').free / (1024 ** 3),  # GB
        "Percentage": psutil.disk_usage('/').percent,
    }
    return disk_usage

# 获取网络使用情况的函数
def get_network_usage():
    network_io = {
        "Sent": psutil.net_io_counters().bytes_sent,
        "Received": psutil.net_io_counters().bytes_recv,
    }
    return network_io

# Streamlit界面
def main():
    st.title('System Performance Monitor')
    system_info_section, cpu_usage_section, memory_usage_section, disk_usage_section, network_usage_section = st.columns(5)

    # 显示系统信息
    with system_info_section:
        st.header('System Information')
        system_info = get_system_info()
        for key, value in system_info.items():
            st.write(f'{key}: {value}')

    # 显示CPU使用率
    with cpu_usage_section:
        st.header('CPU Usage')
        cpu_usage = get_cpu_usage()
        st.write(f'Current CPU Usage: {cpu_usage}%')
        st.line_chart(
            get_cpu_usage(),
            height=200,
            refresh_rate=1000,
        )

    # 显示内存使用情况
    with memory_usage_section:
        st.header('Memory Usage')
        memory_usage = get_memory_usage()
        st.write(f'Current Memory Usage: {memory_usage}%')
        st.line_chart(
            get_memory_usage(),
            height=200,
            refresh_rate=1000,
        )

    # 显示磁盘使用情况
    with disk_usage_section:
        st.header('Disk Usage')
        disk_usage = get_disk_usage()
        for key, value in disk_usage.items():
            st.write(f'{key.capitalize()}: {value}')
        st.bar_chart(
            [disk_usage['Used'], disk_usage['Free']],
            x=['Used', 'Free'],
            y='GB',
        )

    # 显示网络使用情况
    with network_usage_section:
        st.header('Network Usage')
        network_io = get_network_usage()
        for key, value in network_io.items():
            st.write(f'{key.capitalize()}: {value} bytes')
        st.line_chart(
            get_network_usage(),
            height=200,
            refresh_rate=1000,
        )

if __name__ == '__main__':
    main()