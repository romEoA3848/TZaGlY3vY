# 代码生成时间: 2025-10-04 21:30:49
import streamlit as st
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

"""
Deep Learning Neural Network application using Streamlit
This application demonstrates how to build a simple neural network for deep learning purposes.
"""

# Define the neural network architecture
class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)  # First layer
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)  # Output layer

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# Function to create a simple dataset
def create_dataset():
    try:
        # Create a simple dataset for demonstration purposes
        x_train = torch.randn(100, 10)  # 100 samples with 10 features
        y_train = torch.randint(0, 2, (100, 1))  # Binary classification
        dataset = TensorDataset(x_train, y_train)
        dataloader = DataLoader(dataset, batch_size=10, shuffle=True)
        return dataloader
    except Exception as e:
        st.error(f"Error creating dataset: {e}")

# Function to train the neural network
def train_model(model, dataloader, epochs):
    try:
        criterion = nn.BCEWithLogitsLoss()  # Binary cross-entropy loss
        optimizer = optim.Adam(model.parameters(), lr=0.001)

        for epoch in range(epochs):
            for inputs, labels in dataloader:
                optimizer.zero_grad()
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()

            # Print the loss every epoch
            st.write(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")
    except Exception as e:
        st.error(f"Error training model: {e}")

# Streamlit interface
def main():
    st.title('Deep Learning Neural Network')

    # Input parameters
    input_size = st.number_input('Input Size', min_value=1, value=10)
    hidden_size = st.number_input('Hidden Size', min_value=1, value=5)
    num_classes = st.number_input('Number of Classes', min_value=1, value=1)
    epochs = st.number_input('Number of Epochs', min_value=1, value=10)

    # Create the model
    model = NeuralNetwork(input_size, hidden_size, num_classes)

    # Create dataset
    dataloader = create_dataset()

    # Train the model
    train_model(model, dataloader, epochs)

if __name__ == '__main__':
    main()