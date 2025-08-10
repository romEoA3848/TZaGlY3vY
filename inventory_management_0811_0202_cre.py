# 代码生成时间: 2025-08-11 02:02:34
import streamlit as st
from dataclasses import dataclass
from typing import Dict, List

"""
Inventory Management System using Streamlit framework.
This application allows users to manage inventory items.
"""


# Define the structure of an inventory item
@dataclass
class Item:
    id: int
    name: str
    quantity: int

    @classmethod
    def from_dict(cls, data: Dict):
        """Class method to create an instance from a dictionary."""
        return cls(**data)


# Define the inventory system
class InventorySystem:
    def __init__(self):
        """Initialize the inventory system with an empty list of items."""
        self.items: List[Item] = []

    def add_item(self, item: Item):
        """Add a new item to the inventory."""
        self.items.append(item)

    def remove_item(self, item_id: int):
        """Remove an item from the inventory by its ID."""
        self.items = [item for item in self.items if item.id != item_id]

    def update_item_quantity(self, item_id: int, quantity: int):
        """Update the quantity of an item in the inventory."""
        for item in self.items:
            if item.id == item_id:
                item.quantity = quantity
                break

    def get_item(self, item_id: int):
        """Get an item from the inventory by its ID."""
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def display_items(self):
        """Display all items in the inventory."""
        for item in self.items:
            st.write(f"ID: {item.id}, Name: {item.name}, Quantity: {item.quantity}")

def main():
    """Main function to run the Streamlit application."""
    st.title('Inventory Management System')

    inventory = InventorySystem()
    
    # Load initial inventory data (for demonstration purposes)
    inventory.add_item(Item.from_dict({'id': 1, 'name': 'Apple', 'quantity': 10}))
    inventory.add_item(Item.from_dict({'id': 2, 'name': 'Banana', 'quantity': 20}))

    with st.form(key='inventory_form'):
        item_id = st.number_input('Item ID', min_value=1)
        item_name = st.text_input('Item Name')
        item_quantity = st.number_input('Item Quantity', min_value=0)
        
        submit_button = st.form_submit_button(label='Add Item')
        
        if submit_button:
            try:
                new_item = Item(item_id, item_name, item_quantity)
                inventory.add_item(new_item)
                st.success(f'Added item: {new_item.name}')
            except ValueError as e:
                st.error(f'Error adding item: {str(e)}')
    
    action = st.selectbox('Choose an action', options=['Delete Item', 'Update Item Quantity'])
    if action == 'Delete Item':
        item_id = st.number_input('Enter item ID to delete', min_value=1)
        if st.button('Delete Item'):
            inventory.remove_item(item_id)
            st.success(f'Item with ID {item_id} has been removed')
    elif action == 'Update Item Quantity':
        item_id = st.number_input('Enter item ID to update', min_value=1)
        new_quantity = st.number_input('Enter new quantity', min_value=0)
        if st.button('Update Item Quantity'):
            inventory.update_item_quantity(item_id, new_quantity)
            st.success(f'Item with ID {item_id} quantity updated to {new_quantity}')
    
    inventory.display_items()

if __name__ == '__main__':
    main()