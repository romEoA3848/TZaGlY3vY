# 代码生成时间: 2025-09-14 06:04:06
import streamlit as st

"""
Streamlit-based Message Notification System
"""

# Streamlit session state
if 'notification' not in st.session_state:
    st.session_state['notification'] = {"message": "", "error": False}

# Create a sidebar
with st.sidebar:
    st.title('Message Notification System')
    
    # Text input for message
    st.session_state['notification']['message'] = st.text_input('Enter your message:', key='message')
    
    # Submit button
    if st.button('Send Notification'):
        try:
            # Process and display the entered message
            st.session_state['notification']['error'] = False
            st.session_state['notification']['message'] = f'Message Sent: {st.session_state['notification']['message']}'
        except Exception as e:
            # Handle any errors that might occur
            st.session_state['notification']['error'] = True
            st.session_state['notification']['message'] = str(e)

# Display notification message
if st.session_state['notification']['error']:
    st.error(st.session_state['notification']['message'])
else:
    st.success(st.session_state['notification']['message'])