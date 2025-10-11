# 代码生成时间: 2025-10-12 02:54:19
import streamlit as st
def drag_and_sort_component(initial_list):
    """
    This function creates a drag and sort component using Streamlit's API.
    It returns the sorted list based on user's drag and drop actions.
    
    Parameters:
    initial_list (list): The initial list of items to be sorted.
    
    Returns:
    list: The sorted list of items.
    """
    try:
        # Use Streamlit's session state to store the list
        if 'sorted_list' not in st.session_state:
            st.session_state['sorted_list'] = initial_list
        
        # Create the drag and drop interface
        sorted_list = st.draggable_component(key="drag_and_sort",
                                             value=st.session_state['sorted_list'],
                                             label="Drag to sort",
                                             data=st.session_state['sorted_list'],
                                             help="Drag and drop items to sort them")
        
        # Update session state with the new sorted list
        st.session_state['sorted_list'] = sorted_list
        
        return sorted_list
    except Exception as e:
        # Handle any exceptions and return the initial list
        st.error(f"An error occurred: {e}")
        return initial_list

# Example usage
if __name__ == '__main__':
    # Define the initial list of items
    initial_items = [1, 2, 3, 4, 5]
    
    # Create a title for the app
    st.title("Drag and Sort Component Example")
    
    # Create a drag and sort component with the initial list
    sorted_items = drag_and_sort_component(initial_items)
    
    # Display the sorted items
    st.write("Sorted Items:")
    st.write(sorted_items)