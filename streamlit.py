import streamlit as st
from PIL import Image
#app = Flask(__name__)
import requests
import json


def main():
    
    html_temp = """
    <div style="background-color:Green;padding:10px">
    <h2 style="color:white;text-align:center;">Consumer Complaint App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    Text = st.text_input("Enter your Text here")
    result=""
    obj=""    
    if st.button("Predict"):
        txt={"text":Text}
        url = 'http://127.0.0.1:8000/predict'
        x = requests.post(url, json = txt)
        obj=x.json()
        result = obj[0] 
    st.success(result)
    

if __name__== '__main__':
    main()
