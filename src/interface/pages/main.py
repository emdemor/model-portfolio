import streamlit as st

name: str = "Página Principal"


def render():
    st.title("Bem-vindo ao Aplicativo Principal")
    st.write("Esta é a página principal do sistema.")
