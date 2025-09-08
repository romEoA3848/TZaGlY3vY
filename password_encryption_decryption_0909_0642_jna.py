# 代码生成时间: 2025-09-09 06:42:39
import streamlit as st
from cryptography.fernet import Fernet

"""
Password Encryption and Decryption Tool using Streamlit.
This tool allows users to encrypt and decrypt passwords using a symmetric key.

Attributes:
    None

Methods:
    encrypt_password: Encrypts a given password.
    decrypt_password: Decrypts a given cipher text.
"""

# Generate a key for encryption and decryption.
# Typically, this key would be securely stored and not hard-coded in the application.
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_password(password: str) -> str:
    """Encrypts a given password using the Fernet symmetric encryption library.
    
    Args:
        password (str): The password to encrypt.
    
    Returns:
        str: The encrypted password.
    
    Raises:
        TypeError: If the password is not a string.
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string.")
    return cipher_suite.encrypt(password.encode()).decode()


def decrypt_password(encrypted_password: str) -> str:
    """Decrypts a given cipher text using the Fernet symmetric encryption library.
    
    Args:
        encrypted_password (str): The cipher text to decrypt.
    
    Returns:
        str: The decrypted password.
    
    Raises:
        TypeError: If the encrypted password is not a string.
        ValueError: If the encryption key is incorrect or the cipher text is corrupted.
    """
    if not isinstance(encrypted_password, str):
        raise TypeError("Encrypted password must be a string.")
    try:
        return cipher_suite.decrypt(encrypted_password.encode()).decode()
    except Exception as e:
        raise ValueError("Decryption failed: " + str(e))

# Create a Streamlit app to interact with the user.
st.title('Password Encryption and Decryption Tool')

# Text input for the password to be encrypted.
password_input = st.text_input('Enter password to encrypt: ')

# Button to trigger the encryption process.
if st.button('Encrypt Password'):
    """Encrypts the password and displays the result."""
    encrypted_password = encrypt_password(password_input)
    st.success('Encrypted Password: ' + encrypted_password)

# Text input for the encrypted password to be decrypted.
encrypted_input = st.text_input('Enter encrypted password to decrypt: ')

# Button to trigger the decryption process.
if st.button('Decrypt Password'):
    """Decrypts the password and displays the result."""
    try:
        decrypted_password = decrypt_password(encrypted_input)
        st.success('Decrypted Password: ' + decrypted_password)
    except ValueError as ve:
        st.error('Error: ' + str(ve))
