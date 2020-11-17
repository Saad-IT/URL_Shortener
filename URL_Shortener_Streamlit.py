import streamlit as st
import pandas as pd
import pyshorteners
from PIL import Image
import time


st.title("URL Shortener")
st.markdown("@Author: Syed Saad Ali")
image=Image.open("URL_Shortener_Image.jpg")
st.image(image,use_column_width=True)
st.markdown("Enter Your URL Here:")
url=st.text_input("")
bt=st.button("Enter")



if url and bt:
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)
    
    st.markdown("Shorter URL:")
    st.write(pyshorteners.Shortener().tinyurl.short(url))

#st.progress()
