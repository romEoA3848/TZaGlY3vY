# 代码生成时间: 2025-10-10 03:49:46
import streamlit as st
from sqlparse import split
from sqlparse.sql import IdentifierList, Identifier
import re

# 函数：提取SQL查询中的表名和字段名
def extract_tables_and_columns(sql_query):
    tables = set()
    columns = set()
    for token in split(sql_query):
        if token.get_type() == 'IDENTIFIER':
            identifier = token.get_real_name()
            tables.add(identifier)
        elif isinstance(token, IdentifierList):
            for identifier in token.get_identifiers():
                columns.add(identifier.get_name())
    return tables, columns

# 函数：分析SQL查询并提出优化建议
def analyze_and_optimize(sql_query):
    try:
        # 提取表名和字段名
        tables, columns = extract_tables_and_columns(sql_query)
        # 提出优化建议
        # 这里只是一个示例，实际优化逻辑会更复杂
        advice = []
        if len(tables) > 1:
            advice.append('Consider using JOINs instead of multiple FROM clauses for better performance.')
        if 'SELECT *' in sql_query:
            advice.append('Avoid using SELECT *; specify only the necessary columns.')
        return advice
    except Exception as e:
        return [f'An error occurred: {str(e)}']

# Streamlit 应用的主体
def main():
    st.title('SQL Query Optimizer')
    
    # 输入框，用户输入SQL查询
    sql_query = st.text_area('Enter your SQL query here:', height=200)
    
    # 按钮，用户点击以分析查询
    if st.button('Analyze Query'):
        # 分析并优化SQL查询
        advice = analyze_and_optimize(sql_query)
        
        # 显示优化建议
        if advice:
            st.subheader('Optimization Advice')
            for item in advice:
                st.write(item)
        else:
            st.write('No optimization advice found.')

if __name__ == '__main__':
    main()