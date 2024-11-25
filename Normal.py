import streamlit as st
import pandas as pd

# Input fields
st.subheader("Staking Details")

def normal():
    staking_amount = st.number_input("Enter Staking Amount:", value=1.0, min_value=0.5, step=0.1)
    number_of_years = st.slider("Select Number of Years:", min_value=1, max_value=13, value=10)

    # Staking logic
    if st.button("Start Staking"):
        daily_rate = 1  # Initial daily rate
        invested_coin = staking_amount  # Initial investment
        roi_data = []  # To store ROI for each year

        for year in range(1, number_of_years + 1):
            # Calculate annual returns
            returns = staking_amount * 0.7 * (daily_rate / 100) * 365
            calculation = f"{staking_amount:.2f} × 70% × {daily_rate:.2f}% × 365"

            # Remarks
            if year == 1:
                remarks = f"Initial {round(staking_amount)} ozone return on investment"
            elif year == number_of_years:
                remarks = "Final year profit realization"
            elif returns > staking_amount:
                remarks = "Strong compounding effect" if year <= 5 else "Consistent profit increase"
            else:
                remarks = "Approaching maximum return"

            # Append year data
            roi_data.append([
                year,
                round(staking_amount, 2),
                calculation,
                round(returns, 2),
                remarks
            ])

            # Update investment for next year
            if year == 1:
                returns = returns - staking_amount
                staking_amount = returns
                daily_rate = (daily_rate - 0.05)  # Reduce daily rate

            else:
                staking_amount = returns
                daily_rate = (daily_rate - 0.05)

        # Convert data to DataFrame and display
        df = pd.DataFrame(roi_data, columns=["Year", "Invested Coin", "Calculation", "Returns", "Remarks"])
        st.subheader("Returns Summary")
        st.table(df)

        # Display Final Message
        st.write(f"Final Year Returns: {round(returns)}")