import streamlit as st

from streamlit_app.settings import Settings


def main() -> None:
    settings = Settings()

    st.set_page_config(page_title=settings.app_name, page_icon="✨", layout="centered")

    st.title(settings.app_name)
    st.write(
        "This is a minimal, professional Streamlit app packaged as a Python project."
    )

    name = st.text_input("Your name", placeholder="Type your name...")
    if name:
        st.success(f"Hello, {name}!")


if __name__ == "__main__":
    main()
