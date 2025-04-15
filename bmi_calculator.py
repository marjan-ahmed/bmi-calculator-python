import streamlit as st
import time

# BMI_FORMULA = weight/height * height

st.set_page_config("BMI Calculator", "📝")

st.title("BMI (Body Mass Index) :green-background[Calculator]")

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # convert cm to meters
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

with st.form("bmi_form"):
    name = st.text_input("Enter your name")
    weight = st.number_input("Enter your weight (kg)", min_value=1.0)
    height = st.number_input("Enter your height (cm)", min_value=1.0)
    submitted = st.form_submit_button("Calculate")

    if submitted:
        bmi = calculate_bmi(weight, height)

        st.success(f"{name}, your BMI is {bmi}")

st.markdown(f"<h6 style='text-align: center; color: black;'>© {time.strftime} 2025 Mohammad Marjan Ahmed. All rights reserved.</h6>", unsafe_allow_html=True)