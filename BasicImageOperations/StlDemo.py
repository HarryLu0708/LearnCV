import streamlit as stl
import cv2
import numpy as np
from PIL import Image

def main():
    stl.title("First Streamlit Demo")
    stl.subheader("By Astropower")
    stl.text("A simple image uploader.")

    image_file = stl.file_uploader("Upload your picture",type=["jpg","png","jpeg"])
    if not image_file:
        return None
    o_img = Image.open(image_file)
    o_img = np.array(o_img)
    # image 
    trans_img = cv2.cvtColor(o_img,cv2.COLOR_BGR2GRAY)
    stl.text("Original Image:")
    stl.image([o_img])
    stl.text("Gray Image:")
    stl.image([trans_img])

if __name__=="__main__":
    main()


