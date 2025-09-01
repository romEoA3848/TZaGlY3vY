# 代码生成时间: 2025-09-01 12:37:14
import streamlit as st
import requests
from requests.exceptions import ConnectionError

"""
网络连接状态检查器
使用Streamlit框架创建，用于检查网络连接状态
"""

# 定义一个函数来检查网络连接状态
def check_connection(url):
    try:
        # 发起一个简单的GET请求
        response = requests.get(url)
        # 如果请求成功，返回True
        return True
    except ConnectionError:
        # 如果发生连接错误，返回False
        return False

# Streamlit页面配置
def main():
    st.title('网络连接状态检查器')
    
    # 让用户输入要检查的URL
    url_input = st.text_input('请输入要检查的URL:', 'https://www.example.com')
    
    # 检查输入是否为空
    if url_input:
        # 使用Streamlit按钮触发网络检查
        if st.button('检查网络连接'):
            # 检查网络连接状态
            is_connected = check_connection(url_input)
            
            # 根据检查结果更新页面信息
            if is_connected:
                st.success('网络连接成功！')
            else:
                st.error('网络连接失败，请检查您的网络设置。')
    else:
        st.warning('请输入一个有效的URL！')

# 运行Streamlit应用
if __name__ == '__main__':
    main()