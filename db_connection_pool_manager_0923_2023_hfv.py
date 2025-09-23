# 代码生成时间: 2025-09-23 20:23:39
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError

# 配置数据库连接信息
DB_URI = '你的数据库URI'

# 创建数据库连接引擎
engine = create_engine(DB_URI)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建连接池
db_session = scoped_session(SessionLocal)

"""
Streamlit应用的主功能
"""
def main():
    st.title('数据库连接池管理')
    
    # 连接数据库
    try:
        with db_session() as session:
            # 执行数据库查询或操作
            # 例如：获取所有用户信息
            users = session.execute("SELECT * FROM users").fetchall()
            st.write(users)
    except SQLAlchemyError as e:
        st.error(f'数据库操作失败: {e}')
    finally:
        db_session.remove()

if __name__ == '__main__':
    main()