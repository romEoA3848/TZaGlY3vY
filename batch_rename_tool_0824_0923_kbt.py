# 代码生成时间: 2025-08-24 09:23:45
import streamlit as st
def rename_file(old_name, new_name):
    """Rename a single file."""
    try:
        import os
        os.rename(old_name, new_name)
        return True
    except OSError as e:
        st.error(f"Error renaming file {old_name} to {new_name}: {e}")
        return False

def rename_files(directory, pattern, replacement):
    """Batch rename files in a directory based on a pattern and replacement."""
# 优化算法效率
    import os
# NOTE: 重要实现细节
    import re
    for filename in os.listdir(directory):
        if re.search(pattern, filename):
            old_name = os.path.join(directory, filename)
            new_name = re.sub(pattern, replacement, filename)
            new_name = os.path.join(directory, new_name)
            if rename_file(old_name, new_name):
                st.success(f"Renamed {old_name} to {new_name}")

st.title('Batch File Renamer')

# Directory selection
# 增强安全性
directory = st.text_input('Enter the directory path:', '/path/to/directory')
if st.button('Browse'):
    directory = st.file_uploader('Upload a directory', type='directory')

# Check if directory is valid
if directory and os.path.isdir(directory):
# 优化算法效率
    # Input pattern and replacement
    pattern = st.text_input('Enter the pattern for renaming:', '.*.txt')
    replacement = st.text_input('Enter the replacement string:', '_new.txt')
    
    # Rename files button
    if st.button('Rename Files'):
        rename_files(directory, pattern, replacement)
else:
# 改进用户体验
    st.error('Invalid directory path. Please enter a valid path.')