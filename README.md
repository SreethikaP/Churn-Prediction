# Churn-Prediction
A simple machine learning web application built with Streamlit to predict customer churn based on user input. The model is trained on customer data and deployed using an interactive web interface.

📈 Features

Predicts whether a customer will churn based on input features.
User-friendly web app interface built using Streamlit.
Pre-trained machine learning model loaded for real-time predictions.

🛠 Technologies Used

Python
Streamlit
Scikit-learn
Pickle (for model serialization)


📂 Project Structure
```
├── model.h5                  # Trained ML classification model
├── regression_model.h5       # Trained ML regression model
├── app.py                    # Streamlit web app for ANN Classification
├── regressionapp.py          # Streamlit web app for ANN regression
├── experiments.ipynb
├── salaryregression.iynb
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```
🚀 Installation

1. Clone the repository
   ```
     git clone https://github.com/SreethikaP/Churn-Prediction.git
     cd Churn-Prediction
   ```
2. Create a virtual environment
   ```
   python -m venv venv
   source venv/bin/activate    # On Mac/Linux
   venv\Scripts\activate       # On Windows
   ```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Run the Streamlit app
   ```
   streamlit run regressionapp.py
```


## 🌐 Live Demo

Check out the live deployed app here:  
👉 [Churn Prediction App on Streamlit](https://churn-prediction-8jh2tfstfxmejkqfdrehcq.streamlit.app)


