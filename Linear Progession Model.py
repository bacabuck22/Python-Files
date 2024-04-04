import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Step 1: Load the dataset
data = pd.read_csv('Places.csv')

# Step 2: Prepare the data
target_column = 'ACCESS2_CrudePrev'
features = data.drop(target_column, axis=1)  # Features excluding the target column
target = data[target_column]  # Target variable

# Step 3: Data Cleansing and Preprocessing
data.dropna(inplace=True)

# Separate categorical and numeric features
categorical_features = ['CountyName', 'StateAbbr', 'StateDesc']
numeric_features = [col for col in features.columns if col not in categorical_features]

# Preprocessing: One-hot encoding for categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(sparse=True), categorical_features),
    ],
    remainder='passthrough'
)

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Step 5: Create a pipeline with preprocessing and model
model = LinearRegression()

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', model)
])

# Step 6: Train the model and make predictions
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)