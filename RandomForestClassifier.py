# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer  # Import imputer

# Load the dataset
titanic_data = pd.read_excel("Titanic.xlsx")

# Select features (X) and target variable (y)
features = titanic_data[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare']]
target = titanic_data['survived']

# Convert categorical variables to numerical using one-hot encoding
features = pd.get_dummies(features, columns=['sex'], drop_first=True)

# Handle missing values by imputing with the mean
imputer = SimpleImputer(strategy='mean')
features_imputed = pd.DataFrame(imputer.fit_transform(features), columns=features.columns)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features_imputed, target, test_size=0.2, random_state=42)

# Create a Random Forest Classifier
rf_classifier = RandomForestClassifier(random_state=42)

# Train the classifier
rf_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Display classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))