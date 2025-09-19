# 代码生成时间: 2025-09-20 03:27:34
import streamlit as st
from hashlib import sha256, sha1, md5

"""哈希值计算工具"""

# 定义支持的哈希算法
HASH_ALGORITHMS = {"SHA-256": sha256, "SHA-1": sha1, "MD5": md5}

def calculate_hash(text, algorithm):
    """计算文本的哈希值"""
    if algorithm not in HASH_ALGORITHMS:
        raise ValueError("Unsupported hash algorithm")
    return HASH_ALGORITHMS[algorithm](text.encode()).hexdigest()

def main():
    """主函数，设置Streamlit界面"""
    st.title("哈希值计算工具")

    # 输入框，用户输入文本
    input_text = st.text_area("请输入文本")
    if input_text:  # 只有当文本框不为空时，才显示哈希算法选择器
        # 选择器，用户选择哈希算法
        hash_algorithm = st.selectbox(
            "选择哈希算法",
            list(HASH_ALGORITHMS.keys())
        )
        # 计算哈希值并显示结果
        try:
            hash_value = calculate_hash(input_text, hash_algorithm)
            st.write("计算结果：", hash_value)
        except ValueError as e:
            st.error(f"错误：{e}")

if __name__ == "__main__":
    main()