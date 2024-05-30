import base64
import requests
import pdf2image
from .openAI import OpenAI
import os
import re

# Get the current directory of the script
current_dir = os.path.dirname(__file__)

# Construct the path to the temp directory
temp_directory = os.path.join(current_dir, '..', 'temp')

openAI=OpenAI(html_data="", user_query="",model='gpt-4o')

# Function to convert PDF to images
def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def extract_content(markdown_string):
    # Use a regular expression to match the pattern and extract content
    match = re.search(r'```\s*(.*?)\s*```', markdown_string, re.DOTALL)
    if match:
        print('re : 00')
        return match.group(1)
    match1 = re.search(r'```\s*(.*)', markdown_string, re.DOTALL)
    if match1:
        print('re : 11')
        return match1.group(1)
    return markdown_string




def process_pdf_and_send_ocr(pdf_file):
    
    try:
        # Construct the path to the test.pdf file
        pdf_file = temp_directory+'/'+ pdf_file
        
        
        total_text=''
        images = pdf_to_img(pdf_file)
        for pg, img in enumerate(images):
            
            # Save the image temporarily
            temp_image_path = f"{temp_directory}/page_{pg+1}.jpg"
            img.save(temp_image_path)
            
            # Getting the base64 string
            base64_image = encode_image(temp_image_path)
            
            # GPT
            ocr_text=openAI.gpt_ocr(base64_image)
            
            ocr_text=extract_content(ocr_text)
            
            # Total text
            total_text+=ocr_text
            
            # delete image
            os.remove(temp_image_path)
        
        return total_text
    except Exception as e:
        print('Error in process_pdf_and_send_ocr ',e)
        return ''

        
# # Example usage
# pdf_file = "guide.pdf"
# print(process_pdf_and_send_ocr(pdf_file))