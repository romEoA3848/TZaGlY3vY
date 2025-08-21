# 代码生成时间: 2025-08-21 10:27:27
import streamlit as st
import sqlite3

"""
Streamlit application to demonstrate prevention of SQL injection.
This application provides a simple interface to interact with a SQLite database and
includes parameters to demonstrate how to safely handle user input to prevent SQL injection.
"""

# Function to safely query the database
def safe_query(db_connection, query, parameters):
    """Execute a parameterized SQL query to prevent SQL injection."""
    try:
        cursor = db_connection.cursor()
        cursor.execute(query, parameters)
        result = cursor.fetchall()
        cursor.close()
        return result
    except sqlite3.Error as e:
        st.error(f"An error occurred: {e}")
        return None

# Main function to run the Streamlit application
def main():
    # Set up the Streamlit interface
    st.title("SQL Injection Prevention Demo")

    # Text input for user query
    user_input = st.text_input("Enter your query (e.g., SELECT * FROM users WHERE name = ?)", "SELECT * FROM users WHERE name = ?")
    user_value = st.text_input("Enter the value to search for", "")

    # Check if the user has provided input
    if user_input and user_value:
        try:
            # Establish a connection to the SQLite database
            conn = sqlite3.connect("example.db")
            
            # Execute the safe query function with the user input
            result = safe_query(conn, user_input, (user_value,))
            
            # Display the results
            if result:
                st.write("Query Results:")
                st.write(result)
            else:
                st.write("No results found.")
        except Exception as e:
            st.error(f"An error occurred while connecting to the database: {e}")
        finally:
            # Close the database connection
            conn.close()

# Run the Streamlit application
if __name__ == '__main__':
    main()