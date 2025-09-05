# 代码生成时间: 2025-09-06 06:55:27
import streamlit as st
from streamlit.components.v1 import html
import schedule
import time
from threading import Thread

"""
定时任务调度器 Streamlit 应用
"""

# 定义任务执行的函数
def task_to_schedule():
    st.write("定时任务执行...")
    # 这里添加任务实际执行的代码
    st.write("任务执行完成。")

# 定义定时任务调度函数
def scheduled_job(interval):
    """
    定时任务调度函数
    :param interval: 任务执行的时间间隔（秒）
    """
    while True:
        schedule.run_pending()
        time.sleep(1)

# 设置 Streamlit 页面
def main():
    st.title('定时任务调度器')
    with st.form("task_form"):
        # 获取用户输入的时间间隔
        interval = st.number_input('label', min_value=1, max_value=60, value=5, step=1, format='%d 秒')
        submit_button = st.form_submit_button(label='开始定时任务')

    if submit_button:
        # 如果用户提交了表单，启动定时任务调度
        schedule.every(interval).seconds.do(task_to_schedule)
        # 启动一个线程来运行定时任务，确保 Streamlit 页面不会阻塞
        job_thread = Thread(target=scheduled_job, args=(interval,), daemon=True)
        job_thread.start()
        html("<div style='color: green;' id='success'>任务已启动</div>")
    else:
        html("<div style='color: red;' id='error'>请先设置时间间隔并提交表单</div>")

if __name__ == '__main__':
    main()