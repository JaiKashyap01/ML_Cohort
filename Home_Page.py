import streamlit as st
from streamlit_extras.switch_page_button import switch_page
st.set_page_config (initial_sidebar_state="collapsed")
st.header('Mammal Classifier')
st.title("Home page")
st.text("Welcome to my mammal classifier.")
st.text("This is a Machine Learling Model that has been trained on over 270 MB")
st.text("worth of images of mammals from across the interenet and ")
st.text("can recognise almost all mammals with a high accuracy.")
st.text("From the blue whale to the tiny shrews and bats, this model can identify them all")
import cv2
st.image("Mammals.jpg", caption="Mammals of the World")
if st.button("next page"):
    switch_page("model_implementation")

    
        
