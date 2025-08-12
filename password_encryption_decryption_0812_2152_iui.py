# 代码生成时间: 2025-08-12 21:52:29
import streamlit as st
from cryptography.fernet import Fernet

"""
密码加密解密工具
使用STREAMLIT框架创建的密码加密解密工具，可以方便地在网页上进行密码的加密和解密操作。
"""

# 初始化Fernet对象，用于生成密钥
def generate_key():
    return Fernet.Fernet.generate_key()

# 生成密钥
key = generate_key()

# 初始化Fernet对象
cipher_suite = Fernet(key)

# 加密函数
def encrypt(text):
    return cipher_suite.encrypt(text.encode())

# 解密函数
def decrypt(encrypted_text):
    try:
        return cipher_suite.decrypt(encrypted_text).decode()
    except Exception as e:
        return f"解密失败: {e}"

# 设置页面布局
st.title('密码加密解密工具')

# 用户输入
text = st.text_input('输入待加密或待解密的文本')
action = st.radio('请选择操作', ('加密', '解密'))

# 显示密钥
st.write(f'密钥: {key}')

if text:
    if action == '加密':
        # 执行加密操作
        encrypted_text = encrypt(text)
        st.write(f'加密后的文本: {encrypted_text}')
    elif action == '解密':
        # 执行解密操作
        decrypted_text = decrypt(text)
        st.write(f'解密后的文本: {decrypted_text}')
