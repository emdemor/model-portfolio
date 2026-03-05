import importlib
import pkgutil

from interface.utils import get_app_name
import streamlit as st

from interface import config
from interface.elements.settings import initiate_session_state, page_config
from interface.elements.sidebar import sidebar
import interface.pages


def get_pages():
    """
    Lista todos os módulos em 'interface.pages' e retorna um dicionário
    com o nome do módulo e a referência do módulo.
    """
    pages = {}
    package = interface.pages

    for _, module_name, is_pkg in pkgutil.iter_modules(package.__path__):
        if not is_pkg:  # Ignorar pacotes, listar apenas módulos
            module_path = f"{package.__name__}.{module_name}"
            module = importlib.import_module(module_path)
            pages[module_name] = module

    return pages


def front():
    page_config(layout="centered", sidebar="auto")
    initiate_session_state()
    pages = get_pages()
    app_names = [get_app_name(label, pages) for label in pages]
    app_name_map = {get_app_name(label, pages): label for label in pages}

    sidebar(pages)
    

    app_name = st.session_state.get("app_name", "Página Principal")
    if app_name in app_names:
        module_key = app_name_map[app_name]
        pages[module_key].render()
    else:
        st.title(config.TITLE)
        st.text(f"App '{app_name}' não encontrado.")
