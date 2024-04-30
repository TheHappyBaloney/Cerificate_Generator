from PIL import Image, ImageDraw, ImageFont
import os
import requests
import zipfile

# Function to download font file from Google Fonts
def download_font(font_name):
    font_file_path = f"{font_name.replace(' ', '_')}.ttf"
    url = f"https://fonts.googleapis.com/css2?family={font_name.replace(' ', '+')}"
    response = requests.get(url)
    css_text = response.text
    font_url_start = css_text.find("url(") + 5
    font_url_end = css_text.find(")", font_url_start) - 1
    font_url = css_text[font_url_start:font_url_end]
    font_response = requests.get(font_url)
    with open(font_file_path, "wb") as font_file:
        font_file.write(font_response.content)
    return font_file_path

# Function to generate certificate with selected font and name position
def generate_certificate(name, font_path, font_size, text_color, template_path, output_path, position):
    template = Image.open(template_path)
    draw = ImageDraw.Draw(template)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, name, fill=text_color, font=font)
    template.save(output_path)

# Function to generate certificates for a list of names
def generate_certificates(names, font_name, font_size, text_color, template_path):
    font_file_path = download_font(font_name)
    os.makedirs("output_certificates", exist_ok=True)

    for name in names:
        output_path = os.path.join("output_certificates", f"{name}_certificate.jpg")
        # Generate certificate with selected font and position
        generate_certificate(name, font_file_path, font_size, text_color, template_path, output_path, (100, 100))

    # Create a zip file containing all the certificates
    with zipfile.ZipFile("certificates.zip", "w") as zipf:
        for file in os.listdir("output_certificates"):
            zipf.write(os.path.join("output_certificates", file), arcname=file)