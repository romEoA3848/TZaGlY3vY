# 代码生成时间: 2025-09-18 12:56:00
import streamlit as st

# Inventory Management System
# This system allows users to add, update, delete, and view items in stock.

# Initialize the inventory dictionary
inventory = {}

# Function to add an item to the inventory
def add_item(item_name, quantity):
    if item_name in inventory:
        # If the item exists, update the quantity
        inventory[item_name] += quantity
    else:
        # If the item does not exist, add it to the inventory
        inventory[item_name] = quantity
    return True

# Function to update an item quantity in the inventory
def update_item(item_name, quantity):
    if item_name in inventory:
        # If the item exists, update the quantity
        inventory[item_name] = quantity
        return True
    else:
        # If the item does not exist, raise an error
        st.error(f"Item '{item_name}' not found in inventory.")
        return False

# Function to delete an item from the inventory
def delete_item(item_name):
    if item_name in inventory:
        # If the item exists, remove it from the inventory
        del inventory[item_name]
        return True
    else:
        # If the item does not exist, raise an error
        st.error(f"Item '{item_name}' not found in inventory.")
        return False

# Function to display inventory
def display_inventory():
    st.write("Current Inventory:")
    for item_name, quantity in inventory.items():
        st.write(f"{item_name}: {quantity}")

# Streamlit interface
def main():
    st.title('Inventory Management System')

    action = st.selectbox(
        "Choose an action",
        ("Add Item", "Update Item", "Delete Item", "View Inventory")
    )

    if action == "Add Item":
        item_name = st.text_input("Enter item name")
        quantity = st.number_input("Enter quantity", min_value=1, max_value=1000, value=1, step=1)
        if st.button("Add"):
            if add_item(item_name, quantity):
                st.success(f"Item '{item_name}' added successfully.")

    elif action == "Update Item":
        item_name = st.text_input("Enter item name")
        quantity = st.number_input("Enter new quantity", min_value=0, max_value=1000, value=0, step=1)
        if st.button("Update\):
            if update_item(item_name, quantity):
                st.success(f"Item '{item_name}' updated successfully.")

    elif action == "Delete Item":
        item_name = st.text_input("Enter item name")
        if st.button("Delete"):
            if delete_item(item_name):
                st.success(f"Item '{item_name}' deleted successfully.")

    elif action == "View Inventory":
        display_inventory()

if __name__ == '__main__':
    main()