# 代码生成时间: 2025-08-15 16:14:02
import streamlit as st
import json
import os
from pathlib import Path
from typing import Dict


class ConfigManager:
    """A class to manage configuration files."""
    def __init__(self, config_path: str):  # 初始化配置文件路径
        self.config_path = Path(config_path)
        self.config_data: Dict = {}
        self.load_config()

    def load_config(self):  # 加载配置文件
        """Load the configuration file or initialize an empty config if it doesn't exist."""
        if self.config_path.exists():
            with open(self.config_path, 'r') as file:
                self.config_data = json.load(file)
        else:
            self.config_data = {}

    def save_config(self):  # 保存配置文件
        """Save the current configuration data to the file."""
        with open(self.config_path, 'w') as file:
            json.dump(self.config_data, file, indent=4)

    def get_config(self, key: str):  # 获取配置项
        """Get a configuration value by key."""
        return self.config_data.get(key)

    def set_config(self, key: str, value):  # 设置配置项
        """Set a configuration value by key."""
        self.config_data[key] = value

    def delete_config(self, key: str):  # 删除配置项
        """Delete a configuration value by key."""
        if key in self.config_data:
            del self.config_data[key]


# Streamlit UI for ConfigManager
def main():
    CONFIG_PATH = 'config.json'  # 配置文件路径

    st.title('Config Manager')

    manager = ConfigManager(CONFIG_PATH)  # 实例化配置管理器

    # 用户界面输入与操作
    with st.form(key='config_form'):
        config_key = st.text_input('Enter config key')
        config_value = st.text_input('Enter config value')
        if st.form_submit_button('Submit'):
            if config_key:
                if config_value:
                    manager.set_config(config_key, config_value)
                    st.success(f'Config {config_key} set to {config_value}')
                else:
                    if manager.get_config(config_key):
                        manager.delete_config(config_key)
                        st.success(f'Config {config_key} deleted')
                    else:
                        st.error(f'Config {config_key} not found')
            else:
                st.error('Please enter a key')

        manager.save_config()  # 保存配置

    # 显示当前配置
    st.header('Current Configuration')
    for key, value in manager.get_config().items():
        st.write(f'{key}: {value}')


if __name__ == '__main__':
    main()