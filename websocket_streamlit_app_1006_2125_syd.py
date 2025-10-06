# 代码生成时间: 2025-10-06 21:25:42
import streamlit as st
def websocket_connected():
    # 显示连接状态
    st.session_state['connected'] = True
def websocket_disconnected():
    # 显示断开连接状态
    st.session_state['connected'] = False

def websocket_message(message_json):
    # 解析接收到的消息
    message = json.loads(message_json)
    # 更新接收消息状态
    st.session_state['message'] = message
    # 打印接收到的消息
    print(f"Received message: {message}")

# 设置页面标题
st.title('WebSocket Streamlit App')

# 检查是否连接
if 'connected' not in st.session_state:
    st.session_state['connected'] = False
if not st.session_state['connected']:
    # 如果没有连接，显示连接按钮
    if st.button('Connect WebSocket'):
        # 连接WebSocket
        from streamlit.components.v1 import html
        import json

        with open('js/socket.js', 'r') as f:
            js = f.read()
        html(
            f"<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.0/socket.io.js"></script>"
            "<script>{js}</script>", height=0
        )
        st.session_state['connected'] = True
        print("WebSocket connected")
else:
    # 如果已连接，显示断开连接按钮
    if st.button('Disconnect WebSocket'):
        st.session_state['connected'] = False
        print("WebSocket disconnected")

# 显示接收到的消息
if 'message' in st.session_state:
    st.write("Received message: ", st.session_state['message'])
