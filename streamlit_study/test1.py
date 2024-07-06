import streamlit as st
import pandas as pd

df = pd.read_excel("")

st.title("我的第一个 streamlit 应用")
st.text("欢迎使用 streamlit")

name = st.text_input("请输入您的姓名","匿名")

button = st.button("提交")

if button:
    st.text("你好" + name + "欢迎使用Streamlit！" )
