from PIL import Image
import pytesseract
from gtts import gTTS
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

filename = 'imgg.jpeg'

file_path = os.path.join(current_directory, filename)

tesseract_path = '/usr/bin/tesseract'
pytesseract.pytesseract.tesseract_cmd = tesseract_path

try:
    img = Image.open(file_path)

    text = pytesseract.image_to_string(img, lang='tam')

    tts = gTTS(text=text, lang='ta', slow=False)
    tts.save("tamil_audio.mp3")
    print("Audio saved as 'tamil_audio.mp3'")

except ImportError as e:
    print("Error: try to install 'pip install pillow pytesseract gtts'.")
except FileNotFoundError as e:
    print(f"Error: The file {filename} was not found in the directory {current_directory}.")
except pytesseract.TesseractNotFoundError as e:
    print("Error: Tesseract is not installed or the path is incorrect.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
