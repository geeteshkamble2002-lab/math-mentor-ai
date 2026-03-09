# import numpy as np
# from PIL import Image


# def extract_text_from_image(uploaded_file):

#     try:
#         import easyocr

#         reader = easyocr.Reader(['en'], gpu=False)

#         image = Image.open(uploaded_file).convert("RGB")
#         image_np = np.array(image)

#         results = reader.readtext(image_np)

#         extracted_text = []

#         for detection in results:
#             text = detection[1]
#             extracted_text.append(text)

#         return " ".join(extracted_text)

#     except Exception as e:
#         return f"OCR Failed: {str(e)}"


import numpy as np
from PIL import Image
import easyocr
import torch

# Check GPU availability
USE_GPU = torch.cuda.is_available()

print("GPU Available:", USE_GPU)

# Initialize OCR reader once
reader = easyocr.Reader(['en'], gpu=USE_GPU)


def extract_text_from_image(uploaded_file):

    try:
        image = Image.open(uploaded_file).convert("RGB")
        image_np = np.array(image)

        results = reader.readtext(image_np)

        extracted_text = []

        for detection in results:
            text = detection[1]
            extracted_text.append(text)

        if len(extracted_text) == 0:
            return "No text detected"

        return " ".join(extracted_text)

    except Exception as e:
        return f"OCR Error: {str(e)}"