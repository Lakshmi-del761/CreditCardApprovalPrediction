# Credit Card Approval Prediction - Setup Guide

## Quick Start

### 1. Prerequisites
- Python 3.8 or higher
- MongoDB running (local or cloud)

### 2. Environment Configuration

Create a `.env` file in the project root with:
```
MONGO_URI=mongodb://localhost:27017/
DATABASE_NAME=credit_card_db
```

For MongoDB Atlas (cloud):
```
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/
DATABASE_NAME=credit_card_db
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python main.py
```

The application will start at: **http://localhost:5000**

## Features

### Frontend (index.html)
- ✅ Clean, professional form with 15 input fields
- ✅ Organized into logical sections
- ✅ Real-time form validation
- ✅ Loading indicator during prediction
- ✅ Color-coded results (Approved/Rejected)
- ✅ Error handling and user feedback
- ✅ Mobile responsive design

### Backend (main.py)
- ✅ Flask REST API with `/predict` endpoint
- ✅ Automatic model loading on startup
- ✅ Prediction result stored in MongoDB
- ✅ Support for all 15 required fields

### Models (in models/ folder)
- `model.pkl` - Trained classification model
- `industry_encoder.pkl` - Industry categorical encoder
- `ethnicity_encoder.pkl` - Ethnicity categorical encoder
- `citizen_encoder.pkl` - Citizenship categorical encoder
- `feature_names.pkl` - Feature names for model input

## Input Fields Required

**Personal Information**
- Gender: Male/Female
- Age: 18-120
- Ethnicity: Caucasian/Asian/African American/Latino/Other
- Citizenship: ByBirth/Naturalized/Other

**Family & Status**
- Married: Yes/No
- Bank Customer: Yes/No

**Financial Information**
- Annual Income: Positive number ($)
- Debt: Positive number ($)
- Credit Score: 300-850
- Zip Code: Text

**Employment**
- Industry: Select from 33 industries
- Years Employed: 0-70
- Currently Employed: Yes/No
- Prior Default: Yes/No

**Additional**
- Driver's License: Yes/No

## API Endpoint

### POST /predict
Send JSON with all required fields:
```json
{
  "Gender": "Male",
  "Age": 35,
  "Income": 50000,
  "Debt": 5000,
  "CreditScore": 750,
  ...
}
```

Response:
```json
{
  "prediction": "Approved"
}
```

## Troubleshooting

### Issue: Model Loading Failed
- Verify all `.pkl` files exist in `models/` folder
- Check file permissions

### Issue: MongoDB Connection Error
- Ensure `.env` file is in project root
- Verify MONGO_URI format
- Check MongoDB service is running

### Issue: Form Not Submitting
- Open browser console (F12) for error messages
- Check Network tab in DevTools
- Ensure Flask app is running on port 5000

## Database Schema

Prediction history stored in MongoDB with fields:
- All 15 input fields from the form
- Prediction result (Approved/Rejected)
- Automatic timestamp

## Next Steps

1. ✅ Update `.env` with your MongoDB credentials
2. ✅ Run `python main.py`
3. ✅ Open browser to http://localhost:5000
4. ✅ Test with sample data
5. ✅ Deploy to production when ready

## Customization

To modify the form fields or industry list, edit:
- `templates/index.html` - Frontend form
- `src/prediction.py` - Backend prediction logic

