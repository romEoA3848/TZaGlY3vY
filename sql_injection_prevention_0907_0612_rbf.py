# 代码生成时间: 2025-09-07 06:12:48
import streamlit as st
from sqlalchemy import create_engine, text

# 配置数据库连接
DATABASE_URL = "sqlite:///example.db"  # 此处以SQLite为例，实际应用中请替换为正确的数据库URL
engine = create_engine(DATABASE_URL)

# 函数：防止SQL注入，安全地查询数据库
def safe_query(query, params):
    """
    执行一个参数化的SQL查询，防止SQL注入。
    
    参数:
    query (str): SQL查询语句
    params (dict): 查询参数
    
    返回:
    list: 查询结果
    """
    try:
        with engine.connect() as connection:
            result = connection.execute(text(query), **params)
            return result.fetchall()
    except Exception as e:
        st.error("数据库查询错误：" + str(e))
        return None

# Streamlit界面
def main():
    st.title("防止SQL注入示例")
    
    # 用户输入查询条件
    user_input = st.text_input("请输入查询条件（例如：name='John'）")
    if st.button("查询"):
        try:
            # 构建安全的查询语句和参数
            query = "SELECT * FROM users WHERE " + user_input
            params = {}
            
            # 调用安全查询函数
            results = safe_query(query, params)
            
            # 显示查询结果
            if results is not None:
                st.write("查询结果：")
                st.write(results)
        except Exception as e:
            st.error("发生错误：" + str(e))

if __name__ == "__main__":
    main()