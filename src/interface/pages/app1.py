import streamlit as st


name: str = "Aplicativo 1"
order: int = 1
requires_auth: bool = True

def render():
    st.title("Bem-vindo ao Aplicativo 1")
    st.write("Este é o primeiro aplicativo.")
