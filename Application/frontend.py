import streamlit as st
import os
import requests
from PIL import Image, ImageDraw, ImageFont
from backend import generate_certificates, download_font, generate_certificate

# Main Function to generate certificate with selected font and name position
def main():
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