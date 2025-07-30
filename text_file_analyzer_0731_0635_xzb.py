# 代码生成时间: 2025-07-31 06:35:41
import streamlit as st
import pandas as pd
from typing import List

"""
Text File Analyzer using Streamlit.
This program allows users to upload a text file and analyze its content.
"""

# Function to read and return the content of a text file
def read_text_file(file_path: str) -> List[str]:
    """
    Reads text file and returns content as a list of lines.
    :param file_path: Path to the text file.
    :return: List of lines in the file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()
    except Exception as e:
        raise FileNotFoundError(f"Unable to read file: {e}")

# Function to analyze text file content
def analyze_text_content(lines: List[str]) -> pd.DataFrame:
    """
    Analyzes text file content and returns a DataFrame with word frequencies.
    :param lines: List of lines in the text file.
    :return: DataFrame containing word frequencies.
    """
    word_list = []
    for line in lines:
        words = line.split()
        word_list.extend(words)
    
    # Remove empty strings and convert to lower case for consistency
    word_list = [word.strip(".,/#!$%^&*;:{}=-_`~()").lower() for word in word_list if word.strip(".,/#!$%^&*;:{}=-_`~()")]
    
    # Count word frequencies
    word_freq = pd.Series(word_list).value_counts().reset_index()
    word_freq.columns = ["Word", "Frequency"]
    return word_freq

# Streamlit interface
def main():
    st.title("Text File Content Analyzer")
    st.write("Upload a text file to analyze its content.")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a text file", type=['txt'])
    
    if uploaded_file is not None:
        # Read file
        file_path = "temp.txt"
        with open(file_path, "wb") as file:
            file.write(uploaded_file.getvalue())
        
        try:
            lines = read_text_file(file_path)
            # Analyze content
            analysis_df = analyze_text_content(lines)
            
            # Display results
            st.write("Word Frequencies:")
            st.dataframe(analysis_df)
        except FileNotFoundError as e:
            st.error(str(e))
        finally:
            # Clean up temporary file
            try:
                import os
                os.remove(file_path)
            except OSError:
                pass
    
if __name__ == "__main__":
    main()