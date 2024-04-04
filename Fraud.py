# credit_fraud_detection.py
# Author: Brian Baca
# Date: 2024-01-21
# Class: CS3379

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load the dataset
file_name = 'CreditFraud.xlsx'
df = pd.read_excel(file_name)

# Data preprocessing
if 'class' in df.columns:
    X = df.drop('class', axis=1)  # Features
    y = df['class']  # Target variable

    # Split the data into training, testing, and validation sets
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
    X_test, X_val, y_test, y_val = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    # Define numerical and categorical features
    numerical_features = X.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X.select_dtypes(include=['object']).columns

    # Create a preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(), categorical_features)
        ])

    # Create and train the model (Random Forest Classifier as an example)
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier())
    ])

    model.fit(X_train, y_train)

    # Make predictions on validation set
    y_val_pred = model.predict(X_val)

    # Evaluate the model on validation set
    conf_matrix_val = confusion_matrix(y_val, y_val_pred)
    class_report_val = classification_report(y_val, y_val_pred)

    # Print results to the console
    print("Confusion Matrix (Validation Set):\n", conf_matrix_val)
    print("\nClassification Report (Validation Set):\n", class_report_val)
else:
    print("Column 'class' not found in the dataset.")