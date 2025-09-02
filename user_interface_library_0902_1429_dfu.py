# 代码生成时间: 2025-09-02 14:29:20
import streamlit as st
def main():
    """Main function to create the user interface library."""
    # Add a header to the application
    st.title('User Interface Component Library')

    # Text Input
    text_input = st.text_input("This is a text input box", key='text_input')
    st.write("Text Input Value: ", text_input)  # Display the input value

    # Number Input
    number_input = st.number_input("This is a number input box", min_value=0, max_value=100, key='number_input')
    st.write("Number Input Value: ", number_input)  # Display the input value

    # Slider
    slider_value = st.slider("This is a slider input", min_value=0, max_value=100, key='slider')
    st.write("Slider Value: ", slider_value)  # Display the slider value

    # Checkbox
    checkbox_value = st.checkbox("This is a checkbox", key='checkbox')
    st.write("Checkbox Value: ", checkbox_value)  # Display the checkbox value

    # Selectbox
    selectbox_value = st.selectbox("This is a selectbox", options=['Option 1', 'Option 2', 'Option 3'], key='selectbox')
    st.write("Selectbox Value: ", selectbox_value)  # Display the selectbox value

    # Multiselect
    multiselect_values = st.multiselect("This is a multiselect", options=['Option 1', 'Option 2', 'Option 3'], key='multiselect')
    st.write("Multiselect Values: ", multiselect_values)  # Display the multiselect values

    # Radio Buttons
    radio_button_value = st.radio('This is a radio button', options=['Option 1', 'Option 2', 'Option 3'], key='radio_button')
    st.write("Radio Button Value: ", radio_button_value)  # Display the radio button value

    # Button
    if st.button('Click Me!', key='button'):
        st.write("You pressed the button!")  # Display a message when the button is pressed

if __name__ == '__main__':
    main()