# 代码生成时间: 2025-08-06 21:14:25
import streamlit as st
import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

# 定时任务调度器 Streamlit 应用
class ScheduledTaskScheduler:
    def __init__(self):
        # 初始化调度器
        self.scheduler = BackgroundScheduler(
            jobstores={'default': st.scheduler.JobStore()},
            executors={'default': ThreadPoolExecutor(20)},
            event_executor=ThreadPoolExecutor(2)
        )
        # 注册事件监听器
        self.scheduler.add_listener(self.job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

    def job_listener(self, event):
        # 事件监听器，用于接收任务执行结果
        if event.exception:
            st.error(f"Job '{event.job_id}' raised an exception: {event.exception}")
        elif event.code:
            st.error(f"Job '{event.job_id}' returned error code {event.code}")
        else:
            st.success(f"Job '{event.job_id}' executed successfully")

    def add_job(self, func, trigger, args=None, kwargs=None, id=None, replace_existing=False):
        # 添加任务到调度器
        if args is None:
            args = []
        if kwargs is None:
            kwargs = {}
        try:
            self.scheduler.add_job(func, trigger, args=args, kwargs=kwargs, id=id, replace_existing=replace_existing)
            st.success(f"Job '{id}' added successfully")
        except Exception as e:
            st.error(f"Failed to add job '{id}': {e}")

    def remove_job(self, job_id):
        # 从调度器移除任务
        try:
            self.scheduler.remove_job(job_id)
            st.success(f"Job '{job_id}' removed successfully")
        except JobLookupError:
            st.error(f"Job '{job_id}' not found")

    def run(self):
        # 启动调度器
        self.scheduler.start()
        st.text("Scheduler started.")

if __name__ == '__main__':
    # 创建应用
    scheduler_app = ScheduledTaskScheduler()

    # 添加一个定时任务，每5秒执行一次
    scheduler_app.add_job(st.echo, 'interval', args=['Hello world!'], id='echo_job', replace_existing=True)

    # 启动应用
    scheduler_app.run()

    # 保持应用运行
    while True:
        time.sleep(1)