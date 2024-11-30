import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Constants
DAILY_ROI_RATE = 0.7
ADDITIONAL_1_RATE = 0.007  # Updated for 1 coin
DAYS_IN_YEAR = 365

def calculate_daily_roi_rate(daily_rate: float, year: int) -> float:
    """Calculate the daily ROI rate."""
    if year == 1:
        return DAILY_ROI_RATE * (daily_rate / 100)
    else:
        daily_rate -= (5 / 100)
        return DAILY_ROI_RATE * (daily_rate / 100)

def calculate_compounding(staking_amount: float, years: int, start_date: datetime) -> pd.DataFrame:
    """Calculate compounding staking details."""
    stake_history = []
    total_days = years * DAYS_IN_YEAR
    daily_rate = 1
    current_date = start_date
    initial_stake_count = staking_amount
    total_units = 0
    wallet_balance = 0
    days_to_next_unit = 0
    expire_dates = {}

    for day in range(1, total_days + 1):
        if day % DAYS_IN_YEAR == 0:
            daily_rate -= (5 / 100)

        daily_roi_rate = calculate_daily_roi_rate(daily_rate, (day // DAYS_IN_YEAR) + 1)
        additional_1 = 0

        # Check for expire dates
        expired_stakes = [stake for stake in expire_dates if expire_dates[stake] <= current_date]
        for stake in expired_stakes:
            del expire_dates[stake]
            total_units -= 1
            staking_amount -= 1  # Update to subtract 1 coin

        # Calculate additional 1 coin
        for stake in expire_dates:
            if expire_dates[stake] > current_date:
                additional_1 += ADDITIONAL_1_RATE

        if current_date >= (start_date + timedelta(days=365)):
            staking_amount -= initial_stake_count
            initial_stake_count = 0
        daily_return = (daily_roi_rate * initial_stake_count) + additional_1
        wallet_balance += daily_return
        days_to_next_unit += 1

        if wallet_balance >= 1:  # Update threshold to 1 coin
            staking_amount += 1
            total_units += 1
            if total_units >= 365:
                staking_amount += 1
                total_units += 1
            stake_expire = current_date + timedelta(days=DAYS_IN_YEAR)
            expire_dates[stake_expire] = stake_expire
            stake = {
                "Stake Date": current_date.strftime("%d %B %Y"),
                "Staking Amount": round(staking_amount, 4),
                "Present Wallet Balance": round(wallet_balance, 4),
                "Daily ROI": round(daily_return, 4),
                "Days to Next 1 Coin": days_to_next_unit,
                "Total Units": total_units,
                "Burning Date": stake_expire.strftime("%d %B %Y")
            }
            stake_history.append(stake)
            wallet_balance -= 1
            days_to_next_unit = 0

        current_date += timedelta(days=1)

    return pd.DataFrame(stake_history)


def full():
    st.title("Compounding Staking Plan")
    st.subheader("Staking Details", divider="gray")

    staking_amount = st.number_input("Staking Amount", min_value=0.5, value=1.0, step=0.5)  # Adjust step and min value
    number_of_years = st.slider("Number of Years", min_value=1, max_value=10, value=1)
    start_date = st.date_input("Date of Staking", value=datetime.today(), format="DD/MM/YYYY")

    if st.button("Generate Table"):
        start_date = datetime.combine(start_date, datetime.min.time())
        compounding_table = calculate_compounding(staking_amount, number_of_years, start_date)
        st.success("Compounding Table Generated Successfully!")
        st.write(compounding_table)
        st.download_button(
            "Download",
            compounding_table.to_csv(index=False),
            "compounding_staking_table.csv",
            "text/csv"
        )


if __name__ == "__main__":
    full()
