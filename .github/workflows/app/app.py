import streamlit as st

st.set_page_config(
    page_title="Docker Streamlit Demo",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 Welcome to Docker + Streamlit")
st.write("This app is running inside a Docker container.")

if st.button("Click Me"):
    st.success("Hello from Streamlit running in Docker!")
