# 代码生成时间: 2025-08-18 13:46:54
import streamlit as st
from sqlalchemy import create_engine, text

"""
Streamlit application to demonstrate SQL injection protection.
"""

# Define a function to safely query the database to prevent SQL injection.
def safe_query(sql_query, params):
    try:
        # Connect to the database
        engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')
        # Use the engine to execute the query with parameters
        with engine.connect() as conn:
            result = conn.execute(text(sql_query), params)
            return result.fetchall()
    except Exception as e:
        # Handle any errors that occur during database connection or query execution
        st.error(f'An error occurred: {e}')
        return None

# Streamlit interface
def main():
    """
    Main function to create the Streamlit interface.
    """
    st.title('SQL Injection Protection Demo')

    # Input for user to enter a query
    user_query = st.text_input("Enter your SQL query: ", "SELECT * FROM users;")

    # Input for parameters to the query
    params_input = st.text_input('Enter parameters for the query (comma-separated): ', '')

    if st.button('Run Query'):
        # Split the parameters input into a list
        params = params_input.split(',')

        # Execute the query safely to prevent SQL injection
        results = safe_query(user_query, params)

        if results is not None:
            st.write('Query Results:')
            st.write(results)

if __name__ == '__main__':
    main()