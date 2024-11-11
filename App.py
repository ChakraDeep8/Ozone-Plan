import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import math

# Constants
INITIAL_DAILY_RATE = 0.007  # 1% daily earnings on 70% of the coins
THRESHOLD = 0.5  # Restake when earnings reach 0.5 coins
RATE_DECREASE_PER_YEAR = 0.005  # Daily rate decreases by 0.5% annually

def calculate_staking_schedule(start_date, initial_coins, years_to_simulate=2):
    # Initialize variables
    schedule = []
    current_date = start_date
    coins = initial_coins
    stake_term = 1
    daily_rate = INITIAL_DAILY_RATE
    burn_schedule = []  # List to track burn dates for each stake

    # Loop through each year
    for year in range(years_to_simulate):
        while current_date.year == start_date.year + year:
            # Calculate days to reach the next 0.5 coins
            days_to_reach_threshold = math.ceil(THRESHOLD / (coins * daily_rate))
            next_stake_date = current_date + timedelta(days=days_to_reach_threshold)

            # Append the current stake to the schedule
            schedule.append({
                "Stake Term": stake_term,
                "Number of Coins": coins,
                "Next Date of Staking": next_stake_date.strftime('%d %b %Y'),
                "Days to Reach 0.5 Coins": days_to_reach_threshold,
                "Burn Date": (current_date + timedelta(days=365)).strftime('%d %b %Y')
            })

            # Add the current stake's burn date to the burn schedule
            burn_schedule.append({
                "Coins": coins,
                "Burn Date": current_date + timedelta(days=365)  # 1 year from stake date
            })

            # Update for the next restake
            current_date = next_stake_date
            coins += THRESHOLD  # Increase coins by 0.5 at each restake
            stake_term += 1

            # Check and apply any burns scheduled for this date
            burn_schedule = [entry for entry in burn_schedule if entry["Burn Date"] > current_date]
            total_burned_coins = sum(entry["Coins"] for entry in burn_schedule if entry["Burn Date"] <= current_date)
            coins -= total_burned_coins

            # Remove burned coins from schedule
            burn_schedule = [entry for entry in burn_schedule if entry["Burn Date"] > current_date]

        # Update the daily rate for the new year
        daily_rate *= (1 - RATE_DECREASE_PER_YEAR)

    # Convert list to DataFrame once after the loop
    df = pd.DataFrame(schedule)
    return df

# Streamlit app
st.header("Ozone Coin Compounding Staking Calculator with Annual Burn",divider="rainbow")

# Inputs
start_date = st.date_input("Enter the initial staking date:", value=datetime.now())
initial_coins = st.number_input("Enter the number of coins staked:", min_value=1.0)
years_to_simulate = st.slider("Number of years to simulate:", min_value=1, max_value=10, value=2)

# Button to generate schedule
if st.button("Generate Staking Schedule"):
    schedule_df = calculate_staking_schedule(start_date, initial_coins, years_to_simulate)
    
    if not schedule_df.empty:  # Ensure DataFrame has data before showing
        # Display the table
        st.write(schedule_df)
        
        # Download CSV
        csv = schedule_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Schedule as CSV",
            data=csv,
            file_name="staking_schedule.csv",
            mime="text/csv"
        )
    else:
        st.error("The generated CSV file is empty. Please check the calculation logic.")
