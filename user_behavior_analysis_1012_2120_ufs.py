# 代码生成时间: 2025-10-12 21:20:48
import streamlit as st
import pandas as pd
import numpy as np

# Streamlit页面配置
st.set_page_config(page_title='User Behavior Analysis', page_icon=':smiley:', layout='wide')

# 主函数，用于分析用户行为
def main():
    # 显示欢迎信息
    st.title('User Behavior Analysis Dashboard')

    # 允许用户上传数据文件
    st.subheader('Upload User Data')
    uploaded_file = st.file_uploader('Choose a file', type=['csv', 'xlsx', 'txt'])

    if uploaded_file is not None:
        # 读取文件内容
        try:
            if uploaded_file.type == 'text/csv':
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.type in ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.ms-excel']:
                df = pd.read_excel(uploaded_file)
            else:
                df = pd.read_table(uploaded_file)

            # 显示数据预览
            st.subheader('Data Preview')
            st.write(df.head())

            # 分析用户行为
            st.subheader('User Behavior Analysis')
            if 'user_id' in df.columns and 'action_type' in df.columns:
                user_actions = df.groupby('user_id')['action_type'].value_counts().unstack().fillna(0)
                st.write('User Actions Heatmap')
                st.write(user_actions.heatmap())
            else:
                st.error('Required columns are missing: user_id and/or action_type')

        except Exception as e:
            st.error(f'Failed to read the file: {str(e)}')

# 运行主函数
if __name__ == '__main__':
    main()