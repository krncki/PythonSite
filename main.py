import streamlit as sl

sl.set_page_config(layout="wide")
col1, col2 = sl.columns(2)

with col1:
    sl.image("images/photo.jpg")

with col2:
    sl.title("Eric Kornacki")
    content = """
    Hi, I am Eric. I like to dabble in many things within IT. 
    """
    sl.write(content)
