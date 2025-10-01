# 代码生成时间: 2025-10-01 16:54:49
import streamlit as st
import hashlib
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature

"""
数字签名工具，使用STREAMLIT框架创建的Web应用
"""

# 定义主函数
def main():
    """
    主函数，运行STREAMLIT应用
    """
    st.title('数字签名工具')

    # 获取用户输入的数据
    data = st.text_area('请输入数据')
    signature = st.text_area('请输入签名')
    private_key = st.text_area('请输入私钥', type='password')
    
    # 创建按钮，用于验证签名
    if st.button('验证签名'):
        try:
            # 加载私钥
            private_key_obj = serialization.load_pem_private_key(
                private_key.encode(),
                password=None,
                backend=default_backend()
            )
            # 验证签名
            if verify_signature(data, signature, private_key_obj):
                st.success('签名验证成功！')
            else:
                st.error('签名验证失败！')
        except (ValueError, InvalidSignature) as e:
            st.error(f'验证过程中出现错误：{e}')

# 定义验证签名的函数
def verify_signature(data, signature, private_key_obj):
    """
    验证签名
    :param data: 需要验证的数据
    :param signature: 签名
    :param private_key_obj: 私钥对象
    :return: 验证结果
    """
    # 将签名解码
    signature_bytes = signature.encode()
    
    # 验证签名
    try:
        private_key_obj.public_key().verify(
            signature_bytes,
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False

# 运行主函数
if __name__ == '__main__':
    main()