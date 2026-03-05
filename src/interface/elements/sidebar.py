import os
from typing import Any

from interface.utils import get_app_name
import streamlit as st

from interface import config


def sidebar(pages: dict[str, Any]):
    left_co, cent_co, last_co = st.columns(3)
    with cent_co:
        st.sidebar.image(config.LOGO_FILEPATH, width=150)

    st.sidebar.header("Configurações")

    pages_list = [get_app_name(app_name, pages) for app_name in pages]

    if pages_list:
        st.sidebar.selectbox(
            "Aplicação",
            pages_list,
            placeholder="Selecione o app",
            key="app_name",
            on_change=update_app_name,
        )



def update_app_name():
    pass
    # if "app_name" in st.session_state:
    #     print(f"[INFO] app_name updated to '{st.session_state['app_name']}'")
