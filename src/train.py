import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
data = pd.read_csv("data/clean_dataset.csv")
print(data.head())
 
 # Display dataset information
print(data.info())

# Check for missing values
print(data.isnull().sum())

# Check target variable distribution
print(data["Approved"].value_counts())
# Create LabelEncoder object
industry_encoder = LabelEncoder()
ethnicity_encoder = LabelEncoder()
citizen_encoder = LabelEncoder()
# Encode categorical columns
data["Industry"] = industry_encoder.fit_transform(data["Industry"])
data["Ethnicity"] = ethnicity_encoder.fit_transform(data["Ethnicity"])
data["Citizen"] = citizen_encoder.fit_transform(data["Citizen"])

# Print all classes
print("Industry Classes:")
print(industry_encoder.classes_)

print("\nEthnicity Classes:")
print(ethnicity_encoder.classes_)

print("\nCitizen Classes:")
print(citizen_encoder.classes_)

# Verify the changes
print(data.head())

# Separate features and target
X = data.drop("Approved", axis=1)
feature_names = X.columns.tolist()
print(X.columns)
y = data["Approved"]

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Features:", X_train.shape)
print("Testing Features:", X_test.shape)

print("Training Target:", y_train.shape)
print("Testing Target:", y_test.shape)

# Create the model
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict using the test dataset
y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred)

# Calculate model accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy}")
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model
joblib.dump(model, "models/model.pkl")

joblib.dump(industry_encoder, "models/industry_encoder.pkl")
joblib.dump(ethnicity_encoder, "models/ethnicity_encoder.pkl")
joblib.dump(citizen_encoder, "models/citizen_encoder.pkl")
joblib.dump(feature_names, "models/feature_names.pkl")

print("✅ Model saved successfully!")

print(data.head())
print(data.dtypes)