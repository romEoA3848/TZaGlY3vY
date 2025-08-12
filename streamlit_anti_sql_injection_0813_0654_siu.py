# 代码生成时间: 2025-08-13 06:54:53
import streamlit as st
from sqlite3 import connect, Error

# 函数：防止SQL注入的安全查询
# 参数：sql（查询语句），params（参数字典）
# 返回：查询结果
def safe_query(sql, params):
    try:
        # 连接到SQLite数据库
        conn = connect('example.db')
        cursor = conn.cursor()

        # 使用参数化查询防止SQL注入
        cursor.execute(sql, params)
        result = cursor.fetchall()

        # 关闭游标和连接
        cursor.close()
        conn.close()

        return result
    except Error as e:
        # 错误处理
        print(f"数据库错误：{e}")
        return None

# Streamlit应用
def main():
    st.title('防止SQL注入示例')

    # 用户输入
    user_input = st.text_input("输入查询条件", "")

    # 表单提交按钮
    if st.button('查询'):
        # 定义查询语句和参数字典
        sql = "SELECT * FROM users WHERE username = ?"
        params = {1: user_input}

        # 执行安全查询
        result = safe_query(sql, params)

        # 显示查询结果
        if result:
            st.write(result)
        else:
            st.error("查询失败，请检查输入！")

if __name__ == '__main__':
    main()