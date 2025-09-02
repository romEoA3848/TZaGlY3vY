# 代码生成时间: 2025-09-02 09:26:12
import streamlit as st
import hashlib
from typing import Dict

"""
Hash Calculator App using Streamlit

This application allows users to calculate hash values for input strings.
It supports SHA-1, SHA-256, and MD5 hash functions.
"""

# Define the supported hash functions
SUPPORTED_HASH_FUNCTIONS: Dict[str, str] = {
    "SHA-1": hashlib.sha1,
    "SHA-256": hashlib.sha256,
    "MD5": hashlib.md5
}

def calculate_hash(input_string: str, hash_function: str) -> str:
    """
    Calculate the hash of the input string using the specified hash function.

    Args:
    input_string (str): The string to be hashed.
    hash_function (str): The hash function to use (e.g., 'SHA-1', 'SHA-256', 'MD5').

    Returns:
    str: The hash value of the input string.
    """
    try:
        # Get the hash function object from the dictionary
        hash_func = SUPPORTED_HASH_FUNCTIONS[hash_function]
        # Update the hash object with the bytes of the input string
        hash_obj = hash_func()
        hash_obj.update(input_string.encode())
        # Return the hex digest of the hash
        return hash_obj.hexdigest()
    except KeyError:
        # Handle the case where the hash function is not supported
        raise ValueError(f"Unsupported hash function: {hash_function}")

def main():
    """
    Main function to run the Streamlit app.
    """
    # Create a title for the app
    st.title('Hash Calculator App')

    # Create a text input field for the user to enter the string
    input_string = st.text_input('Enter a string to hash:', '')

    if input_string:
        # Create a select box for the user to choose the hash function
        hash_function = st.selectbox('Choose a hash function:', list(SUPPORTED_HASH_FUNCTIONS.keys()))

        # Calculate the hash value
        hash_value = calculate_hash(input_string, hash_function)

        # Display the hash value in the app
        st.write(f'The {hash_function} hash of the input string is: {hash_value}')

if __name__ == '__main__':
    main()