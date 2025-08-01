# 代码生成时间: 2025-08-01 19:20:26
import streamlit as st
from psutil import Process, AccessDenied, NoSuchProcess
import os

"""
Memory Analysis App

This Streamlit app is designed to provide a user-friendly interface for analyzing memory usage.
It allows users to select a process by name or PID and displays its memory usage statistics.
"""

# Function to get memory usage of a process
def get_memory_usage(process_id):
    try:
        process = Process(process_id)
        mem_info = {
            'Memory Percent': f"{process.memory_percent():.2f}%",
            'RSS (Resident Set Size)': f"{process.memory_info().rss / (1024 * 1024):.2f} MB",
            'VMS (Virtual Memory Size)': f"{process.memory_info().vms / (1024 * 1024):.2f} MB",
        }
        return mem_info
    except AccessDenied:
        return {"error": "Access denied. You don't have permission to inspect this process."}
    except NoSuchProcess:
        return {"error": "Process not found. The process may have already terminated."}
    except Exception as e:
        return {"error": str(e)}

# Streamlit app layout
def main():
    st.title('Memory Usage Analysis Tool')
    st.write('Use this tool to analyze memory usage of any process on your system.')

    # Getting the list of processes to display in the sidebar
    processes = [p.info for p in Process.iter() if p.info['name'] and p.pid != os.getpid()]
    
    # User input for process selection
    process_name = st.sidebar.selectbox(
        'Select a process to analyze memory usage:',
        [proc['name'] for proc in processes],
    )
    
    # Get the corresponding process ID from the process name
    selected_process = next((p.info for p in Process.iter() if p.info['name'] == process_name), None)
    process_id = selected_process['pid'] if selected_process else None

    # Displaying memory usage statistics
    if process_id:
        result = get_memory_usage(process_id)
        st.subheader(f'Memory Usage for {process_name}')
        if 'error' in result:
            st.error(result['error'])
        else:
            for key, value in result.items():
                st.write(f"{key}: {value}")
    else:
        st.error('No process selected or process not found.')

if __name__ == '__main__':
    main()