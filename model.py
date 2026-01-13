import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model():
    data = pd.read_csv("aqi_data.csv")

    X = data[["PM2.5", "PM10", "NO2", "SO2", "CO"]]
    y = data["AQI"]

    model = LinearRegression()
    model.fit(X, y)

    return model
