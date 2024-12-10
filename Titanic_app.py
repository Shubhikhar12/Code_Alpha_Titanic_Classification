# titanic_app.py
import streamlit as st
import joblib

# Load the model
model = joblib.load('titanic_model.pkl')

# Streamlit app title
st.title("Titanic Survival Prediction")

# Input form
pclass = st.selectbox("Ticket Class (Pclass)", [1, 2, 3])
sex = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=0, max_value=100, value=30)
fare = st.number_input("Fare Paid", min_value=0.0, value=50.0)
embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])

# Convert inputs
sex = 1 if sex == "Male" else 0
embarked_mapping = {"C": 0, "Q": 1, "S": 2}
embarked = embarked_mapping[embarked]

# Prediction
if st.button("Predict"):
    result = model.predict([[pclass, sex, age, fare, embarked]])
    if result[0] == 1:
        st.success("Survived!")
    else:
        st.error("Did Not Survive")
