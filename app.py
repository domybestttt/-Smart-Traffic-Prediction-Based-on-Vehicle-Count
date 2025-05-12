import streamlit as st
import numpy as np
import joblib

# Load the saved model, scaler, and label encoder
model = joblib.load('traffic_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Set page configuration
st.set_page_config(
    page_title="TRAFFIC FLOW PREDICTION",
    page_icon="🚦",
    layout="centered",
)

# Custom CSS styling
st.markdown("""
    <style>
    .stApp {
    background-color: #87CEEB; /* Sunset Orange */
    font-family: 'Verdana', sans-serif;
}


    .stSidebar {
        background-color: #B7202E !important; /* RED */
    }

    .header-text {
        font-size: 2.7rem;
        font-weight: bold;
        color: #000000;
        text-align: center;
        margin-top: 20px;
    }

    .description-text, .sidebar-text, .result-text, .footer-text {
        font-size: 1.2rem;
        color: #000000;
    }

    .result-text {
        font-size: 1.8rem;
        color: #004d4d;
        font-weight: bold;
    }

    .footer-text {
        font-size: 1rem;
        color: #f0f0f0;
        text-align: center;
        margin-top: 2rem;
    }

    .stButton>button {
        background-color: #004d4d;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 1rem;
    }

    .stButton>button:hover {
        background-color: #003333;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header-text">🚦 TRAFFIC FLOW PREDICTION</div>', unsafe_allow_html=True)

# Description
st.markdown("""
    <div class="description-text">
    <br>  
    Provide vehicle counts to predict traffic situation: <i>Low, Normal, or Heavy</i>.  
    </div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown('<div class="sidebar-text"><b>🚘 VEHICLE COUNTS</b></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-text">Adjust the values:</div>', unsafe_allow_html=True)

car_count = st.sidebar.number_input("🚗 Car Count", min_value=0, value=50)
bike_count = st.sidebar.number_input("🏍️ Bike Count", min_value=0, value=10)
bus_count = st.sidebar.number_input("🚌 Bus Count", min_value=0, value=50)
truck_count = st.sidebar.number_input("🚛 Truck Count", min_value=0, value=20)

# Prediction
if st.sidebar.button("🔍 Predict Traffic Situation"):
    test_input = np.array([[car_count, bike_count, bus_count, truck_count]])
    test_input_scaled = scaler.transform(test_input)
    predicted_class = model.predict(test_input_scaled)
    predicted_label = label_encoder.inverse_transform(predicted_class)

    st.markdown('<div class="result-text">🚦 Prediction Result</div>', unsafe_allow_html=True)
    st.success(f"The predicted traffic situation is: **{predicted_label[0].capitalize()}**")

# Footer
st.markdown('<div class="footer-text">NIKSHITA G.</div>', unsafe_allow_html=True)
