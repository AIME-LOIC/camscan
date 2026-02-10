import pytesseract
from PIL import Image

def get_text_from_image(image_path):
    try:
        # Grayscale helps OCR accuracy
        img = Image.open(image_path).convert('L')
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error reading image: {e}"
