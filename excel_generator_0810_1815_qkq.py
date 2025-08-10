# 代码生成时间: 2025-08-10 18:15:04
import streamlit as st
import pandas as pd
from openpyxl import Workbook
# TODO: 优化性能
from openpyxl.utils.exceptions import InvalidFileException
from openpyxl import load_workbook
import os

# 函数：生成Excel表格
def generate_excel(data, filename='Generated_Excel.xlsx', sheet_name='Sheet1'):
    wb = Workbook()
    ws = wb.active
    ws.title = sheet_name
    
    for i, row in enumerate(data):
        ws.append(row)
    
    try:
# NOTE: 重要实现细节
        wb.save(filename=filename)
        return f'Excel file {filename} generated successfully.'
    except InvalidFileException as e:
        return f'Error occurred while generating Excel file: {e}'

# Streamlit页面配置
def excel_app():
    st.title('Excel表格自动生成器')
    st.write('欢迎使用Excel表格自动生成器，请输入数据并生成Excel文件。')
    
    # 数据输入区域
# 优化算法效率
    data_input = st.text_area('请输入表格数据（列与列之间用逗号分隔，行之间用换行符分隔）:', height=200)
# 增强安全性
    
    # 判断是否有数据输入
    if data_input:
        try:
# 改进用户体验
            # 将输入的字符串转换为DataFrame
            data = [row.split(',') for row in data_input.strip().split('
')]
            df = pd.DataFrame(data)
            
            # 检查是否有空列
# FIXME: 处理边界情况
            if df.isnull().values.any():
                st.warning('数据中存在空值，请检查并补全数据后再进行生成。')
            else:
                # 生成Excel文件
                result_message = generate_excel(data)
                st.success(result_message)
        except ValueError as e:
            st.error(f'数据格式有误：{e}')
    else:
        st.warning('请输入数据以生成Excel表格。')
        
# 运行Streamlit应用
if __name__ == '__main__':
    excel_app()
# NOTE: 重要实现细节