import streamlit as st
import cv2
import numpy as np

def main():
    st.title("Image Generations and Pixel Accessing")
    st.subheader("Image Generations")
    h = st.number_input("Height:",min_value=28,value=100)
    w = st.number_input("Width:",min_value=28,value=100)
    
    start_gen = st.button("Generate!")
    if start_gen:
        img = np.random.randint(0,256,size=(h,w))
    
    x,y=0


if __name__ == "__main__":
    main()

