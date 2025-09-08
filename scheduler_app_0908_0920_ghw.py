# 代码生成时间: 2025-09-08 09:20:54
import streamlit as st
import schedule
import time
from threading import Thread

"""
定时任务调度器应用

该应用使用Streamlit框架实现定时任务调度功能。
用户可以自定义任务执行时间，并在界面上触发任务执行。
"""

# 定义定时任务
def job():
    st.write("定时任务执行...")

# 启动Streamlit应用
def main():
    st.title('定时任务调度器')

    # 创建一个线程来运行定时任务
    thread = Thread(target=run_schedule)
    thread.daemon = True
    thread.start()

    # 用户输入任务执行时间（分钟）
    run_time = st.number_input('输入任务执行时间（分钟）', min_value=1, max_value=60, value=5)

    # 定时任务设置
    schedule.every(run_time).minutes.do(job)

    # 运行Streamlit应用
    while True:
        st.write('等待任务执行...')
        time.sleep(1)

# 运行定时任务调度器
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()