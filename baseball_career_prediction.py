"""
Class: Machine Learning: CS379
Author: Brian Baca
Date: January 20, 2024
Description: Predicting career home runs in Major League Baseball players using Linear Regression.
"""

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the data
file_path = 'Hitters.xlsx'  # If the file is in the same directory as your script
data = pd.read_excel(file_path)

# Explore the data
print(data.head())

# Preprocess the data
features = data[['Years', 'HmRun']]
target = data['CHmRun']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Build a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Visualize the predictions
plt.scatter(X_test['Years'], y_test, color='black', label='Actual')
plt.scatter(X_test['Years'], predictions, color='blue', label='Predicted')
plt.xlabel('Years')
plt.ylabel('Career Home Runs')
plt.legend()
plt.show()