# 代码生成时间: 2025-08-08 12:55:35
import streamlit as st

"""
Math Calculator App
====================

This Streamlit application provides a simple math calculator with basic operations.
"""

# Define a function to perform addition

def add(x, y):
    try:
        return x + y
    except TypeError:
        return "Error: Invalid input. Please enter numbers."

# Define a function to perform subtraction

def subtract(x, y):
    try:
        return x - y
    except TypeError:
        return "Error: Invalid input. Please enter numbers."

# Define a function to perform multiplication

def multiply(x, y):
    try:
        return x * y
    except TypeError:
        return "Error: Invalid input. Please enter numbers."

# Define a function to perform division

def divide(x, y):
    try:
        if y == 0:
            return "Error: Division by zero is not allowed."
        return x / y
    except TypeError:
        return "Error: Invalid input. Please enter numbers."

# Streamlit interface
def main():
    st.title('Math Calculator App')
    
    # Create a sidebar for input controls
    with st.sidebar:
        st.header('Controls')

    # Input for the first number
    num1 = st.number_input('Enter first number', min_value=-1000.0, max_value=1000.0, value=0.0, step=0.1)
    
    # Input for the second number
    num2 = st.number_input('Enter second number', min_value=-1000.0, max_value=1000.0, value=0.0, step=0.1)
    
    # Dropdown for selecting operation
    operation = st.selectbox('Choose an operation', ('Add', 'Subtract', 'Multiply', 'Divide'))
    
    # Calculate and display the result
    result = None
    if st.button('Calculate'):
        if operation == 'Add':
            result = add(num1, num2)
        elif operation == 'Subtract':
            result = subtract(num1, num2)
        elif operation == 'Multiply':
            result = multiply(num1, num2)
        elif operation == 'Divide':
            result = divide(num1, num2)
    
    # Display the result
    if result is not None:
        st.write(f'The result is: {result}')

if __name__ == '__main__':
    main()