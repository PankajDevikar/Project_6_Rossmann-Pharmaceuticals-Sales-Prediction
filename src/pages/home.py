# imports
import streamlit as st
import awesome_streamlit as ast

def write():
    """Used to write the page in the app.py file"""
    st.title('Rossmann Pharmaceuticals')
    st.write('\n\n\n\n')
    
    # Display company logo or relevant image with a caption
    st.image("src/images/rosssman.jpg", caption="Rossmann Pharmaceuticals - Delivering Health Across Europe")
    st.write('---')
    
    # Company description and project overview
    st.markdown(
        """
        **Rossmann Pharmaceuticals** is an international pharmaceutical company that operates over 3,000 drug stores 
        in 7 European countries. Currently, the finance team at Rossmann is focused on predicting daily sales for 
        up to six weeks in advance, helping to optimize operations and improve inventory management across its stores.
        """
    )
