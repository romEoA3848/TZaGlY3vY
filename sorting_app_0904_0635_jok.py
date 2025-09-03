# 代码生成时间: 2025-09-04 06:35:18
import streamlit as st

def bubble_sort(arr):
    """
    Bubble Sort Algorithm implementation.
    This function sorts an array in ascending order.
    :param arr: List of numbers to be sorted.
    :return: Sorted list.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    """
    Selection Sort Algorithm implementation.
    This function sorts an array in ascending order.
    :param arr: List of numbers to be sorted.
    :return: Sorted list.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    """
    Insertion Sort Algorithm implementation.
    This function sorts an array in ascending order.
    :param arr: List of numbers to be sorted.
    :return: Sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def main():
    st.title('Sorting Algorithms Visualization')
    
    # Generate a random list of numbers
    numbers = st.slider('Number of elements', min_value=1, max_value=100, value=10)
    random_list = [st.number_input(f'Element {i+1}', min_value=-100, max_value=100, value=0, step=1) for i in range(numbers)]
    
    # Select the sorting algorithm
    algorithm = st.selectbox(
        'Select a sorting algorithm:',
        ['Bubble Sort', 'Selection Sort', 'Insertion Sort']
    )
    
    # Sort the list using the selected algorithm
    if algorithm == 'Bubble Sort':
        sorted_list = bubble_sort(random_list)
    elif algorithm == 'Selection Sort':
        sorted_list = selection_sort(random_list)
    else:  # Insertion Sort
        sorted_list = insertion_sort(random_list)
    
    # Display the sorted list
    st.write('Sorted List:', sorted_list)

if __name__ == '__main__':
    main()