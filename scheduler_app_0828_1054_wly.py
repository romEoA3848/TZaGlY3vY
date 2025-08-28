# 代码生成时间: 2025-08-28 10:54:01
import streamlit as st
import schedule
import time
from datetime import datetime

"""
定时任务调度器应用
使用 STREAMLIT 框架创建的定时任务调度器，可以添加任务并设置执行时间。
"""

# 初始化 Streamlit 应用
st.title('定时任务调度器')

# 任务列表，用于存储所有任务
tasks = {}

# 定义添加任务的函数
def add_task(name, schedule_time):
    """
    添加一个新的定时任务
    :param name: 任务名称
    :param schedule_time: 任务执行的时间（格式为 '分钟 小时'）
    """
    # 解析任务执行的时间
    minutes, hours = map(int, schedule_time.split())
    task_id = st.session_state.get('task_count', 0) + 1
    st.session_state['task_count'] = task_id

    # 添加任务到调度器
    schedule.every().day.at(f"{hours:02d}:{minutes:02d}").do(lambda: print(f"Task {name} executed at {datetime.now()}"))
    tasks[task_id] = {'name': name, 'time': f"{hours:02d}:{minutes:02d}"}
    st.write(f"Task {name} added at {schedule_time}")

# 定义清除任务的函数
def clear_tasks():
    """
    清除所有定时任务
    """
    schedule.clear()
    tasks.clear()
    st.write("All tasks cleared")

# 定义启动调度器的函数
def start_scheduler():
    "