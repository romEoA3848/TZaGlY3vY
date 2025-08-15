# 代码生成时间: 2025-08-15 11:39:37
import streamlit as st
import json
from typing import Any

"""
JSON数据格式转换器应用
"""

# 初始化Streamlit应用
def main():
    st.title('JSON数据格式转换器')

    # 获取用户输入的JSON字符串
    json_str = st.text_area('请输入JSON字符串', height=200)

    # 提示用户输入
    if json_str:
        try:
            # 尝试解析JSON字符串
            data = json.loads(json_str)
            st.write('解析后的JSON对象：')
            st.json(data)
        except json.JSONDecodeError as e:
            # 错误处理：JSON格式错误
            st.error(f'JSON格式错误：{e}')
    else:
        st.info('请输入JSON字符串进行转换。')

# 运行Streamlit应用
if __name__ == '__main__':
    main()