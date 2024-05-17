import streamlit as st
from PIL import Image
with st.expander("Start Camera"):
    cam_image=st.camera_input("Camera")
uploaded_img=st.file_uploader("Uploaded image")
if cam_image:
    img=Image.open(cam_image)
    gray_img=img.convert("L")
    st.image(gray_img)
if uploaded_img:
    img=Image.open(uploaded_img)
    gray_img=img.convert("L")
    st.image(gray_img)