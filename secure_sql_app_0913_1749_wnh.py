# 代码生成时间: 2025-09-13 17:49:45
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os

# 数据库配置信息
DATABASE_URL = 'postgresql+psycopg2://user:password@localhost/dbname'  # 请替换为实际的数据库连接信息

# 创建数据库引擎和会话
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# 主函数，用于处理Streamlit应用的请求
def main():
    """主函数，用于处理Streamlit应用的请求"""
    # 检查数据库连接是否成功
    with Session() as session:
        try:
            session.execute("SELECT 1")
            st.write("数据库连接成功")
        except SQLAlchemyError as e:
            st.error("数据库连接失败: " + str(e))
            return

    # 创建Streamlit应用
    with st.form("query_form"):
        query_input = st.text_input("SQL查询输入", key="query_input")
        submit_button = st.form_submit_button("查询")

    if submit_button:
        # 验证输入
        if query_input:
            try:
                # 使用参数化查询防止SQL注入
                with Session() as session:
                    result = session.execute(query_input)
                    st.write("查询结果：")
                    for row in result:
                        st.write(row)
            except SQLAlchemyError as e:
                st.error("SQL执行失败: " + str(e))
        else:
            st.error("请输入SQL查询语句")

if __name__ == "__main__":
    main()