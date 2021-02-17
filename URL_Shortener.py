import streamlit as st
import pandas as pd
import pyshorteners                                  
from PIL import Image
import time
import webbrowser


st.title("URL Shortener")
image=Image.open("URL_Shortener_logo.jpg")
st.image(image,use_column_width=True)
st.sidebar.title("URL Shortener ✂️")
if st.sidebar.checkbox("How it works?",False,key=1):
    st.sidebar.info("Type or paste valid url and click on 'Enter' button. You will get shorted url.")

st.sidebar.markdown("Developed by: ")
st.sidebar.subheader("Syed Saad Ali \n  (B.Tech (IT) Student)")
st.sidebar.markdown("Follow on: ")
st.sidebar.success("Github: https://github.com/Saad-IT")
st.sidebar.success("Linkedin: https://www.linkedin.com/in/saad-ali-syed-b88830193")


st.markdown("⌨️ Enter Your URL Here:")
url=st.text_input("")
bt=st.button("Enter")


if url and bt:
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)
    
    st.markdown("✔️ Shorted URL:")
    try:
        st.write(pyshorteners.Shortener().tinyurl.short(url))
    except:
        st.error("⚠️ Please Enter Valid URL")

