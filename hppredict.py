import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r"C:\Users\rumjhum\Desktop\House Price\train.csv")

# Define features and target
features = ["GrLivArea", "BedroomAbvGr", "FullBath"]
X = data[features]
y = data["SalePrice"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make pimport streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r"C:\Users\rumjhum\Desktop\House Price\train.csv")

# Define features and target
features = ["GrLivArea", "BedroomAbvGr", "FullBath"]
X = data[features]
y = data["SalePrice"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Streamlit App
st.set_page_config(page_title="House Price Predictor", page_icon="🏠")

st.title("🏠 House Price Predictor")
st.write("This app predicts house prices using a Linear Regression model.")

# Display dataset information
if st.checkbox("Show Dataset"):
    st.write("### Dataset")
    st.dataframe(data.head())

# Model Evaluation Metrics
st.write("### Model Performance Metrics")
st.write(f"- Mean Squared Error: **{mse:.2f}**")
st.write(f"- R-Squared Value: **{r2:.2f}**")

# Plot Actual vs Predicted Prices
st.write("### Actual vs Predicted Prices")
fig, ax = plt.subplots()
ax.scatter(y_test, y_pred, alpha=0.5)
ax.set_xlabel("Actual Prices")
ax.set_ylabel("Predicted Prices")
ax.set_title("Actual Prices vs Predicted Prices")
st.pyplot(fig)

# Prediction Interface
st.write("### Predict House Price")
GrLivArea = st.number_input("Enter Ground Living Area (in sq ft)", min_value=0, value=2000)
BedroomAbvGr = st.number_input("Enter Number of Bedrooms", min_value=0, value=3)
FullBath = st.number_input("Enter Number of Full Bathrooms", min_value=0, value=2)

if st.button("Predict Price"):
    new_data = pd.DataFrame({'GrLivArea': [GrLivArea], 'BedroomAbvGr': [BedroomAbvGr], 'FullBath': [FullBath]})
    predicted_price = model.predict(new_data)
    st.success(f"Predicted Price: **${predicted_price[0]:,.2f}**")

# Dollar to Rupee Converter
st.write("### Dollar to Rupee Converter")
dollar_amount = st.number_input("Enter amount in USD", min_value=0.0, value=1.0)
exchange_rate = 82.0  # Approximate exchange rate
rupee_amount = dollar_amount * exchange_rate
if st.button("Convert to INR"):
    st.success(f"${dollar_amount} is approximately ₹{rupee_amount:,.2f}")
