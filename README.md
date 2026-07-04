# 💳 Credit Card Approval Prediction

A full-stack machine learning web application that predicts credit card approval using a Random Forest classifier. Built with Flask backend, Bootstrap responsive frontend, and MongoDB database integration.

---

## 🎯 Project Overview

This project combines machine learning with a professional web interface to:
- **Collect** applicant information through an intuitive form
- **Process** data with trained ML models
- **Predict** credit card approval instantly
- **Store** prediction history in MongoDB

## ✨ Features

### Machine Learning
- ✅ **Random Forest Classifier** - Trained on real credit card approval dataset
- ✅ **Categorical Encoding** - LabelEncoder for Industry, Ethnicity, and Citizenship
- ✅ **Feature Engineering** - 15 carefully selected applicant features
- ✅ **Data Preprocessing** - Clean dataset with proper validation

### Web Application
- ✅ **Responsive Design** - Bootstrap 5.3 with custom styling
- ✅ **Professional UI** - Background images, icons, smooth transitions
- ✅ **Form Validation** - Client-side input validation
- ✅ **Real-time Feedback** - Loading indicators and result display
- ✅ **Mobile Friendly** - Works seamlessly on all devices

### Backend
- ✅ **Flask REST API** - RESTful endpoint for predictions
- ✅ **MongoDB Integration** - Store prediction history
- ✅ **Error Handling** - Comprehensive exception management
- ✅ **Automatic Model Loading** - Pre-loads encoders on startup

---

## 🚀 Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap 5.3 |
| **Backend** | Python 3.8+, Flask 3.1.3 |
| **Database** | MongoDB |
| **ML Framework** | Scikit-learn (Random Forest) |
| **Model Serialization** | Joblib |
| **Data Processing** | Pandas, NumPy |
| **Environment** | Python-dotenv |

---

## 📋 Input Fields (15 Features)

| Category | Fields | Type |
|----------|--------|------|
| **Personal Info** | Gender, Age, Ethnicity, Citizen | Dropdown/Number |
| **Family Status** | Married, Bank Customer | Yes/No (1/0) |
| **Financial** | Income, Debt, Credit Score, Zip Code | Number |
| **Employment** | Industry, Years Employed, Employed, Prior Default | Dropdown/Yes-No |
| **Other** | Driver's License | Yes/No (1/0) |

### Field Details

**Gender**: Male (1) or Female (0)
**Age**: Applicant's age
**Debt**: Current debt amount
**Married**: Marital status (1=Yes, 0=No)
**Bank Customer**: Current bank customer (1=Yes, 0=No)
**Industry**: Sector of employment (14 categories)
**Ethnicity**: Ethnic background (5 categories)
**Years Employed**: Years in current employment
**Prior Default**: Previous loan default (1=Yes, 0=No)
**Employed**: Currently employed (1=Yes, 0=No)
**Credit Score**: Credit score (typically 300-850)
**Driver's License**: Has driver's license (1=Yes, 0=No)
**Citizen**: Citizenship status (3 categories)
**Zip Code**: Residential zip code
**Income**: Annual income

---

## 📁 Project Structure

```
CreditCardApprovalPrediction/
├── main.py                      # Flask application entry point
├── config.py                    # Configuration settings
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (MONGO_URI, DATABASE_NAME)
├── .env.example                 # Environment template
├── test_connection.py           # MongoDB connection test
│
├── src/
│   ├── prediction.py            # ML prediction logic
│   ├── database.py              # MongoDB connection helper
│   └── train.py                 # Model training script
│
├── models/                      # Trained ML models
│   ├── model.pkl                # Random Forest classifier
│   ├── industry_encoder.pkl     # Industry encoder
│   ├── ethnicity_encoder.pkl    # Ethnicity encoder
│   ├── citizen_encoder.pkl      # Citizenship encoder
│   └── feature_names.pkl        # Feature names list
│
├── data/
│   └── clean_dataset.csv        # Training dataset
│
├── templates/
│   └── index.html               # Main web form (Bootstrap)
│
├── static/
│   ├── css/
│   │   └── style.css            # Custom styling
│   ├── js/
│   │   └── script.js            # Frontend logic
│   └── images/
│       └── background.jpg       # Background image
│
└── docs/
    ├── README.md                # This file
    ├── SETUP_GUIDE.md           # Detailed setup instructions
    └── WEBAPP_SUMMARY.md        # Feature summary
```

---

## 🔧 Installation & Setup

### 1. Prerequisites
- Python 3.8 or higher
- MongoDB (local or cloud)
- pip package manager

### 2. Clone/Setup Project
```bash
cd CreditCardApprovalPrediction
```

### 3. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root:

**Local MongoDB:**
```env
MONGO_URI=mongodb://localhost:27017/
DATABASE_NAME=credit_card_db
```

**MongoDB Atlas (Cloud):**
```env
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/
DATABASE_NAME=credit_card_db
```

### 6. Test MongoDB Connection (Optional)
```bash
python test_connection.py
```

### 7. Run the Application
```bash
python main.py
```

The app will start at: **http://localhost:5000**

---

## 🎮 How to Use

### Using the Web Interface

1. **Open Browser**: Navigate to `http://localhost:5000`
2. **Fill Form**: Enter applicant information in all fields
3. **Submit**: Click "Get Prediction" button
4. **View Result**: See Approved ✅ or Rejected ❌
5. **History**: Predictions are saved to MongoDB

### API Usage (Direct)

**Endpoint**: `POST /predict`

