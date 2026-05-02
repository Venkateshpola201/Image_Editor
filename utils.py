from PIL import Image
import numpy as np
import cv2
from io import BytesIO


def read_image(uploaded_file):

    image = Image.open(uploaded_file)

    image = np.array(image)

    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    elif image.shape[2] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)

    else:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    return image


def convert_to_download(img):

    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

   
    pil_img = Image.fromarray(img_rgb)


    buffer = BytesIO()

  
    pil_img.save(buffer, format="PNG")

    return buffer.getvalue()