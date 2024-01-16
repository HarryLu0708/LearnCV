import streamlit as st
import cv2

def main():
    cap = cv2.VideoCapture(0)
    st.title("Video Streaming Demo")
    stop = st.button("Stop")
    frame_placeholder = st.empty()
    while cap.isOpened() and not stop:
        ret, frame = cap.read()
        if not ret:
            st.write("Video capture has ended.")
            break
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame,channels="RGB")
        if stop:
            break
    cap.release()

if __name__=="__main__":
    main()


