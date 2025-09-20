# 代码生成时间: 2025-09-20 23:09:47
import streamlit as st
from psutil import cpu_percent, virtual_memory, disk_usage, net_io_counters, users
import time

"""
System Performance Monitor using Streamlit

This Streamlit application monitors system performance metrics such as CPU usage,
memory usage, disk usage, network IO, and logged-in users.
"""

# Function to get CPU usage
def get_cpu_usage():
    return cpu_percent(interval=1)

# Function to get memory usage
def get_memory_usage():
    return virtual_memory().percent

# Function to get disk usage
def get_disk_usage():
    return disk_usage('/').percent

# Function to get network IO
def get_network_io():
    return {
        "bytes_sent": net_io_counters().bytes_sent,
        "bytes_recv": net_io_counters().bytes_recv
    }

# Function to get logged-in users
def get_logged_in_users():
    return len(users())

# Main Streamlit application
def main():
    st.title('System Performance Monitor')

    with st.expander('CPU Usage'):
        st.metric('CPU Usage (%)', get_cpu_usage())

    with st.expander('Memory Usage'):
        st.metric('Memory Usage (%)', get_memory_usage())

    with st.expander('Disk Usage'):
        st.metric('Disk Usage (%)', get_disk_usage())

    with st.expander('Network IO'):
        st.metric('Bytes Sent', get_network_io()['bytes_sent'])
        st.metric('Bytes Received', get_network_io()['bytes_recv'])

    with st.expander('Logged-In Users'):
        st.metric('Logged-In Users', get_logged_in_users())

    # Refresh the application every 5 seconds
    st.empty()
    st.text('Refreshing every 5 seconds...')
    time.sleep(5)

# Run the Streamlit application
if __name__ == '__main__':
    main()