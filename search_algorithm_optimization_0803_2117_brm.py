# 代码生成时间: 2025-08-03 21:17:17
import streamlit as st
from typing import List, Tuple

"""
A Streamlit app for demonstrating search algorithm optimization.
"""
# 添加错误处理

# Define a function to perform linear search on a list of items.
# This function returns the index of the item if found, otherwise -1.
def linear_search(items: List[int], target: int) -> int:
    """
    Perform a linear search on a list of items.

    Args:
    items (List[int]): A list of integers.
    target (int): The target number to search for.

    Returns:
# 优化算法效率
    int: The index of the target item if found, otherwise -1.
# 扩展功能模块
    """
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1
# 改进用户体验

# Define a function to perform binary search on a sorted list of items.
# This function returns the index of the item if found, otherwise -1.
def binary_search(items: List[int], target: int) -> int:
    """
    Perform a binary search on a sorted list of items.

    Args:
# NOTE: 重要实现细节
    items (List[int]): A sorted list of integers.
    target (int): The target number to search for.

    Returns:
    int: The index of the target item if found, otherwise -1.
    """
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
# NOTE: 重要实现细节
            low = mid + 1
        else:
            high = mid - 1
    return -1
# NOTE: 重要实现细节

# Streamlit app startup message.
st.title('Search Algorithm Optimization')

# Create a side bar for input parameters.
with st.sidebar:
    # User input for the list of numbers.
    st.subheader('Input Parameters')
    numbers = st.text_input('Enter a list of numbers (comma-separated)', '1, 2, 3, 4, 5')
    target_number = st.number_input('Enter the target number', min_value=0, max_value=100, value=50)
# NOTE: 重要实现细节
    search_type = st.radio('Choose a search type', ('Linear Search', 'Binary Search'))

    # Convert user input to a list of integers.
    try:
        numbers_list = [int(num) for num in numbers.split(',')]
    except ValueError:
        st.error('Please enter a valid list of numbers.')
        numbers_list = []

    # Perform the search based on the user's choice.
    if st.button('Search'):
        if search_type == 'Linear Search':
            index = linear_search(numbers_list, target_number)
            if index != -1:
# NOTE: 重要实现细节
                st.success(f'Found target number at index {index}')
            else:
                st.error('Target number not found.')
        elif search_type == 'Binary Search':
            if sorted(numbers_list) == numbers_list:  # Check if the list is sorted.
                index = binary_search(numbers_list, target_number)
# 添加错误处理
                if index != -1:
# 优化算法效率
                    st.success(f'Found target number at index {index}')
                else:
                    st.error('Target number not found.')
            else:
                st.error('Binary search requires a sorted list. Please sort the list first.')
