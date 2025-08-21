# 代码生成时间: 2025-08-21 15:19:59
import streamlit as st
import sqlite3
from sqlite3 import Error
import os

"""
Database Migration Tool using Streamlit

This tool allows users to perform database migrations using a simple GUI.
It creates a migration script and applies it to the database.
"""

# Constants
DATABASE_NAME = "example.db"
MIGRATION_SCRIPT_TEMPLATE = """
-- Migration Script Template
BEGIN TRANSACTION;

-- Your migration SQL commands here
-- For example:
-- CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT NOT NULL);

COMMIT;
"""

# Function to create connection to SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        st.error(f"Error connecting to database: {e}")
    return conn

# Function to execute SQL migration script
def execute_migration_script(conn, script):
    try:
        cursor = conn.cursor()
        cursor.executescript(script)
        conn.commit()
        st.success("Migration successful.")
    except Error as e:
        st.error(f"Error executing migration script: {e}")

# Streamlit App
def main():
    st.title("Database Migration Tool")

    # User inputs
    db_path = st.text_input("Database File Path", value=DATABASE_NAME)
    migration_script = st.text_area("Migration Script", value=MIGRATION_SCRIPT_TEMPLATE, height=300)

    # Check if database file exists
    if not os.path.isfile(db_path):
        st.error("Database file does not exist.")
        return

    # Connect to the database
    conn = create_connection(db_path)
    if conn is not None:
        # Execute the migration script
        with conn:
            execute_migration_script(conn, migration_script)

if __name__ == '__main__':
    main()