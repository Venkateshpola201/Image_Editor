import cv2
import numpy as np


def apply_blur(img, ksize):
    if ksize % 2==0:
        ksize1+= 1
    return cv2.GaussianBlur(img, (ksize, ksize), 0)


def apply_sharpness(img, alpha):
    blurred = cv2.GaussianBlur(img, (0,0), 3)
    sharp = cv2.addWeighted(img, 1 + alpha, blurred, -alpha, 0)
    return sharp

def apply_brightness(img, beta):
    return cv2.convertScaleAbs(img, beta = beta)
   
def apply_constrast(img, alpha):
    return cv2.convertScaleAbs(img, alpha=alpha)

def apply_edge_detection(img, t1, t2):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, t1, t2)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

def apply_grayscale(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

def apply_sepia(img):
    kernel = np.array([
        [0.272, 0.534, 0.131],
        [0.349, 0.686, 0.168],
        [0.393, 0.769, 0.189]
    ])

    sepia = cv2.transform(img, kernel)
    sepia = np.clip(sepia, 0, 255)

    return sepia.astype(np.uint8)


def apply_cartoon(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        9
    )

    color = cv2.bilateralFilter(img, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon



def rotate_image(img, angle):
    height, width = img.shape[:2]

    center = (width // 2, height // 2)

    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    rotated = cv2.warpAffine(
        img,
        matrix,
        (width, height)
    )

    return rotated

def flip_image(img, mode):
    return cv2.flip(img, mode)


def resize_image(img, width, height):
    return cv2.resize(img, (width, height))