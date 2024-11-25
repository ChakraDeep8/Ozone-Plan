import streamlit as st
import base64

def home():
    # Title and Description
    st.header("Ozone Chain Project")
    st.subheader("Revolutionizing Blockchain with AI and PoS Technology", divider="gray")
    st.write(
        "The Ozone Chain is a cutting-edge blockchain network utilizing Proof-of-Stake (PoS) for sustainable and efficient decentralized solutions. "
        "Explore the white paper and learn more about its innovative features."
    )

    st.write(
        "Browse the Ozone Chain white paper to gain in-depth insights into the platform's architecture, governance, and tokenomics."
    )

    # Embed PDF Viewer
    pdf_file_path = "res/Ozone white papper.pdf"  # Path to the uploaded PDF file
    with open(pdf_file_path, "rb") as pdf_file:
        base64_pdf = base64.b64encode(pdf_file.read()).decode("utf-8")

    pdf_viewer_html = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}" 
                width="100%" height="800px" 
                style="border:none;"></iframe>
    """
    st.markdown(pdf_viewer_html, unsafe_allow_html=True)

    # Additional Information Section
    st.write("### Explore More")
    st.write(
        """
        - Learn about the [Ozone Chain ecosystem](https://www.ozonechain.org).
        - Connect with the community on [Twitter](https://twitter.com/ozonechain) and [Facebook](https://facebook.com/ozonechain).
        - Stay updated with the latest developments in blockchain and AI.
        """
    )
