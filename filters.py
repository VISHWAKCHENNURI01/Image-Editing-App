import cv2
import numpy as np

def apply_blur(image, ksize):

    if ksize > 1:
        image = cv2.GaussianBlur(
            image,
            (ksize, ksize),
            0
        )

    return image


def apply_sharpness(image, alpha):

    blurred = cv2.GaussianBlur(image, (0, 0), 3)

    sharpened = cv2.addWeighted(
        image,
        1 + alpha,
        blurred,
        -alpha,
        0
    )

    return sharpened


def adjust_brightness(image, beta):

    return cv2.convertScaleAbs(
        image,
        alpha=1,
        beta=beta
    )


def adjust_contrast(image, alpha):

    return cv2.convertScaleAbs(
        image,
        alpha=alpha,
        beta=0
    )


def apply_edge_detection(image, thresh1, thresh2):

    edges = cv2.Canny(
        image,
        thresh1,
        thresh2
    )

    return edges


def apply_grayscale(image):

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    return gray