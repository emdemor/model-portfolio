import streamlit as st


name: str = "Aplicativo 2"
order: int = 2


def render():
    st.title("Bem-vindo ao Aplicativo 2")
    st.write("Este é o segundo aplicativo.")
