import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import requests


def download_pdf(pdf_url=None, button_text=None):
    """Downloads the PDF file using st.download_button."""
    try:
        response = requests.get(pdf_url, stream=True)
        response.raise_for_status()  # Raise an error for bad HTTP status codes

        # Create a downloadable button
        st.download_button(
            label=button_text,
            data=response.content,
            file_name="MetaOzone_White_Paper.pdf",
            mime="application/pdf",
        )
    except requests.exceptions.RequestException as e:
        st.error(f"Error downloading the PDF: {e}")


def home(translations, lang):
    st.subheader(translations["home"]["subheader"][lang], divider="rainbow")
    st.write(translations["home"]["description"][lang])
    st.markdown(f"##### {translations['common']['download'][lang]} 👇")

    # Embed the PDF Viewer
    local_pdf_url = "res/Ozone-white-paper.pdf"  # Local PDF file path
    pdf_github_url = "https://raw.githubusercontent.com/ChakraDeep8/Ozone-Plan/main/res/Ozone-white-paper.pdf"

    # Button to download PDF
    download_pdf(pdf_github_url, button_text=translations["home"]["whitepaper"][lang])

    # Display PDF in Viewer
    pdf_viewer(local_pdf_url)
