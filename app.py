import streamlit as st
from PIL import Image
import cv2
import numpy as np

from filters import(
    apply_blur,
    apply_sharpness,
    adjust_brightness,
    adjust_contrast,
    apply_edge_detection,
    apply_grayscale
)

from utils import (
    pil_to_cv2,
    cv2_to_pil,
    image_to_bytes
)

st.set_page_config(
    page_title="Image Editing App",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ Image Editing App with Streamlit & OpenCV")

st.sidebar.header("Filter Controls")

blur_value = st.sidebar.slider(
    "Blur Kernel Size",
    1, 51, 1, step=2
    )

sharpness_value = st.sidebar.slider(
    "Sharpness",
    0.0, 3.0, 1.0
)

brightness_value = st.sidebar.slider(
    "Brightness",
    -100, 100, 0
)

contrast_value = st.sidebar.slider(
    "Contrast",
    0.5, 3.0, 1.0
)

edge_detect = st.sidebar.checkbox("Enable Edge Detection")

thresh1 = st.sidebar.slider(
    "Threshold 1",
    0, 255, 100
)

thresh2 = st.sidebar.slider(
    "Threshold 2",
    0, 255, 200
)

grayscale = st.sidebar.checkbox("Convert to Grayscale")

# Reset button
if st.sidebar.button("Reset Filters"):
    st.experimental_rerun()

# File uploader
uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Load image
    pil_image = Image.open(uploaded_file).convert("RGB")

    # Convert to OpenCV format
    image = pil_to_cv2(pil_image)

    # Copy original image
    processed = image.copy()

    # Apply filters sequentially
    processed = apply_blur(processed, blur_value)
    processed = apply_sharpness(processed, sharpness_value)
    processed = adjust_brightness(processed, brightness_value)
    processed = adjust_contrast(processed, contrast_value)

    if edge_detect:
        processed = apply_edge_detection(
            processed,
            thresh1,
            thresh2
        )

    if grayscale:
        processed = apply_grayscale(processed)

    # Convert processed image for display
    processed_pil = cv2_to_pil(processed)

    # Display images side by side
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(pil_image, use_column_width=True)

    with col2:
        st.subheader("Processed Image")
        st.image(processed_pil, use_column_width=True)

    # Download button
    img_bytes = image_to_bytes(processed_pil)

    st.download_button(
        label="Download Processed Image",
        data=img_bytes,
        file_name="processed_image.png",
        mime="image/png"
    )