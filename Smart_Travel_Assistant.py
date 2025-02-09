import streamlit as st
import datetime

st.title("Smart Travel Assistant")

# User Destination Selection
st.header("Select Your Destination")
destination = st.selectbox("Destination:", ["Paris", "New York", "Tokyo", "Dubai", "Sydney"], key="destination_select")
weather = st.radio("Weather Condition:", ["Sunny", "Rainy", "Cold"], key="weather_radio")

# Travel Expense Calculator
st.header("Expense Calculator")
days = st.slider("Travel Days:", 1, 30, 5)
daily_budget = st.number_input("Daily Budget:", min_value=0.0, value=100.0)
flight_cost = st.number_input("Flight Cost (Optional):", min_value=0.0)
hotel_cost = st.number_input("Hotel Cost (Optional):", min_value=0.0)

# Total Estimated Cost
total_cost = (days * daily_budget) + flight_cost + hotel_cost
st.write(f"**Total Trip Cost:** ${total_cost:.2f}")

# Packing Checklist
st.header("Packing Checklist")
packing_list = {"Sunny": ["Sunglasses", "Sunscreen", "Hat"], "Rainy": ["Umbrella", "Raincoat", "Waterproof Shoes"], "Cold": ["Jacket", "Gloves", "Warm Clothes"]}
custom_list = st.multiselect("Edit Packing List:", packing_list[weather], packing_list[weather])
st.text_area("Packing List:", "\n".join(custom_list), height=100)

# Travel Summary & File Saving
st.header("Travel Summary")
if st.button("Save Details"):
    with open("travel_summary.txt", "a") as file:
        file.write(f"Destination: {destination}\nWeather: {weather}\nTotal Cost: ${total_cost:.2f}\nPacking List: {', '.join(custom_list)}\n")
    st.success("Details Saved!")

if st.button("View Past Plans"):
    try:
        with open("travel_summary.txt", "r") as file:
            st.text(file.read())
    except FileNotFoundError:
        st.error("No plans found.")

# Countdown Timer
trip_date = st.date_input("Trip Start Date:")
if trip_date >= datetime.date.today():
    st.write(f"**Days Left:** {(trip_date - datetime.date.today()).days}")

# Currency Converter (Simplified without External API)
st.header("Currency Converter")
exchange_rates = {"USD": {"EUR": 0.85, "GBP": 0.75, "AUD": 1.4}, "EUR": {"USD": 1.18, "GBP": 0.88, "AUD": 1.65}, "GBP": {"USD": 1.33, "EUR": 1.14, "AUD": 1.88}, "AUD": {"USD": 0.72, "EUR": 0.61, "GBP": 0.53}}
base_currency = st.selectbox("Base Currency:", ["USD", "EUR", "GBP", "AUD"], key="base_currency_select")
target_currency = st.selectbox("Target Currency:", ["USD", "EUR", "GBP", "AUD"], key="target_currency_select")
amount = st.number_input("Amount to Convert:", min_value=0.0, value=total_cost)
if st.button("Convert"):
    if base_currency != target_currency:
        converted_amount = amount * exchange_rates.get(base_currency, {}).get(target_currency, 1)
        st.write(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        st.write(f"{amount} {base_currency} = {amount:.2f} {target_currency}")

# Trip Rating System
st.header("Trip Rating")
rating = st.slider("Rate Your Trip (1 to 5 Stars):", 1, 5)
trip_review = st.text_area("Review (Optional):")
if st.button("Submit Rating"):
    with open("trip_reviews.txt", "a") as file:
        file.write(f"Destination: {destination}, Rating: {rating} Stars, Review: {trip_review}\n")
    st.success("Thank you for your feedback!")
