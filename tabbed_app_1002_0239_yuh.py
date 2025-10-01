# 代码生成时间: 2025-10-02 02:39:19
import streamlit as st

"""
Streamlit application that creates a tabbed interface with multiple tabs.
Each tab can contain different content and can be expanded to include more complex functionalities.
"""

# Define a function to display the contents of each tab
def show_tab_content(tab_name):
    """
    Function to show content based on the tab selected.
    :param tab_name: The name of the tab to display.
    """
    if tab_name == "Tab 1":
        st.title("Welcome to Tab 1")
        st.write("This is the content of Tab 1.")
    elif tab_name == "Tab 2":
        st.title("Welcome to Tab 2")
        st.write("This is the content of Tab 2.")
    elif tab_name == "Tab 3":
        st.title("Welcome to Tab 3")
        st.write("This is the content of Tab 3.")
    else:
        st.error("Tab not found.")

# Create tabs in the Streamlit application
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

# Display content in each tab based on the selection
with tab1:
    show_tab_content("Tab 1")

with tab2:
    show_tab_content("Tab 2")

with tab3:
    show_tab_content("Tab 3")