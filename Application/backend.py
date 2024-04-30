from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import requests

# Function to download font file from Google Fonts
def download_font(font_name, font_file_path):
    url = f"https://fonts.googleapis.com/css2?family={font_name.replace(' ', '+')}"
    response = requests.get(url)
    css_text = response.text
    font_url_start = css_text.find("url(") + 5
    font_url_end = css_text.find(")", font_url_start) - 1
    font_url = css_text[font_url_start:font_url_end]
    font_response = requests.get(font_url)
    with open(font_file_path, "wb") as font_file:
        font_file.write(font_response.content)

# Function to generate certificate with selected font and name position
def generate_certificate(name, font_path, font_size, text_color, template_path, output_path, position):
    template = Image.open(template_path)
    draw = ImageDraw.Draw(template)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, name, fill=text_color, font=font)
    template.save(output_path)

# Modify this function to handle font size and text color
def generate_certificates_from_csv(csv_path, font_name, font_size, text_color, template_path, font_file_path):
    df = pd.read_csv(csv_path)
    os.makedirs("output_certificates", exist_ok=True)


    for index, row in df.iterrows():
        name = row["Name"]
        output_path = os.path.join("output_certificates", f"{name}_certificate.jpg")
        # Generate certificate with selected font and position
        generate_certificate(name, font_file_path, template_path, output_path, (100, 100))

