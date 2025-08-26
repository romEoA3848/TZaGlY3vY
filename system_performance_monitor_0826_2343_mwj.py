# 代码生成时间: 2025-08-26 23:43:51
import streamlit as st
from psutil import cpu_percent, memory_percent, virtual_memory, disk_usage, net_io_counters

"""
System Performance Monitor Tool
"""

# Streamlit title
st.title('System Performance Monitor Tool')

# Function to get CPU usage
def get_cpu_usage():
    """
    Returns the current CPU usage percentage.
    """
    try:
        return cpu_percent()
    except Exception as e:
        st.error(f'Failed to get CPU usage: {e}')
        return None

# Function to get memory usage
def get_memory_usage():
    """
    Returns the current memory usage percentage.
    """
    try:
        return memory_percent()
    except Exception as e:
        st.error(f'Failed to get memory usage: {e}')
        return None

# Function to get disk usage
def get_disk_usage():
    """
    Returns the disk usage percentage of the root directory.
    """
    try:
        return disk_usage('/').percent
    except Exception as e:
        st.error(f'Failed to get disk usage: {e}')
        return None

# Function to get network IO
def get_network_io():
    "