from PIL import Image
import cv2
import numpy as np
from io import BytesIO

def pil_to_cv2(pil_image):

    image = np.array(pil_image)

    return cv2.cvtColor(
        image,
        cv2.COLOR_RGB2BGR
    )


def cv2_to_pil(cv_image):

    if len(cv_image.shape) == 2:

        return Image.fromarray(cv_image)

    rgb = cv2.cvtColor(
        cv_image,
        cv2.COLOR_BGR2RGB
    )

    return Image.fromarray(rgb)


def image_to_bytes(pil_image):

    buffer = BytesIO()

    pil_image.save(buffer, format="PNG")

    return buffer.getvalue()