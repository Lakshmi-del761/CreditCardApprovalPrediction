import joblib
import config
import pandas as pd

from src.database import get_collection
class CreditCardApproval:

    def __init__(self):
        self.prediction_collection = get_collection(config.PREDICTION_COLLECTION)
    def load_model(self):
        self.model = joblib.load(config.ML_MODEL_PATH)
        return "Model Loaded Successfully"
    def load_encoders(self):
        self.industry_encoder = joblib.load(config.INDUSTRY_ENCODER_PATH)
        self.ethnicity_encoder = joblib.load(config.ETHNICITY_ENCODER_PATH)
        self.citizen_encoder = joblib.load(config.CITIZEN_ENCODER_PATH)

        return "Encoders Loaded Successfully"
    def load_feature_names(self):
        self.feature_names = joblib.load(config.FEATURE_NAMES_PATH)
        return "Feature Names Loaded Successfully"
    def predict(self,user_data):
        required_fields = [
        "Gender",
        "Age",
        "Debt",
        "Married",
        "BankCustomer",
        "Industry",
        "Ethnicity",
        "YearsEmployed",
        "PriorDefault",
        "Employed",
        "CreditScore",
        "DriversLicense",
        "Citizen",
        "ZipCode",
        "Income"
    ]
        for field in required_fields:
                if field not in user_data:return f"{field} is required."

    # Encoding starts here...
        user_data["Industry"] = self.industry_encoder.transform(
        [user_data["Industry"]]
    )[0]

        user_data["Ethnicity"] = self.ethnicity_encoder.transform(
        [user_data["Ethnicity"]]
    )[0]

        user_data["Citizen"] = self.citizen_encoder.transform(
        [user_data["Citizen"]]
    )[0]

        print(user_data)

        # Convert dictionary into a DataFrame
        input_df = pd.DataFrame([user_data])
        input_df = input_df[self.feature_names]

        print("\nInput DataFrame:")
        print(input_df)
        prediction = self.model.predict(input_df)

        print("Prediction:", prediction)

        result = "Approved" if prediction[0] == 1 else "Rejected"

        import numpy as np

    # Convert NumPy types to Python types
        for key, value in user_data.items():
            if isinstance(value, np.integer):
                user_data[key] = int(value)
            elif isinstance(value, np.floating):
                user_data[key] = float(value)

        
    
      
        user_data["Prediction"] = result

        self.prediction_collection.insert_one(user_data)

        return result
    

    
       
       









