import streamlit as st

def local_css(file_name):
    """
    Load and apply a local CSS file to the Streamlit app.
    
    Args:
        file_name (str): Path to the CSS file.
    """
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Custom CSS file not found.")