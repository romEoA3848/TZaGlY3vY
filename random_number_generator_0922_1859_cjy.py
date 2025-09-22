# 代码生成时间: 2025-09-22 18:59:04
import streamlit as st
import random
from typing import Tuple

"""
Streamlit application for generating random numbers.
This application allows users to specify the range of the random number
and the number of random numbers to generate.
"""

# Function to generate a single random number within a given range
def generate_random_number(min_val: int, max_val: int) -> int:
    """Generate a random number between min_val and max_val.

    Args:
    min_val (int): The minimum value of the range
    max_val (int): The maximum value of the range

    Returns:
    int: A random number within the specified range
    """
    return random.randint(min_val, max_val)

# Function to generate a list of random numbers within a given range
def generate_random_numbers(min_val: int, max_val: int, num: int) -> Tuple[int, ...]:
    """Generate a list of random numbers between min_val and max_val.

    Args:
    min_val (int): The minimum value of the range
    max_val (int): The maximum value of the range
    num (int): The number of random numbers to generate

    Returns:
    Tuple[int, ...]: A tuple containing the random numbers
    """
    return tuple(generate_random_number(min_val, max_val) for _ in range(num))

# Streamlit application
def main():
    """Main function to run the Streamlit application."""
    st.title('Random Number Generator')

    # Input fields for minimum and maximum values
    min_val = st.number_input('Minimum value', min_value=0, max_value=100, value=0, step=1)
    max_val = st.number_input('Maximum value', min_value=1, max_value=100, value=100, step=1)

    # Check if maximum value is greater than minimum value
    if max_val < min_val:
        st.error('Maximum value must be greater than minimum value')
        return

    # Input field for the number of random numbers to generate
    num = st.number_input('Number of random numbers', min_value=1, max_value=100, value=1, step=1)

    # Generate and display random numbers
    random_numbers = generate_random_numbers(min_val, max_val, num)
    st.write('Generated random numbers:', random_numbers)

if __name__ == '__main__':
    main()