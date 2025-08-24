# 代码生成时间: 2025-08-25 03:05:28
import streamlit as st

"""
This Streamlit application demonstrates various sorting algorithms.

It includes Bubble Sort, Insertion Sort, and Quick Sort.
Users can input a list of numbers and choose which algorithm to apply.
"""

# Define sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

# Streamlit interface
def main():
    st.title('Sorting Algorithm Application')

    # Input for the list of numbers
    input_list = st.text_input('Enter a list of numbers separated by spaces: ', value='5 3 8 4 2 7 1')
    try:
        numbers = list(map(int, input_list.split()))
    except ValueError:
        st.error('Please enter only integers separated by spaces.')
        return

    # Select the sorting algorithm
    algorithm = st.selectbox('Choose a sorting algorithm:', ('Bubble Sort', 'Insertion Sort', 'Quick Sort'))

    # Apply the sorting algorithm
    if algorithm == 'Bubble Sort':
        sorted_numbers = bubble_sort(numbers[:])
    elif algorithm == 'Insertion Sort':
        sorted_numbers = insertion_sort(numbers[:])
    elif algorithm == 'Quick Sort':
        sorted_numbers = quick_sort(numbers[:], 0, len(numbers) - 1)

    # Display the result
    st.write('Sorted list:', sorted_numbers)

if __name__ == '__main__':
    main()