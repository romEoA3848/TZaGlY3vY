# 代码生成时间: 2025-08-10 12:40:42
import streamlit as st
import psutil
import os
import time

"""
Streamlit application to monitor system performance.
This application provides real-time system performance metrics such as CPU usage, memory usage, disk usage, and network statistics.
"""

@st.cache(ttl=60)  # Cache results for 60 seconds
def fetch_system_metrics():
    """
    Fetches the system metrics including CPU, memory, disk, and network usage.
    """
    with st.spinner('Fetching system metrics...'):
        time.sleep(1)  # Simulate a time delay
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')
        network = psutil.net_io_counters()
        return cpu_usage, memory, disk_usage, network

def main():
    """
    Main function to run the Streamlit application.
    """
    st.title('System Performance Monitor')
    
    # Fetch system metrics
    cpu_usage, memory, disk_usage, network = fetch_system_metrics()

    # Display CPU usage
    st.subheader('CPU Usage')
    st.metric('CPU Usage (%)', cpu_usage)

    # Display memory usage
    st.subheader('Memory Usage')
    st.metric('Total Memory', f'{memory.total / (1024 ** 3):.2f} GB')
    st.metric('Available Memory', f'{memory.available / (1024 ** 3):.2f} GB')
    st.metric('Used Memory', f'{memory.used / (1024 ** 3):.2f} GB')
    st.metric('Memory Usage (%)', memory.percent)

    # Display disk usage
    st.subheader('Disk Usage')
    st.metric('Total Disk Space', f'{disk_usage.total / (1024 ** 3):.2f} GB')
    st.metric('Used Disk Space', f'{disk_usage.used / (1024 ** 3):.2f} GB')
    st.metric('Free Disk Space', f'{disk_usage.free / (1024 ** 3):.2f} GB')
    st.metric('Disk Usage (%)', disk_usage.percent)

    # Display network usage
    st.subheader('Network Usage')
    st.metric('Sent Data', f'{network.bytes_sent / (1024 ** 3):.2f} GB')
    st.metric('Received Data', f'{network.bytes_recv / (1024 ** 3):.2f} GB')

if __name__ == '__main__':
    main()