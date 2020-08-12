import streamlit as st
import cv2
import numpy as np
from PIL import Image
st.title("Image Processing using OpenCV")
img=st.file_uploader("Upload any Image here", type=("png", "jpg","jpeg"))
if img is not None:
    imag = Image.open(img)
    st.image(imag,use_column_width=True)
    st.text("Enter below : \n 1 : Gray\n 2 : Blur\n 3 : Hue\n 4 : Flip image Vertically\n 5 : Flip image Horizontally\n 6 : Rotate left\n 7 : Rotate 180 degree \n 8 : Rotate right")
    ss=st.text_input('Enter Text Here : ')
    if(ss=='1'):
        newimg=np.array(imag.convert('RGB'))
        im=cv2.cvtColor(newimg,1)
        ksize=(10,10)
        imgr=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY )
        st.image(imgr,use_column_width=True)
    if(ss=='2'):
        newimg=np.array(imag.convert('RGB'))
        im=cv2.cvtColor(newimg,1)
        ksize=(10,10)
        imgr=cv2.blur(im, ksize )
        st.image(imgr,use_column_width=True)
    if(ss=='3'):
        newimg=np.array(imag.convert('RGB'))
        im=cv2.cvtColor(newimg,1)
        imgr=cv2.cvtColor(im, cv2.COLOR_BGR2HSV )
        st.image(imgr,use_column_width=True)
    if(ss=='4'):
        newimg=np.array(imag.convert('RGB'))
        im=cv2.cvtColor(newimg,1)
        imgr= cv2.flip(im, 0)
        st.image(imgr,use_column_width=True)
    if(ss=='5'):
        newimg=np.array(imag.convert('RGB'))
        im=cv2.cvtColor(newimg,1)
        imgr= cv2.flip(im, 1)
        st.image(imgr,use_column_width=True)
    if(ss=='6'):
        newimg=np.array(imag.convert('RGB'))
        im=cv2.cvtColor(newimg,1)
        imgr=cv2.rotate(im, cv2.cv2.ROTATE_90_CLOCKWISE)
        st.image(imgr,use_column_width=True)
    if(ss=='8'):
        newimg=np.array(imag.convert('RGB'))
        im=cv2.cvtColor(newimg,1)
        imgr=cv2.rotate(im, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
        st.image(imgr,use_column_width=True)
    if(ss=='7'):
        newimg=np.array(imag.convert('RGB'))
        im=cv2.cvtColor(newimg,1)
        imgr=cv2.rotate(im, cv2.cv2.ROTATE_180)
        st.image(imgr,use_column_width=True)
        