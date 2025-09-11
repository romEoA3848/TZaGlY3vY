# 代码生成时间: 2025-09-12 01:26:17
import streamlit as st

# 定义用户权限数据结构
permission_data = {
    'users': {
        'admin': {'password': 'admin123', 'permissions': ['read', 'write', 'delete']},
        'editor': {'password': 'editor123', 'permissions': ['read', 'write']},
        'viewer': {'password': 'viewer123', 'permissions': ['read']},
    }
}

# 登录函数
def login(username, password):
    """
    用户登录函数，验证用户名和密码

    :param username: 用户名
    :param password: 密码
    :return: 用户权限列表
    """
    user_info = permission_data.get('users', {}).get(username)
    if user_info and user_info['password'] == password:
        return user_info['permissions']
    else:
        raise ValueError('Invalid username or password')

# 主页面
def main_page():
    """
    用户权限管理主页面
    """
    st.title('User Permission Management System')

    # 用户名和密码输入框
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    # 登录按钮
    login_button = st.button('Login')

    # 错误消息
    error_message = ''

    # 处理登录逻辑
    if login_button:
        try:
            permissions = login(username, password)
            st.write(f'Welcome {username}! You have the following permissions: {permissions}')
        except ValueError as e:
            error_message = str(e)
            st.error(error_message)

    return

# 运行主页面
if __name__ == '__main__':
    main_page()