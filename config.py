import os
from dotenv import load_dotenv
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 8000

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
ML_MODEL_PATH = "models/model.pkl"
INDUSTRY_ENCODER_PATH = "models/industry_encoder.pkl"
ETHNICITY_ENCODER_PATH = "models/ethnicity_encoder.pkl"
CITIZEN_ENCODER_PATH = "models/citizen_encoder.pkl"
FEATURE_NAMES_PATH = "models/feature_names.pkl"
PREDICTION_COLLECTION = "prediction_history"