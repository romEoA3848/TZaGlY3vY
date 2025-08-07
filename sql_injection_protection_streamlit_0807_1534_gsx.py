# 代码生成时间: 2025-08-07 15:34:08
import streamlit as st
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# 配置数据库连接
DATABASE_URL = "your_database_url"
engine = create_engine(DATABASE_URL)

# 函数：防止SQL注入的安全查询
def safe_query(sql_query, params):
    try:
        with engine.connect() as connection:
            result = connection.execute(sql_query, params)
            return result.fetchall()
    except SQLAlchemyError as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit界面设置
def main():
    st.title('SQL Injection Protection Demo')
    
    # 允许用户输入查询参数
    user_input = st.text_input('Enter your query parameters (comma-separated)', '')
    if st.button('Execute Query'):
        # 分割用户输入以获取参数列表
        params = [param.strip() for param in user_input.split(',')] if user_input else []
        
        # 构建SQL查询
        sql_query = text("SELECT * FROM users WHERE username = :username AND password = :password")
        
        # 执行安全查询
        result = safe_query(sql_query, params)
        
        # 显示结果
        if result:
            st.write('Query Results:')
            st.write(result)
        else:
            st.write('No results found or an error occurred.')

if __name__ == '__main__':
    main()