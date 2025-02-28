import os
import PySimpleGUI as sg
from google.cloud import vision
import logging
import json
import time  

try:
    from google.cloud import vision
    print("Google Cloud Vision API client library is installed.")
except ImportError:
    print("Google Cloud Vision API client library is NOT installed.")


from dotenv import load_dotenv
load_dotenv()


client = vision.ImageAnnotatorClient()


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def extract_text_from_image(image_path):
    try:
        logging.debug(f"Extracting text from image: {image_path}")
        with open(image_path, 'rb') as image_file:
            content = image_file.read()
        image = vision.Image(content=content)
        logging.debug("Sending Google Vision API request...")  
        response = client.text_detection(image=image)
        logging.debug("Received Google Vision API response.") 
        if response.error.message:
            logging.error(f"Google Vision API error: {response.error.message}")
            return None
        texts = response.text_annotations
        if texts:
            result = []
            for text in texts:
                vertices = [{"x": vertex.x, "y": vertex.y} for vertex in text.bounding_poly.vertices]
                result.append({
                    "description": text.description,
                    "bounding_poly": vertices
                })
            return result
        else:
            return []
    except Exception as e:
        logging.error(f"Error extracting text: {e}")
        return None


# Main window layout
main_layout = [[sg.Button('Browse')]]
main_window = sg.Window('Image Selector', main_layout, resizable=True)

while True:
    event, values = main_window.read(timeout=100)
    if event in (sg.WIN_CLOSED, "Exit"):
        logging.debug("Main window closed")
        break
    if event == "Browse":
        logging.debug("Browse button clicked")
        image_path = sg.popup_get_file("Select Image", file_types=(("Image Files", "*.png;*.jpg;*.jpeg"), ("All Files", "*.*")))
        if image_path:
            logging.debug(f"Image selected: {image_path}")
            time.sleep(5) 
            text_data = extract_text_from_image(image_path)
            if text_data is not None:
                try:
                    output_path = os.path.join(os.path.dirname(image_path), "vision.json")
                    with open(output_path, 'w') as json_file:
                        json.dump(text_data, json_file, indent=4)
                    sg.popup("Text extraction complete. Results saved to vision.json.")
                    logging.debug(f"Text extraction saved to: {output_path}")
                except Exception as save_err:
                    logging.error(f"Error saving JSON: {save_err}")
                    sg.popup_error(f"Error saving JSON: {save_err}")
            else:
                sg.popup("No text found or error occurred during extraction.")

main_window.close()