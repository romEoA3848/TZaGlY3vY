# 代码生成时间: 2025-09-15 02:18:12
import streamlit as st
from cryptography.fernet import Fernet
import base64
import binascii

"""
密码加密解密工具
"""
# 初始化Streamlit界面
def main():
    st.title('密码加密解密工具')
    
    # 文档字符串
    with st.form('encryption_decryption_form'):
        """
        用户输入密码并选择操作（加密或解密）
        """
        password = st.text_input('输入密码')
        operation = st.selectbox(
            '操作',
            ['加密', '解密']
        )
        submit_button = st.form_submit_button(label='执行')
        
    # 检查用户是否提交了表单
    if submit_button:
        if operation == '加密':
            # 加密密码
            encrypted_password = encrypt_password(password)
            st.success(f'加密后的密码: {encrypted_password}')
        elif operation == '解密':
            # 解密密码
            try:
                decrypted_password = decrypt_password(password)
                st.success(f'解密后的密码: {decrypted_password}')
            except ValueError:
                st.error('解密失败，请检查密码是否正确')

"""
生成密钥并创建一个Fernet实例
"""
def generate_key():
    return Fernet.generate_key()

"""
使用Fernet加密密码
"""
def encrypt_password(password):
    # 生成密钥
    key = generate_key()
    # 创建Fernet实例
    cipher_suite = Fernet(key)
    # 加密密码
    encrypted = cipher_suite.encrypt(password.encode())
    return base64.b64encode(encrypted).decode()

"""
使用Fernet解密密码
"""
def decrypt_password(encrypted_password):
    # 将base64编码的密码解码为字节
    encrypted_password = base64.b64decode(encrypted_password)
    # 生成密钥
    key = generate_key()
    # 创建Fernet实例
    cipher_suite = Fernet(key)
    # 解密密码
    decrypted = cipher_suite.decrypt(encrypted_password)
    return decrypted.decode()

# 运行主函数
if __name__ == '__main__':
    main()