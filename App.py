import streamlit as st
from Normal import normal
from Compounding import main
from Home import home
from PIL import Image

icon = Image.open("res/ozone.jpg")
st.set_page_config(
    page_title="Ozone Chain Project",
    page_icon=icon,
    layout="wide",
    initial_sidebar_state="collapsed"
)
# Set Home page as default
st.title("Ozone Chain Project")
page = st.selectbox("Select Plan 👇", ["🏠 Home", "📊 Normal Staking Plan", "📈 Compounding Staking Plan"])

if page == "🏠 Home":
    home()
elif page == "📊 Normal Staking Plan":
    normal()
elif page == "📈 Compounding Staking Plan":
    main()