**Request Example**:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Gender": 1,
    "Age": 35,
    "Debt": 5000.50,
    "Married": 1,
    "BankCustomer": 1,
    "Industry": "Financials",
    "Ethnicity": "White",
    "YearsEmployed": 8.5,
    "PriorDefault": 0,
    "Employed": 1,
    "CreditScore": 750,
    "DriversLicense": 1,
    "Citizen": "ByBirth",
    "ZipCode": 12345,
    "Income": 75000
  }'
```

**Response Example**:
```json
{
  "prediction": "Approved"
}
```

---

## 📊 Model Training

The ML model was trained using:

```python
# From src/train.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Data split: 80% training, 20% testing
# Features: 15 applicant characteristics
# Target: Approved (1) or Rejected (0)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
accuracy = accuracy_score(y_test, y_pred)  # Model accuracy
```

### To Retrain the Model

```bash
python src/train.py
```

This will:
- Load clean_dataset.csv
- Encode categorical variables
- Split data (80/20)
- Train Random Forest model
- Save all models to `models/` folder

---

## 📈 Model Performance

- **Algorithm**: Random Forest Classifier
- **Training Samples**: [Check dataset]
- **Features**: 15
- **Target Classes**: 2 (Approved/Rejected)
- **Random State**: 42 (for reproducibility)

---

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| **Models not found error** | Run `python src/train.py` to train and save models |
| **MongoDB connection failed** | Check `.env` file and verify MongoDB is running |
| **Port 5000 already in use** | Change port in `main.py`: `app.run(port=5001)` |
| **ModuleNotFoundError** | Run `pip install -r requirements.txt` |
| **Form not submitting** | Open DevTools (F12) → Console for error details |
| **No background image** | Ensure `static/images/background.jpg` exists |

---

## 📚 File Reference

### main.py
- Entry point for the Flask application
- Routes: `/` (form) and `/predict` (API)
- Loads all models on startup

### src/prediction.py
- `CreditCardApproval` class handles predictions
- Encodes categorical variables
- Stores results in MongoDB
- Converts NumPy types to Python types

### src/train.py
- Loads training data from CSV
- Encodes categorical features
- Trains Random Forest model
- Saves models with Joblib

### src/database.py
- MongoDB connection helper
- `get_collection()` function for database access

### config.py
- Configuration from `.env` file
- Model and encoder file paths
- Database collection names

### templates/index.html
- Bootstrap-based responsive form
- Links to CSS and JS files
- 15 input fields organized in grid

### static/css/style.css
- Custom styling for Bootstrap
- Responsive design
- Animation effects
- Color scheme

### static/js/script.js
- Form submission handler
- API request to `/predict` endpoint
- Result display logic
- Error handling

---

## 🚀 Deployment

### Deploy to Heroku

1. **Create Heroku App**:
   ```bash
   heroku create your-app-name
   ```

2. **Set Environment Variables**:
   ```bash
   heroku config:set MONGO_URI=your_mongodb_uri
   heroku config:set DATABASE_NAME=credit_card_db
   ```

3. **Deploy**:
   ```bash
   git push heroku main
   ```

### Deploy to AWS, Google Cloud, or Azure
- Use similar environment variable setup
- Ensure MongoDB URI is accessible from deployed environment
- Upload all project files

---

## 📝 Database Schema

**Collection**: `prediction_history`

**Sample Document**:
```json
{
  "_id": ObjectId("..."),
  "Gender": 1,
  "Age": 35,
  "Debt": 5000.50,
  "Married": 1,
  "BankCustomer": 1,
  "Industry": "Financials",
  "Ethnicity": "White",
  "YearsEmployed": 8.5,
  "PriorDefault": 0,
  "Employed": 1,
  "CreditScore": 750,
  "DriversLicense": 1,
  "Citizen": "ByBirth",
  "ZipCode": 12345,
  "Income": 75000,
  "Prediction": "Approved"
}
```

---

## 🔐 Security Considerations

- ✅ Environment variables for sensitive data
- ✅ Input validation on backend
- ✅ CORS considerations for API
- ⚠️ **Production**: Use HTTPS, add authentication, validate all inputs

---

## 📦 Requirements

See `requirements.txt` for complete list:

- **Flask** 3.1.3 - Web framework
- **scikit-learn** 1.9.0 - Machine learning
- **pandas** 3.0.3 - Data processing
- **NumPy** 2.5.0 - Numerical computing
- **PyMongo** 4.17.0 - MongoDB driver
- **Joblib** 1.5.3 - Model serialization
- **python-dotenv** 1.2.2 - Environment variables

---

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make changes and test thoroughly
4. Commit changes (`git commit -m 'Add improvement'`)
5. Push to branch (`git push origin feature/improvement`)
6. Create Pull Request

---

## 📄 License

This project is open source and available for educational and commercial use.

---

## 👨‍💻 Author

Developed as a full-stack machine learning project combining ML model training, backend API development, and responsive frontend design.

---

## 📞 Support & Documentation

- **Setup Help**: See [SETUP_GUIDE.md](SETUP_GUIDE.md)
- **Features Overview**: See [WEBAPP_SUMMARY.md](WEBAPP_SUMMARY.md)
- **Issues**: Check troubleshooting section above

---

## ✅ Checklist for First Run

- [ ] Create `.env` with MongoDB URI
- [ ] Run `pip install -r requirements.txt`
- [ ] Verify models exist in `models/` folder
- [ ] Run `python main.py`
- [ ] Open `http://localhost:5000` in browser
- [ ] Test with sample data
- [ ] Check MongoDB for stored predictions

---

**Last Updated**: July 4, 2026
**Status**: ✅ Production Ready
