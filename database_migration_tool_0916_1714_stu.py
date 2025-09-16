# 代码生成时间: 2025-09-16 17:14:52
import streamlit as st
import shutil
from pathlib import Path
import subprocess
import logging

# 设置日志记录
logging.basicConfig(level=logging.INFO)

# 配置数据库迁移工具页面
def main():
    st.title('Database Migration Tool')
    
    # 让用户输入源数据库和目标数据库的信息
    source_db_path = st.text_input("Enter the source database path: ")
    target_db_path = st.text_input("Enter the target database path: ")
    
    if st.button('Migrate Database'):
        if source_db_path and target_db_path:
            try:
                # 检查路径是否存在
                source_db = Path(source_db_path)
                target_db = Path(target_db_path)
                
                if not source_db.exists():
                    raise FileNotFoundError(f"Source database file '{source_db_path}' not found.")
                
                if not target_db.parent.exists():
                    # 创建目标路径
                    target_db.parent.mkdir(parents=True)
                
                # 迁移数据库文件
                shutil.copy2(source_db, target_db)
                
                # 显示成功消息
                st.success(f'Database successfully migrated from {source_db} to {target_db}')
            except Exception as e:
                # 显示错误消息
                st.error(f'An error occurred: {e}')
        else:
            st.warning("Please provide both source and target database paths.")
    
# 设置Streamlit页面
if __name__ == '__main__':
    st.set_page_config(page_title='Database Migration Tool', page_icon=':DATABASE:', layout='centered')
    main()