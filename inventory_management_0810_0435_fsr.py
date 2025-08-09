# 代码生成时间: 2025-08-10 04:35:15
import streamlit as st

# 库存管理系统
class InventoryManager:
    def __init__(self):
        """构造函数，初始化库存数据"""
        self.inventory = {}

    def add_item(self, item_name, quantity):
        """添加物品到库存中"""
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def remove_item(self, item_name, quantity):
        """从库存中移除物品"""
        if item_name in self.inventory and self.inventory[item_name] >= quantity:
            self.inventory[item_name] -= quantity
            if self.inventory[item_name] == 0:
                del self.inventory[item_name]
        else:
            raise ValueError("库存不足或物品不存在")

    def get_inventory(self):
        """获取当前库存情况"""
        return self.inventory

# Streamlit界面配置
def main():
    st.title('库存管理系统')

    # 创建库存管理对象
    manager = InventoryManager()

    # 添加物品表单
    with st.form(key='add_item_form'):
        item_name = st.text_input('物品名称', key='add_item_name')
        quantity = st.number_input('数量', value=1, key='add_item_quantity')
        submit_button = st.form_submit_button(label='添加物品')
        if submit_button:
            manager.add_item(item_name, quantity)
            st.success('物品添加成功！')

    # 移除物品表单
    with st.form(key='remove_item_form'):
        item_name = st.text_input('物品名称', key='remove_item_name')
        quantity = st.number_input('数量', value=1, key='remove_item_quantity')
        submit_button = st.form_submit_button(label='移除物品')
        if submit_button:
            try:
                manager.remove_item(item_name, quantity)
                st.success('物品移除成功！')
            except ValueError as e:
                st.error(e)

    # 显示当前库存情况
    st.subheader('当前库存')
    inventory = manager.get_inventory()
    if inventory:
        st.write(inventory)
    else:
        st.write('库存为空。')

if __name__ == '__main__':
    main()