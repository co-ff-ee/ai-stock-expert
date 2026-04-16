from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def train_model(data):
    # Drop rows with NaN values created by indicators
    data = data.dropna()

    X = data[['rsi', 'macd']]
    y = data['Close']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

def predict_price(model, latest_data):
    # Ensure latest_data is a flat list of numbers
    prediction = model.predict([latest_data])
    # Convert prediction to a single float number
    return float(np.array(prediction).ravel()[0])
