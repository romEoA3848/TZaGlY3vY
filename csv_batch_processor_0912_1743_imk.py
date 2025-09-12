# 代码生成时间: 2025-09-12 17:43:26
import streamlit as st
import pandas as pd
import os
from typing import List

# 定义CSV批量处理器类
class CSVBatchProcessor:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        self.files = self._list_csv_files()

    def _list_csv_files(self) -> List[str]:
        """遍历指定文件夹，返回所有CSV文件的完整路径列表。"""
        csv_files = []
        for file in os.listdir(self.folder_path):
            if file.endswith('.csv'):
                csv_files.append(os.path.join(self.folder_path, file))
        return csv_files

    def process_files(self) -> List[pd.DataFrame]:
        """处理指定文件夹中的所有CSV文件，并返回包含每个文件数据的DataFrame列表。"""
        results = []
        for file in self.files:
            try:
                df = pd.read_csv(file)
                results.append(df)
            except Exception as e:
                st.error(f'Error processing {file}: {e}')
        return results

# 主函数，用于在Streamlit中运行程序
def main():
    st.title('CSV Batch Processor')

    # 用户输入文件夹路径
    folder_path = st.text_input('Enter the folder path containing CSV files:', '')
    if folder_path:
        # 创建CSV批量处理器实例
        processor = CSVBatchProcessor(folder_path)

        # 显示CSV文件列表
        st.write('CSV Files to Process:')
        for file in processor.files:
            st.write(file)

        # 处理CSV文件
        result_dfs = processor.process_files()

        # 显示结果
        st.write('Processed CSV Data:')
        for i, df in enumerate(result_dfs):
            st.write(f'File {i+1}:')
            st.write(df)

if __name__ == '__main__':
    main()