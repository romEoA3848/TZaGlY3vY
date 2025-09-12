# 代码生成时间: 2025-09-13 04:39:55
import streamlit as st
import yaml
import json
import os
from typing import Any, Dict

"""
配置文件管理器
"""

# 定义配置文件路径
CONFIG_FILE_PATH = 'config.yaml'

class ConfigManager:
    """
    配置文件管理器类
    """
    def __init__(self, config_file: str = CONFIG_FILE_PATH):
        """
        初始化配置文件管理器
        :param config_file: 配置文件路径
        """
        self.config_file = config_file
        self.config_data: Dict[str, Any] = {}
        self.load_config()

    def load_config(self) -> None:
        """
        加载配置文件
        """
        try:
            with open(self.config_file, 'r', encoding='utf-8') as file:
                self.config_data = yaml.safe_load(file) or {}
        except FileNotFoundError:
            st.error(f'配置文件 {self.config_file} 不存在')
        except yaml.YAMLError as e:
            st.error(f'解析配置文件出错：{e}')

    def save_config(self) -> None:
        """
        保存配置文件
        """
        try:
            with open(self.config_file, 'w', encoding='utf-8') as file:
                yaml.safe_dump(self.config_data, file)
        except Exception as e:
            st.error(f'保存配置文件出错：{e}')

    def get_config(self, key: str) -> Any:
        """
        获取配置项值
        :param key: 配置项键
        :return: 配置项值
        """
        return self.config_data.get(key)

    def set_config(self, key: str, value: Any) -> None:
        """
        设置配置项值
        :param key: 配置项键
        :param value: 配置项值
        """
        self.config_data[key] = value
        self.save_config()

    def delete_config(self, key: str) -> None:
        """
        删除配置项
        :param key: 配置项键
        """
        if key in self.config_data:
            del self.config_data[key]
            self.save_config()

# 创建配置文件管理器实例
config_manager = ConfigManager()

# Streamlit界面
st.title('配置文件管理器')

# 加载按钮
if st.button('加载配置文件'):
    config_manager.load_config()

# 保存按钮
if st.button('保存配置文件'):
    config_manager.save_config()

# 获取配置项
key = st.text_input('请输入配置项键', key='key')
if st.button('获取配置项值'):
    value = config_manager.get_config(key)
    st.write(f'配置项值：{value}')

# 设置配置项
new_key = st.text_input('请输入新的配置项键', key='new_key')
new_value = st.text_input('请输入新的配置项值', key='new_value')
if st.button('设置配置项'):
    config_manager.set_config(new_key, new_value)

# 删除配置项
delete_key = st.text_input('请输入要删除的配置项键', key='delete_key')
if st.button('删除配置项'):
    config_manager.delete_config(delete_key)
