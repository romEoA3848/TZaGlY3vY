# 代码生成时间: 2025-10-01 02:04:28
import streamlit as st
def numerical_integration(f, a, b, n):    """
    Perform numerical integration using the trapezoidal rule.

    Parameters:
    f (callable): Function to integrate.
    a (float): Lower limit of integration.
    b (float): Upper limit of integration.
    n (int): Number of trapezoids to use.

    Returns:
    float: The result of the numerical integration.
    """    h = (b - a) / n    integral = 0.5 * (f(a) + f(b)) * h    for i in range(1, n):        x_i = a + i * h        integral += f(x_i) * h    return integral

# Define the user interface in Streamlit
st.title('Numerical Integration Calculator')
with st.form('integration_form'):    # Input section    function_input = st.text_input('label', 'Enter the function to integrate, e.g., x^2')
    lower_limit = st.slider('Lower limit of integration', min_value=-10.0, max_value=10.0, value=0.0)
    upper_limit = st.slider('Upper limit of integration', min_value=-10.0, max_value=10.0, value=1.0)
    num_trapezoids = st.slider('Number of trapezoids', min_value=10, max_value=1000, value=100)

    # Submit button
    submitted = st.form_submit_button(label='Calculate')

    # Perform the integration if the form is submitted
    if submitted:        try:            # Define the function to integrate based on user input            def integrand(x):                return eval(function_input)

            # Calculate the integral
            result = numerical_integration(integrand, lower_limit, upper_limit, num_trapezoids)

            # Display the result
            st.write(f'The result of the numerical integration is: {result}')        except Exception as e:            # Handle errors, such as non-integer values, invalid function input
            st.error(f'An error occurred: {e}')