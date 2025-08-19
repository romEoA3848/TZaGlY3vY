# 代码生成时间: 2025-08-19 19:02:50
import streamlit as st
from streamlit.components.v1 import html

"""
用户权限管理系统
使用STREAMLIT框架实现一个简单的用户权限管理系统界面
"""

# 定义用户权限数据结构
class PermissionManagement:
    def __init__(self):
        self.user_permissions = {}

    def add_user(self, username):
        """添加用户"""
        if username in self.user_permissions:
            st.error(f"Error: 用户 {username} 已存在！")
        else:
            self.user_permissions[username] = set()
            st.success(f"用户 {username} 添加成功！")

    def remove_user(self, username):
        """删除用户"""
        if username not in self.user_permissions:
            st.error(f"Error: 用户 {username} 不存在！")
        else:
            del self.user_permissions[username]
            st.success(f"用户 {username} 删除成功！")

    def add_permission(self, username, permission):
        """为用户添加权限"""
        if username not in self.user_permissions:
            st.error(f"Error: 用户 {username} 不存在！")
        else:
            self.user_permissions[username].add(permission)
            st.success(f"为用户 {username} 添加权限 {permission} 成功！")

    def remove_permission(self, username, permission):
        """为用户删除权限"""
        if username not in self.user_permissions:
            st.error(f"Error: 用户 {username} 不存在！")
        else:
            self.user_permissions[username].discard(permission)
            st.success(f"为用户 {username} 删除权限 {permission} 成功！")

    def display_permissions(self):
        """显示所有用户的权限"""
        st.write("用户权限列表：")
        for username, permissions in self.user_permissions.items():
            st.write(f"用户 {username} 的权限：{permissions}")

# 初始化用户权限管理系统
permission_mgmt = PermissionManagement()

# 用户界面
st.title('用户权限管理系统')

with st.form(key='permission_form'):
    username = st.text_input('用户名')
    permission = st.text_input('权限', key='permission_input')
    action = st.selectbox('操作', ['添加用户', '删除用户', '添加权限', '删除权限'])
    submit_button = st.form_submit_button(label='提交')

if submit_button:
    if action == '添加用户':
        permission_mgmt.add_user(username)
    elif action == '删除用户':
        permission_mgmt.remove_user(username)
    elif action == '添加权限':
        permission_mgmt.add_permission(username, permission)
    elif action == '删除权限':
        permission_mgmt.remove_permission(username, permission)

# 显示所有用户的权限
permission_mgmt.display_permissions()
