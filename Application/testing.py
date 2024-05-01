import streamlit as st
import os
import requests
from PIL import Image, ImageDraw, ImageFont
from backend import generate_certificates, download_font, generate_certificate

# Main Function to generate certificate with selected font and name position
def main():
    st.set_page_config(page_title="Certificate Creator Baloney", page_icon="📜", layout="wide")
    st.markdown("<h1 style='text-align: center;'>Create Certificates I</h1>", unsafe_allow_html=True)
    st.write("\n")

    st.title("Certificate Generator")
