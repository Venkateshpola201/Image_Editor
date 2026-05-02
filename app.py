import streamlit as st
import cv2

from filters import (
    apply_blur,
    apply_sharpness,
    apply_brightness,
    apply_constrast,
    apply_edge_detection,
    apply_grayscale,
    apply_sepia,
    apply_cartoon,
    rotate_image,
    flip_image,
    resize_image
)

from utils import (
    read_image,
    convert_to_download
)


# PAGE CONFIG
st.set_page_config(
    page_title="Image Editor",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ Image Editor using Streamlit & OpenCV")


# RESET BUTTON
reset = st.sidebar.button("Reset Filters")


# SIDEBAR
st.sidebar.header("Image Filters")


# BASIC FILTERS
blur_value = st.sidebar.slider(
    "Blur",
    1,
    51,
    1 if reset else 1,
    step=2
)

sharpness_value = st.sidebar.slider(
    "Sharpness",
    0.0,
    3.0,
    0.0 if reset else 0.0
)

brightness_value = st.sidebar.slider(
    "Brightness",
    -100,
    100,
    0 if reset else 0
)

contrast_value = st.sidebar.slider(
    "Contrast",
    0.5,
    3.0,
    1.0 if reset else 1.0
)


# TOGGLE FILTERS
edge_toggle = st.sidebar.checkbox(
    "Edge Detection",
    value=False if reset else False
)

gray_toggle = st.sidebar.checkbox(
    "Grayscale",
    value=False if reset else False
)

sepia_toggle = st.sidebar.checkbox(
    "Sepia",
    value=False if reset else False
)

cartoon_toggle = st.sidebar.checkbox(
    "Cartoon",
    value=False if reset else False
)


# EDGE THRESHOLDS
t1 = st.sidebar.slider(
    "Threshold 1",
    0,
    255,
    100 if reset else 100
)

t2 = st.sidebar.slider(
    "Threshold 2",
    0,
    255,
    200 if reset else 200
)


# ROTATION
angle = st.sidebar.slider(
    "Rotate Image",
    -180,
    180,
    0 if reset else 0
)


# FLIP
flip_option = st.sidebar.selectbox(
    "Flip Image",
    [
        "None",
        "Horizontal",
        "Vertical",
        "Both"
    ],
    index=0
)


# RESIZE
st.sidebar.subheader("Resize Image")

width = st.sidebar.slider(
    "Width",
    100,
    1000,
    500 if reset else 500
)

height = st.sidebar.slider(
    "Height",
    100,
    1000,
    500 if reset else 500
)


# FILE UPLOAD
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)


# PROCESS IMAGE
if uploaded_file is not None:

    original = read_image(uploaded_file)

    processed = original.copy()


    # APPLY FILTERS
    processed = apply_blur(
        processed,
        blur_value
    )

    processed = apply_sharpness(
        processed,
        sharpness_value
    )

    processed = apply_brightness(
        processed,
        brightness_value
    )

    processed = apply_constrast(
        processed,
        contrast_value
    )


    # EDGE DETECTION
    if edge_toggle:

        processed = apply_edge_detection(
            processed,
            t1,
            t2
        )


    # GRAYSCALE
    if gray_toggle:

        processed = apply_grayscale(
            processed
        )


    # SEPIA
    if sepia_toggle:

        processed = apply_sepia(
            processed
        )


    # CARTOON
    if cartoon_toggle:

        processed = apply_cartoon(
            processed
        )


    # ROTATION
    if angle != 0:

        processed = rotate_image(
            processed,
            angle
        )


    # FLIP
    if flip_option == "Horizontal":

        processed = flip_image(
            processed,
            1
        )

    elif flip_option == "Vertical":

        processed = flip_image(
            processed,
            0
        )

    elif flip_option == "Both":

        processed = flip_image(
            processed,
            -1
        )


    # RESIZE
    processed = resize_image(
        processed,
        width,
        height
    )


    # DISPLAY IMAGES
    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Original Image")

        st.image(
            cv2.cvtColor(
                original,
                cv2.COLOR_BGR2RGB
            ),
            use_container_width=True
        )


    with col2:

        st.subheader("Processed Image")

        st.image(
            cv2.cvtColor(
                processed,
                cv2.COLOR_BGR2RGB
            ),
            use_container_width=True
        )


    # DOWNLOAD BUTTON
    image_bytes = convert_to_download(
        processed
    )

    st.download_button(
        label="⬇️ Download Image",
        data=image_bytes,
        file_name="edited_image.png",
        mime="image/png"
    )