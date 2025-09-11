# 代码生成时间: 2025-09-11 13:49:48
import streamlit as st

"""
Streamlit application to validate form data
"""

# Define a custom validator function for email
def validate_email(email):
    """Validate the provided email address."""
    if "@" not in email or "." not in email.split("@")[1]:
        return False, "Invalid email format."
    return True, ""

# Define a custom validator function for age
def validate_age(age):
    """Validate the provided age."""
    try:
        age = int(age)
        if age < 0:
            return False, "Age cannot be negative."
    except ValueError:
        return False, "Age must be an integer."
    return True, ""

# Streamlit interface
def main():
    st.title("Form Data Validator")

    # Get data from user
    email = st.text_input("Enter your email")
    age = st.number_input("Enter your age", min_value=0)

    # Validate email
    is_valid_email, email_error = validate_email(email)
    if not is_valid_email:
        st.error(f"Email validation error: {email_error}")

    # Validate age
    is_valid_age, age_error = validate_age(str(age))
    if not is_valid_age:
        st.error(f"Age validation error: {age_error}")

    # Show success message if both are valid
    if is_valid_email and is_valid_age:
        st.success("Both email and age are valid.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()