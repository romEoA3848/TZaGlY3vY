# 代码生成时间: 2025-08-10 00:49:50
Streamlit Interactive Chart Generator

This application allows users to create interactive charts
by selecting different chart types and inputting data.
It uses Streamlit for the web interface and Plotly for charting.
*/

import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np

# Function to create a single chart
def create_chart(chart_type, data):
    """
    Creates a chart based on the chart type and input data.
    
    Args:
    chart_type (str): The type of chart to create.
    data (pd.DataFrame): The data to visualize in the chart.
    
    Returns:
    fig (plotly.graph_objs.Figure): The created chart.
    """
    try:
        if chart_type == 'line':
            return px.line(data)
        elif chart_type == 'bar':
            return px.bar(data)
        elif chart_type == 'scatter':
            return px.scatter(data)
        elif chart_type == 'box':
            return px.box(data)
        elif chart_type == 'histogram':
            return px.histogram(data)
        elif chart_type == 'area':
            return px.area(data)
        else:
            raise ValueError("Unsupported chart type.")
    except Exception as e:
        st.error(f"Failed to create chart: {e}")
        return None

# Function to create a subplot with multiple charts
def create_subplot(charts):
    """
    Creates a subplot with multiple charts.
    
    Args:
    charts (list): A list of tuples containing chart types and data for each chart.
    
    Returns:
    fig (plotly.graph_objs.Figure): The created subplot.
    """
    try:
        fig = make_subplots(rows=len(charts), cols=1)
        for i, (chart_type, data) in enumerate(charts):
            fig.add_trace(create_chart(chart_type, data), row=i+1, col=1)
        return fig
    except Exception as e:
        st.error(f"Failed to create subplot: {e}")
        return None

# Main function to run the application
def main():
    st.title('Interactive Chart Generator')
    
    # Input data
    st.header('Input Data')
    data = st.text_area('Enter data in CSV format:', height=200)
    
    # Check if data is provided
    if data:
        try:
            # Convert data to DataFrame
            df = pd.DataFrame([x.split(',') for x in data.split('
')]).transpose()
            df.columns = df.iloc[0]
            df = df.drop(0).astype(float)
        except Exception as e:
            st.error(f"Failed to parse data: {e}")
            return
            
        # Chart type selection
        st.header('Chart Type')
        chart_types = ['line', 'bar', 'scatter', 'box', 'histogram', 'area']
        selected_charts = st.multiselect('Select chart types:', chart_types)
        
        # Create and display charts
        charts = [(c, df) for c in selected_charts]
        subplot = create_subplot(charts)
        
        if subplot:
            st.plotly_chart(subplot)
        else:
            st.error('Failed to create subplot.')
    else:
        st.error('No data provided.')

# Run the application
if __name__ == '__main__':
    main()