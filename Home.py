import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from PIL import Image
from streamlit_lottie import st_lottie

def home():
    st.subheader("Revolutionizing Blockchain with AI and PoS Technology", divider="rainbow")
    st.write(
        "The Ozone Chain is a cutting-edge blockchain network utilizing Proof-of-Stake (PoS) for sustainable and efficient decentralized solutions. "
        "Explore the white paper and learn more about its innovative features."
    )
    st.markdown("##### Explore More 👇")


    st.write(
        "Browse the Ozone Chain white paper to gain in-depth insights into the platform's architecture, governance, and tokenomics."
    )

    # Embed the PDF Viewer
    pdf_url = "res/Ozone-white-paper.pdf"
    pdf_viewer(pdf_url)