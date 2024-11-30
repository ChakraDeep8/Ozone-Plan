import streamlit as st
import json
from Plans.Normal import normal
from Plans.Half_Coin_Compounding import half
from Plans.Home import home
from Plans.Full_Coin_Compounding import full
from PIL import Image
from streamlit_lottie import st_lottie  # Import Lottie renderer

# Load Lottie file
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

icon = Image.open("res/ozone.jpg")
st.set_page_config(
    page_title="Ozone Chain Project",
    page_icon=icon,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load translations
def load_translations(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

# Switch language
def switch_language(language):
    st.session_state.language = language

# Main app
def main_app():
    translations = load_translations("res/translations.json")

    # Sidebar for language selection
    with st.sidebar:
        st.sidebar.title(translations["common"]["Settings"][st.session_state.language])
        st.sidebar.subheader(translations["common"]["select_language"][st.session_state.language])
        for lang, lang_name in [("en", "English"), ("bn", "বাংলা"), ("hi", "हिंदी")]:
            if st.sidebar.button(lang_name):
                switch_language(lang)

    # Page content
    st.header(translations["app"]["title"][st.session_state.language], divider="rainbow")

    # Add Lottie animation below the title
    lottie_animation = load_lottiefile("res/Crypo_ozone.json")  # Path to your Lottie file
    col1, col2, col3 = st.columns(3)
    with col1:

        st_lottie(lottie_animation, height=400, key="lottie")


    page = st.selectbox(
        translations["app"]["select_plan"][st.session_state.language],
        [
            translations["app"]["home"][st.session_state.language],
            translations["app"]["normal_plan"][st.session_state.language],
            translations["app"]["half_compound_plan"][st.session_state.language],
            translations["app"]["full_compound_plan"][st.session_state.language]
        ]
    )

    if page == translations["app"]["home"][st.session_state.language]:
        home(translations, st.session_state.language)
    elif page == translations["app"]["normal_plan"][st.session_state.language]:
        normal()
    elif page == translations["app"]["half_compound_plan"][st.session_state.language]:
        half()
    elif page == translations["app"]["full_compound_plan"][st.session_state.language]:
        full()


if __name__ == "__main__":
    if "language" not in st.session_state:
        st.session_state.language = "en"
    main_app()
