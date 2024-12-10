import streamlit as sl

sl.set_page_config(layout="wide")
col1, col2 = sl.columns(2)
content = """
Hi, I am Eric. I like to dabble in many things within IT. 
"""
content2 = """
Below you can find some apps that I have built in Python. 
Feel free to contact!
"""

with col1:
    sl.image("images/photo.jpg")

with col2:
    sl.title("Eric Kornacki")
    sl.write(content)

sl.write(content2)