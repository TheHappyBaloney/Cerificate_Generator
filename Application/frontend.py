import streamlit as st
import os
import requests
from PIL import Image, ImageDraw, ImageFont
from backend import generate_certificates, download_font, generate_certificate

# Main Function to generate certificate with selected font and name position
def main():
    st.set_page_config(page_title="Certificate Creator Baloney", page_icon="📜", layout="wide")
    st.markdown("<h1 style='text-align: center;'>Create Certificates Instantly</h1>", unsafe_allow_html=True)
    st.write("\n")

    st.title("Certificate Generator")

    # Select font from Google Fonts
    font_name = st.selectbox("Select Font from Google Fonts", ["Open Sans", "Roboto", "Lato"])
    
    # Download the selected font
    font_file_path = download_font(font_name)

    # Font size input
    font_size = st.number_input("Enter Font Size", min_value=1, max_value=100, value=12, step=1)
    
    # Text color picker
    text_color = st.text_input("Enter Text Color Hex Code", "#000000")
    
    # Upload template image
    st.header("Upload Template Image")
    template_image = st.file_uploader("Upload a template image", type=["jpg", "png"])

    # Names input
    st.header("Enter Names")
    names_text = st.text_area("Enter each name on a new line")
    names = names_text.split("\n")  # Split the input into a list of names

    # Image preview and name position selection
    st.header("Preview and Position Selection")
    st.write("Use arrow keys to adjust name position")

    # Generate certificates and create a zip file
    if st.button("Generate Certificates"):
        generate_certificates(names, font_name, font_size, text_color, template_image)
        st.write("Certificates generated. Download the zip file.")
        st.download_button("Download Zip File", "certificates.zip")
    
    footer_placeholder = st.empty()
    
    footer_placeholder.markdown("""
    <div style="position: bottom; width: 100%; text-align: center;">
        <h1 style='font-size: 18px;'>This site is brought to you by thehappybaloney. If you have any queries, or suggestions on how this site can be made better feel free to reach out to me on Twitter or Github (@thehappybaloney).</h1>
    </div>
""", unsafe_allow_html=True)
