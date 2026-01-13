import streamlit as st
import pandas as pd
from model import train_model

st.title("Air Quality Prediction & Health Alert System")

data = pd.read_csv("aqi_data.csv")

city = st.selectbox("Select City", data["City"].unique())

# Get latest data for selected city
city_data = data[data["City"] == city]
latest_row = city_data.sort_values("Datetime", ascending=False).iloc[0]

pm25 = latest_row["PM2.5"]
pm10 = latest_row["PM10"]
no2  = latest_row["NO2"]
so2  = latest_row["SO2"]
co   = latest_row["CO"]

st.subheader("Current Pollution Levels (Latest Available Data)")
st.write(f"PM2.5: {pm25}")
st.write(f"PM10: {pm10}")
st.write(f"NO2: {no2}")
st.write(f"SO2: {so2}")
st.write(f"CO: {co}")

if st.button("Predict Current AQI"):
    model = train_model()
    prediction = model.predict([[pm25, pm10, no2, so2, co]])[0]

    st.success(f"Predicted AQI: {int(prediction)}")

    if prediction <= 50:
        st.info("Good air quality 😊")
    elif prediction <= 100:
        st.warning("Moderate air quality ⚠️")
    elif prediction <= 200:
        st.error("Poor air quality 🚨 Avoid outdoor activity")
    else:
        st.error("Severe air quality ☠️ Health risk")
