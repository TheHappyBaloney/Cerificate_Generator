import streamlit as st
import os
import requests
from PIL import Image, ImageDraw, ImageFont
from backend import generate_certificates_from_csv , download_font, generate_certificate

# Main Function to generate certificate with selected font and name position
def main():
    st.title("Certificate Generator")

    # Select font from Google Fonts
    font_name = st.selectbox("Select Font from Google Fonts", ["Open Sans", "Roboto", "Lato"])

    # Search bar for font selection
    search_query = st.text_input("Search Fonts")
    
    # Font size input
    font_size = st.number_input("Enter Font Size", min_value=1, max_value=100, value=12, step=1)
    
    # Text color picker
    text_color = st.color_picker("Select Text Color", "#000000")
    
    # Upload template image
    st.header("Upload Template Image")
    template_image = st.file_uploader("Upload a template image", type=["jpg", "png"])

    # Name input
    name = st.text_input("Enter Name")

    # Image preview and name position selection
    st.header("Preview and Position Selection")
    st.write("Use arrow keys to adjust name position")
    # Show image preview here

    # Generate button
    if st.button("Generate Certificate"):
        if not template_image or not name:
            st.error("Please upload template image and enter a name.")
        else:
            # Download font file
            font_file_path = f"{font_name.replace(' ', '_').lower()}.ttf"
            download_font(font_name, font_file_path)

            # Generate certificate
            output_path = f"output_certificates/{name}_certificate.jpg"
            generate_certificate(name, font_file_path, template_image, output_path, (100, 100))
            st.success("Certificate generated successfully!")

if __name__ == "__main__":
    main()
