# 代码生成时间: 2025-08-04 06:13:42
import streamlit as st
import psutil
from datetime import datetime

"""
System Performance Monitor using Streamlit.
This application allows users to monitor system performance metrics such as CPU, Memory, and Disk usage.
"""

# Function to get CPU usage
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

# Function to get memory usage
def get_memory_usage():
    memory = psutil.virtual_memory()
    return {
        'Total': memory.total / (1024 ** 3),  # GB
        'Available': memory.available / (1024 ** 3),  # GB
        'Used': memory.used / (1024 ** 3),  # GB
        'Percentage': memory.percent
    }

# Function to get disk usage
def get_disk_usage():
    disk_partitions = psutil.disk_partitions()
    disk_usage_list = []
    for partition in disk_partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_usage_list.append({
            'Device': partition.device,
            'Mountpoint': partition.mountpoint,
            'Total Size': usage.total / (1024 ** 3),  # GB
            'Used': usage.used / (1024 ** 3),  # GB
            'Free': usage.free / (1024 ** 3),  # GB
            'Percentage': usage.percent
        })
    return disk_usage_list

# Streamlit app configuration
st.set_page_config(page_title='System Performance Monitor', page_icon='🖥️')

# Side navigation menu
nav, stats, cpu_chart, memory_chart, disk_chart = st.columns(5)

# Navigation selection
if nav.button('CPU Metrics'):
    st.header('CPU Usage')
    cpu_usage = get_cpu_usage()
    st.write(f'CPU Usage: {cpu_usage}%')
    st.line_chart([datetime.now(), datetime.now()], [cpu_usage, cpu_usage], height=200)

# Memory Metrics
if stats.button('Memory Metrics'):
    st.header('Memory Usage')
    memory_usage = get_memory_usage()
    st.write(memory_usage)
    st.line_chart([datetime.now(), datetime.now()], [memory_usage['Percentage'], memory_usage['Percentage']], height=200)

# Disk Metrics
if cpu_chart.button('Disk Metrics'):
    st.header('Disk Usage')
    disk_usage = get_disk_usage()
    for disk in disk_usage:
        st.write(f'Device: {disk[